import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = 'http://books.toscrape.com/'
books = set()
book_info = []

def scrape_books(html_soup):
    for i in html_soup.find_all('article', class_='product_pod'):
        book_link = i.find('h3').find('a').get('href')
        books.add(urljoin(base_url, book_link))

def scrape_book(html_soup):
    book_img = html_soup.find('div', class_='thumbnail')
    book_img = book_img.find('img').get('src') if book_img else "No image available"
    
    book_title = html_soup.find('h1').get_text(strip=True) if html_soup.find('h1') else "No title available"
    
    book_price = html_soup.find('p', class_='price_color')
    book_price = book_price.get_text(strip=True) if book_price else "No price available"
    
    book_availability = html_soup.find('p', class_='instock availability')
    book_availability = book_availability.get_text(strip=True).strip() if book_availability else "No availability information"
    
    book_rating = html_soup.find('p', class_='star-rating')
    book_rating = ' '.join(book_rating.get('class')).replace('star-rating', '').strip() if book_rating else "No rating available"
    
    book_des = html_soup.find('div', id='product_description')
    book_des = book_des.find_next_sibling('p').get_text(strip=True) if book_des else "No description available."
    
    book_info.append({
        'Img': book_img,
        'Title': book_title,
        'Price': book_price,
        'Rating': book_rating,
        'Availability': book_availability,
        'Description': book_des
    })

inp = input('Enter the value based on whether you want to re-scrape the catalogue(y/n): ')

url = base_url
if inp.lower() == 'y':
    while True:
        print("Scraping the books available in the following page: ", url)
        r = requests.get(url)
        html_soup = BeautifulSoup(r.text, 'html.parser')
        scrape_books(html_soup)
        next_page = html_soup.select_one('li.next > a')
        if not next_page:
            break
        url = urljoin(base_url, next_page.get('href'))

for book in books:
    print("Scraping the following book in the list: ", book)
    r = requests.get(book)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    scrape_book(html_soup)

# Print the scraped book information
for info in book_info:
    print(info)
