# Five-member work allocation and integration plan

The work is divided into five sections. Each member owns a deliverable and must explain their module during the demonstration. Replace Member 1–5 with actual names and roll numbers.

## Member 1 — Research, IKS framing and numerology engine
**Owns:** `numerology.py`, report sections 1–5 and the mapping explanation.  
**Tasks:** explain the selected Pythagorean mapping; implement normalization, letter mapping, digit reduction and validation; verify test examples; write a balanced IKS comparison distinguishing the chosen convention from Indian traditions.  
**Deliverables:** calculation module, mapping table, two worked examples, IKS note and references approved by faculty.  
**Must explain:** Why normalization is needed; how the mapping works; how 11, 22 and 33 are treated; why numerology is not presented as scientific prediction.

## Member 2 — DSA and linked-list implementation
**Owns:** `linked_list.py`, DSA algorithm descriptions and complexity table.  
**Tasks:** implement Node and SinglyLinkedList; demonstrate insert-at-end, search, update, delete and traversal; test head deletion, middle deletion, tail deletion, empty list and missing ID.  
**Deliverables:** linked-list source, pseudocode, pointer diagrams and complexity analysis.  
**Must explain:** head, next, NULL, node, traversal, pointer relinking, O(n) operations and tail-pointer optimisation.

## Member 3 — Backend and database
**Owns:** `app.py`, `database.py`, API reference and persistence explanation.  
**Tasks:** implement Flask routes; connect JSON requests to calculation and linked-list methods; create SQLite schema; handle invalid input and not-found responses; verify that database and in-memory list stay consistent.  
**Deliverables:** backend source, endpoint table, sample API requests/responses and database schema.  
**Must explain:** client-server architecture, REST methods, JSON, SQLite, primary key, validation and why the linked list is reconstructed at startup.

## Member 4 — Frontend and user experience
**Owns:** `templates/index.html`, `static/style.css`, `static/app.js`.  
**Tasks:** build responsive dashboard; connect form and table to APIs; display results; implement search, edit/delete controls, chart and CSV export link; test on desktop and mobile widths.  
**Deliverables:** interface, screenshots, user guide and frontend walkthrough.  
**Must explain:** HTML structure, CSS responsiveness, JavaScript fetch, DOM updates, API calls and chart rendering.

## Member 5 — Analytics, QA and integration
**Owns:** analytics logic review, `tests/`, integration checklist and final demonstration.  
**Tasks:** verify frequency counts and percentages; test CRUD and error cases; run the full test suite; check clean installation; coordinate merge/integration; prepare demo dataset and final presentation.  
**Deliverables:** test report, bug log, demo script, final package and integration sign-off.  
**Must explain:** frequency distribution, Counter/hash map, expected O(n) analysis, test cases and system limitations.

## Shared integration rules
1. Keep filenames and API contracts unchanged unless all members agree.
2. Member 1 owns the exact output shape of `calculate_name_number`.
3. Member 2 owns the linked-list interface: `insert_end`, `search`, `update`, `delete`, `traverse`, `clear`.
4. Member 3 owns API/database integration and must call the agreed functions.
5. Member 4 must use API endpoints rather than duplicating calculation logic in JavaScript.
6. Member 5 runs all tests after every integration change.
7. Every member should be able to explain the overall architecture, not only their own file.

## Suggested 7-day schedule
| Day | Activity |
|---|---|
| 1 | Finalise scope, mapping, IKS framing and UI sketch |
| 2 | Numerology and linked-list modules |
| 3 | SQLite and Flask API |
| 4 | Frontend and chart integration |
| 5 | Frequency analysis, testing and bug fixes |
| 6 | Report, slides, screenshots and rehearsal |
| 7 | Clean installation rehearsal and final demonstration |
