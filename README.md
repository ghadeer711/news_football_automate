Football News Scraper

A Python-based web scraping project that collects football news articles from "The Sun" (https://www.thesun.co.uk/sport/football/) and exports the extracted data to timestamped CSV files.

The project uses Selenium to interact with the website, validates the extracted information, and stores valid news articles in a structured format.

Features

- Automated Web Scraping: Extracts football news directly from The Sun website using Selenium WebDriver.
- Structured Data Extraction: Collects article titles, subtitles, and URLs.
- Data Validation: Checks extracted articles for required fields and valid URL structures.
- CSV Export: Saves validated news articles to CSV files using Pandas.
- Timestamped Output: Creates a separate output file for each run.
- Error Handling: Handles scraping failures and reports errors to the main application.
- Browser Cleanup: Uses "finally" to ensure the browser is closed after the scraping process.
- Organized Codebase: Separates scraping, validation, storage, and application orchestration into individual modules.

Technologies Used

Technology| Purpose
Python| Core programming language
Selenium| Browser automation and web scraping
Pandas| Data organization and CSV export
CSV| Output format

Project Structure

SVU/
├── main.py
├── scraper.py
├── validator.py
├── storage.py
├── requirements.txt
└── outputs/
    └── headline_YYYY-MM-DD_HH-MM.csv

Module Responsibilities

- "main.py" — Coordinates the scraping, validation, and storage workflow.
- "scraper.py" — Opens the website, extracts article information, and manages browser cleanup.
- "validator.py" — Validates extracted articles and excludes entries with missing required fields or invalid URL structures.
- "storage.py" — Converts validated data into a Pandas DataFrame and exports it to CSV.
- "requirements.txt" — Lists the Python dependencies required by the project.
- "outputs/" — Stores the generated CSV files.

Installation

1. Clone the Repository

git clone https://github.com/ghadeer711/news_football.git

Navigate to the project directory:

cd news_football/SVU

2. Create a Virtual Environment (Recommended)

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure ChromeDriver

The scraper uses a local ChromeDriver executable.

Update "CHROME_DRIVER_PATH" in "scraper.py" to match the location of ChromeDriver on your computer.

Make sure the installed ChromeDriver is compatible with your Chrome browser.

Usage

Run the application from the "SVU" directory:

python main.py

The application will:

1. Open the football news page.
2. Locate and extract available article information.
3. Validate the extracted data.
4. Save valid articles to a timestamped CSV file.
5. Display the execution result or an error message.

Generated files are saved in the "outputs/" directory.

Output Data

Each CSV file contains the following columns:

Column| Description
"title"| The article headline
"subtitle"| The article subtitle, if available
"link"| The article URL

Example:

title| subtitle| link
Example Football Headline| Example article subtitle| https://example.com/article

The example above is illustrative; actual results depend on the articles available on the website.

Error Handling and Data Validation

The project includes basic safeguards to improve reliability:

- Selenium WebDriver errors are reported as scraping failures.
- The browser is closed in a "finally" block after the scraping attempt.
- Articles without a title or usable HTTP/HTTPS URL are excluded.
- The application reports failures instead of displaying a successful result when an operation raises an exception.

The scraper relies on the website's current HTML structure. Changes to the page may require updates to its element selectors.

Limitations

- The scraper depends on the availability and structure of The Sun's football news page.
- The extracted fields may vary depending on the articles displayed.
- URL validation checks structure, not whether each destination is reachable.
- The project does not currently include scheduled execution, a database, or a persistent news history beyond the generated CSV files.

Future Improvements

Potential future enhancements include:

- Logging execution details to a log file.
- Adding automated tests for data validation.
- Improving resilience to changes in the website's HTML structure.
- Adding configurable output formats.
- Introducing retries for temporary website or browser failures.

Author

Ghadeer Alhiloney

---

This project was developed as a practical exercise in Python automation, web scraping, data validation, and file handling.
