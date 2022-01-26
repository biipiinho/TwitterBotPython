import json
import scraping

if __name__ == "__main__":
    quotes = scraping.scrape_quotes()
    with open("quotes.json", mode = "w") as quotes_file:
        json.dump(quotes, quotes_file, ensure_ascii=False)


