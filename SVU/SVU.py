from scraper import scrape_news
from validator import validate_news
from storage import save_news


def main():
    try:
        news = scrape_news()

        valid_news = validate_news(news)

        file_path = save_news(valid_news)

        print(f"Successfully saved {len(valid_news)} news articles.")
        print(f"Output file: {file_path}")

    except Exception as error:
        print(f"Automation failed: {error}")


if __name__ == "__main__":
    main()