# Property Scraper
These scripts will scrape the given URLs on domain.com.au for property information.

Both versions do the same thing.

### How to Deploy (Python)
```
git clone git@github.com:invinceyble/web-scraper.git
cd properties
python property_scraper.py
```

### Limitations / Possible Future Work
- Generate  `suburb_urls` by entering search criteria in the form
- Currently only takes the first page of the links - change this so it iterates through all pages
- Prices of properties aren't necessarily ints or floats - somehow parse these so they are and exclude auctions, etc.
