# MINI PROJECT REPORT
## Numerology Intelligence System: Name Number Computation and Linked-List Analysis

**Subject:** Data Structures and Algorithms  
**Bloom's Taxonomy:** L4 — Analyse  
**Cognitive process:** Analyse  
**Knowledge context:** Indian Knowledge Systems (IKS) contextualisation  
**Team size:** Five members  
**Technology:** Python, Flask, SQLite, HTML, CSS, JavaScript

---

## Certificate / Declaration template
This is to certify that the mini project titled **“Numerology Intelligence System: Name Number Computation and Linked-List Analysis”** is a group project submitted in partial fulfilment of the requirements of the Data Structures and Algorithms course. The work has been carried out by the undersigned team members under the guidance of the course instructor.

Team members: [Add five names and roll numbers]  
Faculty guide: [Add faculty name]  
Department / Institution: [Add details]  
Academic session: [Add session]

## Acknowledgement
We express our sincere gratitude to our faculty guide and department for their guidance and support during the development of this mini project. We also thank our institution and classmates for their feedback. This project helped us understand the practical use of data structures, algorithms, database management and frontend-backend integration.

## Abstract
The Numerology Intelligence System is an interactive web application that calculates traditional Pythagorean name-number values and analyses the resulting dataset. Its primary DSA contribution is a custom singly linked list used to organise records and demonstrate insertion, traversal, searching, updating and deletion. SQLite provides persistent storage, while a Flask REST API connects the backend to a browser-based interface. A frequency-analysis module uses a hash-map-based counter to identify common values, repeated groups and distributions. The project is framed at Bloom's L4 (Analyse) level because users can examine how records are structured, compare frequency patterns, and interpret the behaviour and complexity of linked-list operations. Numerology is used only as an illustrative calculation domain and not as a scientifically validated prediction method.

## 1. Introduction
Data structures organise information so that operations can be performed systematically. A linked list is a linear data structure in which each node stores data and a reference to the next node. Unlike arrays, linked-list nodes do not require contiguous memory locations. This project applies a singly linked list to name-analysis records. Each record stores the submitted name, normalized name, arithmetic total, final numerology number and timestamp. The user can interact with the records through a web interface while the backend performs the actual data-structure operations.

## 2. Problem statement
A simple calculator can compute a name number but does not provide a structured way to maintain multiple results or analyse patterns across them. The proposed system combines calculation, linked-list record management, persistent storage and frequency analysis in one application. It enables users to create, search, update, delete, traverse and export records and to examine the distribution of computed values.

## 3. Objectives
1. Implement a consistent Pythagorean letter-to-number mapping.
2. Create a custom singly linked list for storing and managing records in memory.
3. Implement insertion, traversal, searching, updating and deletion.
4. Persist records in an SQLite database.
5. Analyse the frequency and distribution of final numbers.
6. Build a responsive browser interface connected to a Flask API.
7. Evaluate correctness, edge cases and algorithmic complexity.
8. Contextualise the example domain through a careful IKS discussion without making unsupported historical claims.

## 4. Scope and limitations
The application supports Latin alphabet names, spaces, punctuation and accented Latin character normalization. It does not claim to support every writing system or transliteration convention. The Pythagorean mapping is one selected modern numerology convention; other systems may use different mappings and reduction rules. Results depend on the selected convention. The system is an educational demonstration, not a tool for scientific assessment or personal decision-making.

## 5. IKS contextualisation
The project uses a contemporary name-number calculation convention as an illustrative point of comparison with broader Indian traditions of associating numbers, language, calendars and symbolic systems. Indian Knowledge Systems are diverse and historically varied; the Pythagorean mapping implemented here should not be represented as an ancient Indian method. The IKS component should therefore be handled as a critical comparative discussion: explain that number symbolism and traditional knowledge systems exist in multiple cultures, distinguish documented Indian traditions from the chosen algorithm, and avoid claiming that the application proves cultural or predictive validity. For a final submission, cite the course's prescribed IKS readings or instructor-approved sources.

## 6. System requirements
**Hardware:** Computer with a modern browser; 4 GB RAM recommended; internet access for Chart.js CDN (optional for the API itself).  
**Software:** Python 3.10+, Flask, SQLite (included with standard Python), modern browser, code editor.

## 7. Methodology and architecture
1. User enters a name in the frontend.
2. JavaScript sends a JSON request to Flask.
3. Flask validates and normalizes the name.
4. The numerology module maps letters and computes the total and reduced number.
5. SQLite saves the record and returns its unique ID and timestamp.
6. The record is inserted into the custom singly linked list.
7. The dashboard traverses the linked list and displays records.
8. The analytics endpoint traverses the list and uses a frequency counter to calculate the distribution.
9. The frontend renders the distribution as a chart and insight summaries.

