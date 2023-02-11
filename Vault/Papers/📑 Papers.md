```dataview
TABLE WITHOUT ID paper, author, year, contribution
FROM "Papers/Entries"
WHERE file.name != this.file.name
SORT year DESC
```