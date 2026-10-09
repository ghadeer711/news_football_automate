from urllib.parse import urlparse


def validate_news(news_list):
    if not news_list:
        raise ValueError("No news articles were extracted.")

    valid_news = []

    for news in news_list:
        title = news.get("title", "").strip()
        subtitle = news.get("subtitle", "").strip()
        link = news.get("link", "").strip()

        if not title:
            continue

        if not link:
            continue

        parsed_url = urlparse(link)

        if parsed_url.scheme not in ("http", "https"):
            continue

        if not parsed_url.netloc:
            continue

        valid_news.append({
            "title": title,
            "subtitle": subtitle,
            "link": link
        })

    if not valid_news:
        raise ValueError(
            "No valid news articles remained after validation."
        )

    return valid_news