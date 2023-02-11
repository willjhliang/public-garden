# By Creation Date
```dataview
TABLE WITHOUT ID paper, author, year, contribution
FROM "Papers/Entries"
WHERE file.name != this.file.name
SORT file.ctime DESC
LIMIT 10
```
# By Modified Date
```dataview
TABLE WITHOUT ID paper, author, year, contribution
FROM "Papers/Entries"
WHERE file.name != this.file.name
SORT file.mtime DESC
LIMIT 10
```