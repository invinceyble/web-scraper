library(rvest)

# store web urls in a list
suburb_urls = c('https://www.domain.com.au/sale/sydney-nsw-2000/',
                   'https://www.domain.com.au/sale/melbourne-vic-3000/')

vectors <- list()
i = 1

get_info <- function(url_to_scrape) {

  # for each property, get deets
  property_html <- read_html(url_to_scrape)
  property <- html_nodes(property_html, ".listing-details__columns-container")
  address <- html_nodes(property, ".listing-details__summary-left-column h1") %>% html_text()
  price <- html_nodes(property, ".listing-details__summary-left-column div") %>% html_text()

  # get bed, bath and parking
  prop_attr <- html_nodes(property, ".listing-details__summary-right-column .property-feature__feature-text-container") %>% html_text()
  bed <- unlist(strsplit(prop_attr[1], ' '))[1]
  bath <- unlist(strsplit(prop_attr[2], ' '))[1]
  parking <- unlist(strsplit(prop_attr[3], ' '))[1]

  # get property type, internal area, land area
  deets <- html_nodes(property, ".listing-details__key-features--item .listing-details__key-features--value") %>% html_text()
  type <- deets[1]
  internal_area <- deets[2]
  land_area <- deets[3]

  row <- c(address, price, bed, bath, parking, type, internal_area, land_area, url_to_scrape)
  row
}


for (suburb_url in suburb_urls) {
  # scrape the website for the links to individual properties
  suburb <- read_html(suburb_url)
  properties <- html_nodes(suburb, ".search-results__listing link") %>% html_attr("href")

  for(property_url in properties) {
    vectors[[i]] <- get_info(property_url)
    i = i + 1
  }
}

resultMatrix <- do.call(rbind, vectors)
colnames(resultMatrix) <- c("address", "price", "bed", "baths", "parking", "prop_type", "internal_area", "land_area", "link")
write.table(resultMatrix, file = "R_output.csv", sep = ",", col.names = NA)
