# web-scraper

Practising web scraping in:
- Python: Using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- R: Using rvest

Projects:
1. Practice tutorial in Python
2. Scraping properties

Basic HTML/ CSS Notes:
- `<div>` is a tag called div
- .class-name
- #id-name

### BeautifulSoup
Below are the condensed notes from the official documentation for my understanding.
##### Objects
`BeautifulSoup()` represents the whole document as a whole.
- `soup = BeautifulSoup(html_file)` transforms HTML document into a complex tree of Python objects

`Tag()`

`NavigableString()` is the bit of text within a tag

##### Searching
- `class` is a reserved word in Python, so you can use `find_all()` with the keyword `class_`.
    - e.g. `soup.find_all(class_='search-results__listing')`
