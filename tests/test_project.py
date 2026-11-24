import tempfile
import unittest
from pathlib import Path

from app import create_app
from linked_list import SinglyLinkedList
from numerology import calculate_name_number, reduce_number


class NumerologyTests(unittest.TestCase):
    def test_ada_lovelace_calculation(self):
        result = calculate_name_number("Ada Lovelace")
        self.assertEqual(result["normalized_name"], "ADALOVELACE")
        self.assertEqual(result["total"], 36)
        self.assertEqual(result["numerology_number"], 9)

    def test_accents_and_spaces(self):
        self.assertEqual(calculate_name_number("José").get("normalized_name"), "JOSE")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            calculate_name_number("  123 !! ")

    def test_master_number(self):
        self.assertEqual(reduce_number(22), 22)
        self.assertEqual(reduce_number(29), 11)  # 2+9=11 is a master number
        self.assertEqual(reduce_number(28), 1)


class LinkedListTests(unittest.TestCase):
    def test_insert_search_update_delete_traverse(self):
        linked = SinglyLinkedList()
        linked.insert_end({"id": 1, "name": "A"})
        linked.insert_end({"id": 2, "name": "B"})
        self.assertEqual(len(linked), 2)
        self.assertEqual(linked.search(2).data["name"], "B")
        self.assertTrue(linked.update(2, {"id": 2, "name": "Bee"}))
        self.assertEqual(linked.traverse()[1]["name"], "Bee")
        self.assertTrue(linked.delete(1))
        self.assertEqual([x["id"] for x in linked.traverse()], [2])
        self.assertFalse(linked.delete(999))


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        db_path = str(Path(self.temp_dir.name) / "test.db")
        self.app = create_app({"TESTING": True, "DATABASE_PATH": db_path})
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_read_update_delete(self):
        response = self.client.post("/api/records", json={"name": "Ada Lovelace"})
        self.assertEqual(response.status_code, 201)
        record_id = response.get_json()["record"]["id"]
        self.assertEqual(self.client.get("/api/records").get_json()["count"], 1)
        self.assertEqual(self.client.get(f"/api/records/{record_id}").status_code, 200)
        self.assertEqual(self.client.put(f"/api/records/{record_id}", json={"name": "Grace Hopper"}).status_code, 200)
        self.assertEqual(self.client.delete(f"/api/records/{record_id}").status_code, 200)
        self.assertEqual(self.client.get("/api/records").get_json()["count"], 0)

    def test_validation_and_analytics(self):
        self.assertEqual(self.client.post("/api/records", json={"name": "123"}).status_code, 400)
        self.client.post("/api/records", json={"name": "Ada"})
        self.client.post("/api/records", json={"name": "Bob"})
        analytics = self.client.get("/api/analytics").get_json()
        self.assertEqual(analytics["total_records"], 2)

    def test_health(self):
        self.assertTrue(self.client.get("/api/health").get_json()["success"])


if __name__ == "__main__":
    unittest.main()