**Architecture:** Browser UI → JavaScript fetch API → Flask routes → Numerology module / Singly linked list / SQLite database → JSON response → Dashboard.

## 8. Algorithms
### 8.1 Name number calculation
Input: name string.  
Output: normalized name, letter values, total, final number.  
Steps:
1. Normalize accented Latin characters and convert to uppercase.
2. Remove spaces and non-alphabetic characters.
3. Reject input if no alphabetic characters remain.
4. Map each letter to a value from 1 to 9.
5. Sum all values.
6. Repeatedly sum digits while the value is greater than 9, preserving 11, 22 and 33.
7. Return the calculation details.

### 8.2 Linked-list insertion
1. Create a node containing the new record.
2. If head is empty, set head to the new node.
3. Otherwise traverse until the node whose next pointer is NULL.
4. Set that node's next pointer to the new node.
5. Increase the list size.

### 8.3 Linked-list deletion
1. Set current to head and previous to NULL.
2. Traverse until the target ID is found or current becomes NULL.
3. If not found, return false.
4. If target is head, move head to head.next.
5. Otherwise set previous.next to current.next.
6. Decrease list size.

### 8.4 Frequency analysis
1. Traverse all linked-list nodes.
2. Read each node's final numerology number.
3. Increment that number's count in a hash map / Counter.
4. Calculate percentages using count divided by total records.
5. Identify the maximum-frequency value and repeated groups.

## 9. Data structure design
**Node:** `data` stores the record dictionary; `next` stores the reference to the next node.  
**Linked list:** `head` points to the first node; `_size` tracks the number of nodes.  
**Database:** SQLite stores records persistently. On application startup, the in-memory linked list is reconstructed from the database. SQLite is the persistent source of truth; the linked list is the DSA structure used by the application.

## 10. Complexity analysis
| Operation | Time | Reason |
|---|---:|---|
| Insert at end | O(n) | Traverse to final node |
| Search | O(n) | Sequential scan |
| Update | O(n) | Search then replace |
| Delete | O(n) | Locate node and relink pointers |
| Traverse | O(n) | Visit each node once |
| Frequency analysis | O(n) expected | One traversal with hash-map counting |
| Name calculation | O(m) | Process m letters, plus digit reductions |

Space complexity is O(n) for the linked list and O(k) additional space for frequency counting, where k is the number of distinct final values.

## 11. Testing and validation
The test suite checks known calculations, accented-name normalization, invalid input, master-number preservation, linked-list insertion/search/update/deletion/traversal, API CRUD operations, analytics and health checks. Manual browser testing should additionally confirm responsive layout, search filtering, CSV export, confirmation before deletion and visible error messages.

## 12. Results and discussion
The system demonstrates how a custom linked list can organise a changing collection of records and how a separate frequency-analysis step can reveal distributions in that collection. The dashboard makes the results observable. The implementation also illustrates a practical distinction between an in-memory data structure and persistent database storage. A linked list is not automatically faster than an array or database index for every operation; the chosen structure is valuable here because the project explicitly studies node-based operations and pointer updates.

## 13. Future enhancements
- Add a maintained tail pointer for O(1) tail insertion.
- Add a doubly linked list and compare operation trade-offs.
- Add sorting by name, total or final number.
- Add pagination for large datasets.
- Add user authentication and role-based access.
- Add downloadable PDF reports.
- Add alternate mapping schemes as configurable strategies.
- Add a comparative study of linked lists, arrays and hash tables.

## 14. Conclusion
The project integrates a traditional name-number calculation rule with practical DSA implementation. The custom singly linked list supports record insertion, searching, updating, deletion and traversal. Flask provides the service layer, SQLite provides persistence, and the frontend presents results and frequency patterns. The project meets the L4 Analyse focus by enabling learners to inspect distributions, compare records and evaluate algorithmic costs.

## References (complete with course-approved sources)
1. Course-prescribed Data Structures and Algorithms textbook/notes — add exact author, title, edition and year.
2. Python documentation: https://docs.python.org/3/
3. Flask documentation: https://flask.palletsprojects.com/
4. SQLite documentation: https://www.sqlite.org/docs.html
5. Chart.js documentation: https://www.chartjs.org/docs/
6. Institution/course-prescribed IKS reading list — add exact bibliographic details after consulting the faculty guide.
