"""Flask application: REST API + linked-list-backed numerology dashboard."""
from collections import Counter
from flask import Flask, jsonify, render_template, request, Response
import csv
import io

from database import Database
from linked_list import SinglyLinkedList
from numerology import calculate_name_number


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(test_config or {})
    db = Database(app.config.get("DATABASE_PATH"))
    records = SinglyLinkedList.from_iterable(db.get_all())
    app.extensions["numerology_db"] = db
    app.extensions["numerology_list"] = records

    def refresh_list():
        records.clear()
        for item in db.get_all():
            records.insert_end(item)

    def error(message, status=400):
        return jsonify({"success": False, "error": message}), status

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/api/records")
    def get_records():
        return jsonify({"success": True, "records": records.traverse(), "count": len(records)})

    @app.post("/api/records")
    def add_record():
        payload = request.get_json(silent=True) or {}
        name = payload.get("name", "")
        try:
            result = calculate_name_number(name)
        except ValueError as exc:
            return error(str(exc))
        record = db.create({
            "original_name": name.strip(),
            "normalized_name": result["normalized_name"],
            "total": result["total"],
            "numerology_number": result["numerology_number"],
        })
        records.insert_end(record)
        return jsonify({"success": True, "record": record, "calculation": result}), 201

    @app.get("/api/records/<int:record_id>")
    def search_record(record_id):
        node = records.search(record_id)
        if node is None:
            return error("Record not found.", 404)
        return jsonify({"success": True, "record": node.data})

    @app.put("/api/records/<int:record_id>")
    def update_record(record_id):
        if records.search(record_id) is None:
            return error("Record not found.", 404)
        payload = request.get_json(silent=True) or {}
        name = payload.get("name", "")
        try:
            result = calculate_name_number(name)
        except ValueError as exc:
            return error(str(exc))
        update_data = {
            "original_name": name.strip(),
            "normalized_name": result["normalized_name"],
            "total": result["total"],
            "numerology_number": result["numerology_number"],
        }
        db.update(record_id, update_data)
        refresh_list()
        return jsonify({"success": True, "record": db.get(record_id), "calculation": result})

    @app.delete("/api/records/<int:record_id>")
    def delete_record(record_id):
        if not records.delete(record_id):
            return error("Record not found.", 404)
        db.delete(record_id)
        return jsonify({"success": True, "message": "Record deleted."})

    @app.get("/api/analytics")
    def analytics():
        all_records = records.traverse()
        counts = Counter(str(item["numerology_number"]) for item in all_records)
        total = len(all_records)
        distribution = [
            {"number": int(number), "frequency": count,
             "percentage": round((count / total) * 100, 2) if total else 0}
            for number, count in sorted(counts.items(), key=lambda pair: int(pair[0]))
        ]
        most_common = counts.most_common(1)
        return jsonify({
            "success": True,
            "total_records": total,
            "unique_numbers": len(counts),
            "distribution": distribution,
            "most_frequent": (
                {"number": int(most_common[0][0]), "frequency": most_common[0][1]}
                if most_common else None
            ),
            "repeated_number_groups": [
                item for item in distribution if item["frequency"] > 1
            ],
        })

    @app.get("/api/export")
    def export_csv():
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=[
            "id", "original_name", "normalized_name", "total",
            "numerology_number", "created_at"
        ])
        writer.writeheader()
        writer.writerows(records.traverse())
        return Response(
            output.getvalue(), mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=numerology_records.csv"}
        )

    @app.get("/api/health")
    def health():
        return jsonify({"success": True, "status": "healthy",
                        "linked_list_records": len(records)})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
