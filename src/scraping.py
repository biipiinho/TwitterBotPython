import requests as req
import bs4 as bs4
import constants as cons


def create_url(tag:str) -> str:
    return f'https://www.goodreads.com/quotes/tag/{tag}'


def get_page(url:str) -> bs4.BeautifulSoup:
    page = req.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    return soup

# url =create_url("poetry")
# soup  = get_page(url)
#
# raw_quotes = soup.find_all(class_="quoteText")
#
# for quote in raw_quotes:
#     print(quote.contents[0].strip())
#
def extractor(quote):
    quote_text = quote.contents[0].strip()

    author = quote.find(class_="authorOrTitle").text.strip()

    return quote_text, author


def scrape_quotes():
    collection = list()
    for tag in cons.TAGS:
        url = create_url(tag)
        soup = get_page(url)
        raw_quotes = soup.find_all(class_="quoteText")
        for quote in raw_quotes:
            quote_text,  author = extractor(quote)
            data ={
                    "Quote": quote_text,
                    "Author": author
                    }
            collection.append(data)
    return collection





