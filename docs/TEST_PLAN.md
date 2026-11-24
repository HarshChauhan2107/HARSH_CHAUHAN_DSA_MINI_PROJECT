# Test plan and acceptance checklist

## Automated tests
Run: `python -m unittest discover -s tests -v`

| ID | Test | Expected result |
|---|---|---|
| N01 | Calculate ADA | Total 6, final 6 |
| N02 | Calculate ADA LOVELACE | Total 36, final 9 |
| N03 | Calculate JOSÉ | Accent normalized; calculation succeeds |
| N04 | Input only digits/punctuation | Validation error |
| N05 | Reduce 22 | Master number 22 preserved |
| L01 | Insert into empty list | Head points to new node |
| L02 | Search existing ID | Matching node returned |
| L03 | Search missing ID | None returned |
| L04 | Delete head | Head moves to next node |
| L05 | Delete missing ID | False returned |
| L06 | Update existing node | Node data replaced |
| A01 | POST valid name | HTTP 201 and record created |
| A02 | POST invalid name | HTTP 400 |
| A03 | GET records | All records returned |
| A04 | PUT existing ID | Updated record returned |
| A05 | DELETE existing ID | Record removed |
| A06 | GET analytics | Counts and distribution returned |
| A07 | GET health | Healthy status returned |

## Manual browser acceptance
- [ ] Dashboard loads at `http://127.0.0.1:5000`.
- [ ] Valid name creates a result and a record.
- [ ] Result shows normalized letters, mapped values and total.
- [ ] Refreshing the page preserves saved records.
- [ ] Search filters the visible rows.
- [ ] Edit recalculates the selected record.
- [ ] Delete asks for confirmation and removes the record.
- [ ] Chart changes after records are added or deleted.
- [ ] CSV export downloads a readable file.
- [ ] Empty dataset displays a friendly state.
- [ ] Invalid input displays a useful error.
- [ ] Mobile-width layout remains usable.

## Acceptance criteria
The mini project is ready for demonstration when all automated tests pass, all manual browser checks are completed, five members can explain their modules, and a fresh setup works using only the README instructions.
