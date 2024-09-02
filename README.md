# BookScraper

## Overview
BookScraper is a Python-based web scraping tool designed to extract comprehensive details about books from the "Books to Scrape" website. This project leverages the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing to collect and organize book information efficiently.

## Features
- **Scrapes Book Catalogs:** Extracts book titles, prices, ratings, availability, images, and descriptions.
- **Handles Pagination:** Automatically traverses through multiple pages of the catalog.
- **Collects Detailed Information:** Gathers data from both the catalog and individual book pages.

## Requirements
- Python 3.x
- Requests
- BeautifulSoup4

## Code Overview

- **`scrape_books(html_soup)`**: Extracts book links from catalog pages and adds them to the `books` set.
- **`scrape_book(html_soup)`**: Extracts details from individual book pages and appends them to the `book_info` list.
- **`main`**: Manages user input, handles pagination, and calls the scraping functions.

## Example

After running the script and following the prompts, the program will output detailed information for each book, including:

- **Title:** The book's title.
- **Price:** The book's price.
- **Rating:** The book's rating.
- **Availability:** The book's stock status.
- **Image URL:** The URL of the book's cover image.
- **Description:** A brief description of the book.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull r
