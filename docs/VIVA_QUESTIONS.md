# Viva voce preparation

## Core DSA questions
1. **What is a linked list?** A linear data structure made of nodes, where each node stores data and a reference to the next node.
2. **What is a node?** The basic unit containing a record and a next pointer.
3. **What is the head?** A reference to the first node.
4. **What does NULL mean?** The next reference does not point to another node; it marks the end.
5. **Why use a linked list?** It demonstrates dynamic node allocation and pointer-based insertion/deletion. It is not necessarily faster than arrays for every task.
6. **What is traversal?** Visiting nodes sequentially from head until NULL.
7. **What is the complexity of search?** O(n) because nodes may need to be checked one by one.
8. **Why is insertion at the end O(n) here?** The implementation traverses from head to the final node. A tail pointer would make it O(1).
9. **What happens when deleting the head?** Head is reassigned to head.next.
10. **What happens when deleting a middle node?** The previous node's next pointer is set to the target node's next pointer.
11. **What is the difference between singly and doubly linked lists?** A singly list stores next; a doubly list stores both previous and next references.
12. **What is the space complexity?** O(n) for n nodes.

## Numerology and algorithm questions
13. **Which mapping is used?** Pythagorean mapping, cycling values 1–9 across letters.
14. **How is the final number calculated?** Sum letter values, then repeatedly sum digits until a single digit remains, preserving 11, 22 and 33.
15. **Why normalize names?** To handle case, accents, spaces and punctuation consistently.
16. **What is a master number in this implementation?** 11, 22 or 33, which this selected rule preserves during reduction.
17. **Is numerology scientifically proven?** No. The project uses it as an illustrative traditional calculation convention, not as a scientific prediction tool.

## Backend, database and frontend
18. **What is Flask?** A lightweight Python web framework used to define routes and return responses.
19. **What is an API?** An interface that lets the frontend request operations from the backend.
20. **What is REST?** A common style of web API design using HTTP methods and resource-oriented endpoints.
21. **Why SQLite?** It is lightweight, file-based and included with Python's standard library.
22. **Why use both linked list and SQLite?** SQLite provides persistence; the linked list is the in-memory DSA structure being studied.
23. **What is JSON?** A text-based data interchange format used between JavaScript and Flask.
24. **What does GET do?** Retrieves a resource.
25. **What does POST do?** Creates a resource.
26. **What does PUT do?** Updates/replaces a resource.
27. **What does DELETE do?** Removes a resource.
28. **What is input validation?** Checking input before processing to prevent invalid data and runtime errors.

## L4 Analyse questions
29. **How do you identify the most frequent number?** Traverse records and count each final number using a hash map/Counter, then find the maximum count.
30. **Why is frequency analysis O(n) expected?** Each record is visited once and hash-map increments are expected O(1).
31. **What trade-off does the linked list introduce?** Sequential access is O(n), and each node requires pointer storage.
32. **How would you improve insertion?** Maintain a tail reference so insertion at the end is O(1).
33. **How would you compare arrays and linked lists?** Compare access, insertion/deletion, memory overhead and cache locality using the same dataset.
34. **What does L4 Analyse mean in this project?** Students examine components, relationships, distributions, operation costs and trade-offs rather than only recalling or running code.
35. **How is IKS addressed responsibly?** By critically discussing cultural contexts of number symbolism while clearly identifying the algorithm as the selected Pythagorean convention and not mislabelling it as an ancient Indian algorithm.
