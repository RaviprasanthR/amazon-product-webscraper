# Amazon Price Tracker

This project is a Python-based Amazon price tracker that scrapes product details, such as title and price, from a specified Amazon product page. When the desired price is reached, the script sends an email notification.

---

## Features
- **Scrape Product Details**: Extracts the product title and current price from an Amazon product page.
- **Price Monitoring**: Continuously checks for price updates at regular intervals.
- **Email Alerts**: Sends an email when the product price matches the desired price.
- **Data Logging**: Saves scraped data (title, price, timestamp) into a CSV file.

---

## Requirements
- Python 3.6 or higher
- Required libraries:
  - `beautifulsoup4`
  - `requests`
  - `pandas`
  - `smtplib`

Install the required libraries using:
```bash
pip install beautifulsoup4 requests pandas
```

---

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. Edit the script:
   - Replace the `URL` variable with the link to the desired Amazon product.
   - Provide your Gmail credentials (`mailId` and `mailPass`) and the recipient email address (`toMailId`).
   - Set the desired price threshold.

---

## Usage
Run the script to monitor prices and send email alerts:
```bash
python scrape_amazon.py
```

---

## Function Details

### `check_price(URL, mailId, mailPass, toMailId, desiredPrice)`
- Scrapes the product title and price from the given Amazon URL.
- Logs the data into a CSV file.
- Sends an email if the desired price is met.

### `start_checking(Time)`
- Runs the `check_price()` function in an infinite loop.
- Checks the price at intervals specified by the `Time` parameter (in seconds).

### `send_mail(mailId, passKey, toMailId)`
- Sends an email notification using Gmail's SMTP server.

### `get_current_time()`
- Returns the current time as a formatted string.

---

## Example
Set the desired product URL and price, then run the script:
```python
URL = 'https://www.amazon.in/product-link'
desiredPrice = 500  # Desired price for the product
check_price(URL, 'your_email@gmail.com', 'your_password', 'recipient_email@gmail.com', desiredPrice)
```

---

## Limitations
- The script is specific to Amazon's India domain (`amazon.in`).
- Requires proper headers to avoid being blocked by Amazon.
- Gmail credentials must have "Allow less secure apps" enabled.

---

## Disclaimer
This script is intended for educational purposes only. Use responsibly and ensure compliance with Amazon's terms of service.

---
