import csv
import requests
from bs4 import BeautifulSoup

def main():
    suburb_urls = ['https://www.domain.com.au/sale/sydney-nsw-2000/',
                   'https://www.domain.com.au/sale/melbourne-vic-3000/']

    list_of_rows = []
    for suburb_url in suburb_urls:
        print("SCRAPING SUBURB {}".format(suburb_url.upper()))
        properties = get_property_urls(suburb_url)
        for property_url in properties:
            print("Scraping property {}".format(property_url.split('/')[3]))
            row = get_property_info(property_url)
            list_of_rows.append(row)
        print("")

    with open('./output/python_output.csv', 'w') as f:
        print("Writing files ...")
        writer = csv.writer(f)
        writer.writerow(['address', 'price', 'bed', 'bath', 'parking', 'property_type', 'internal_area', 'land_area', 'link'])
        writer.writerows(list_of_rows)

    print("Done!")

def get_property_urls(suburb_url):
    # get the html text of the url
    response = requests.get(suburb_url)
    html = response.content

    # BeautifulSoup() transforms HTML document into a complex tree of Python objects
    soup = BeautifulSoup(html, "lxml")

    # get URLs of individual properties
    listings = soup.select('.search-results__listing link')     # select() will not pick up any NoneType values, while find_all() will
    property_urls = [x.get('href') for x in listings]           # get() to get the value of an attribute
    return property_urls

def get_property_info(property_url):
    property_html = requests.get(property_url).content
    property_soup = BeautifulSoup(property_html, "lxml")

    address = property_soup.select_one('.listing-details__columns-container .listing-details__summary-left-column h1').string
    price = property_soup.select_one('.listing-details__columns-container .listing-details__summary-left-column div').string

    property_attr = property_soup.select(".listing-details__summary-right-column .property-feature__feature-text-container")
    [bed, bath, parking] = [x.get_text() for x in property_attr]
    bed = bed.split()[0]
    bath = bath.split()[0]
    parking = parking.split()[0]

    property_details = property_soup.select(".listing-details__key-features--item .listing-details__key-features--value")
    property_type, internal_area, land_area = [x.get_text() for x in property_details]

    row = [address, price, bed, bath, parking, property_type, internal_area, land_area, property_url]
    return row

if __name__ == "__main__":
    main()
