# Numerology Intelligence System — DSA Mini Project

A full-stack educational mini project demonstrating name-number calculation, a custom singly linked list, SQLite persistence, CRUD operations, and frequency/pattern analysis.

## Technology stack
- Python 3.10+ and Flask
- Custom singly linked list (not Python's built-in list as the primary record structure)
- SQLite database
- HTML, CSS and JavaScript
- Chart.js for the frequency chart

## 1. Setup

Install Python 3.10 or newer. Open a terminal in this project folder.

### Windows
```bash
py -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

If `py` is not recognised on Windows, use `python` instead. If the `python` command is not recognised, install Python from python.org and enable the PATH option during installation.

## 2. How to use
1. Enter a name in Name Analyzer and select Analyse.
2. The application computes the letter values, total and final number.
3. The record is inserted at the end of the custom singly linked list and saved in SQLite.
4. Use Edit and Delete in the records table to demonstrate update and deletion.
5. Search using the search field.
6. Review the frequency chart and dataset insights.
7. Select Export CSV to download records.

## 3. Numerology rule used
Pythagorean mapping:
- 1: A, J, S
- 2: B, K, T
- 3: C, L, U
- 4: D, M, V
- 5: E, N, W
- 6: F, O, X
- 7: G, P, Y
- 8: H, Q, Z
- 9: I, R

All alphabetic characters in the name are mapped and summed. The total is repeatedly reduced by summing its digits until one digit remains, except master numbers 11, 22 and 33, which are preserved. Spaces and punctuation are ignored. Accented Latin letters are normalized (for example, José becomes JOSE). Names with no English alphabetic characters are rejected.

Examples: ADA = 1 + 4 + 1 = 6. ADA LOVELACE = 36, which reduces to 9.

## 4. DSA implementation
The custom `SinglyLinkedList` class is implemented in `linked_list.py`. Each node stores a record dictionary and a `next` reference. The API uses this structure for traversal, search, update and deletion. SQLite is the persistent store; the linked list is rebuilt from SQLite when the application starts.

| Operation | Implementation | Time complexity |
|---|---|---|
| Insert at end | Traverse to tail, attach new node | O(n) |
| Search by ID | Sequential node traversal | O(n) |
| Update by ID | Search, then replace node data | O(n) |
| Delete by ID | Search with previous/current pointers | O(n) |
| Traverse | Visit every node | O(n) |
| Frequency analysis | Traverse + hash-map Counter | O(n) expected |

Space complexity: O(n) for n linked-list nodes. Frequency analysis uses O(k) additional space, where k is the number of distinct numerology results.

**Extension discussion:** A maintained tail pointer would make insertion at the end O(1). A doubly linked list could simplify backward traversal/deletion when a node reference is already known, at the cost of an extra pointer per node.

## 5. API reference
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Health check |
| GET | `/api/records` | Traverse and return all records |
| POST | `/api/records` | Calculate and insert a record |
| GET | `/api/records/<id>` | Search a record |
| PUT | `/api/records/<id>` | Update a record |
| DELETE | `/api/records/<id>` | Delete a record |
| GET | `/api/analytics` | Frequency and pattern analysis |
| GET | `/api/export` | Export records as CSV |

POST/PUT JSON body: `{"name": "Ada Lovelace"}`.

## 6. Run tests
```bash
python -m unittest discover -s tests -v
```
The tests cover numerology calculation, normalization, invalid input, master numbers, linked-list operations, API CRUD, analytics and health check.

## 7. Troubleshooting
- **ModuleNotFoundError: flask** — activate the virtual environment and run `python -m pip install -r requirements.txt`.
- **Address already in use** — close the other server window or change port 5000 in `app.py`.
- **Blank page / chart not loading** — check internet access because Chart.js is loaded from a CDN; the core API and record operations still run locally.
- **Changes not appearing** — refresh the browser; check the terminal for server errors.
- **Database reset for a clean demo** — stop the server, delete `numerology.db`, and restart. This permanently removes demo records.
- **PowerShell activation blocked** — use Command Prompt, or follow your institution's approved PowerShell execution policy guidance.

## 8. Academic note
Numerology is included as an example domain for applying data structures and algorithmic analysis. The output is not scientifically established as a predictor of personality, compatibility or future events.
