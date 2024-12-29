from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import pandas as pd
import csv

# URL = 'https://www.amazon.in/PSYCHOLOGY-MONEY-DELUXE-Morgan-Housel/dp/9390166934/ref=sr_1_1_sspa?crid=25ADVGPJI7GNF&dib=eyJ2IjoiMSJ9.uZqkV-SGA5FtvD10k0V1-GR3Yrze5CGFFqGoPLKZsHvdyZIAM6KJvx_2I8jJDV6HZwkRO1H2Z46NdQyEnUOgIZoQQWobrEdNOOQj-IRGlmAgQuNsjGPUpMXe0XlQiQh5U-KjyBf1tIQkfc30ge25cxpnPZI_zaz_U3Lo4c2QVJYKrq6UCcgjpJPgRhi9bLGTcpYxMnvZKXPevliGueLfTLfloio332tcRVvOCGcyBKk.7iqLVy_0LIzKv1O2SZpyFp0xlB2AxZUjGTA5rEVy6SY&dib_tag=se&keywords=finance+books&qid=1735475769&sprefix=finance+books%2Caps%2C243&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

def check_price(URL,mailId,mailPass,toMailId,desiredPrice):
   
   # defining headers to avoid getting blocked by amazon
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.in/",
        "Connection": "keep-alive",
        "Host": "www.amazon.in",
        "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    title = soup2.find(id = 'productTitle').get_text().strip()
    price = soup2.find(class_='a-price-whole').get_text().strip()
    curr_time = get_current_time()

    csv_headers = ['Title','Price','Date']
    data = [title,price,curr_time]
    with open('amazon_wscrape_dataset.csv','w',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerow(data)

    if(desiredPrice == int(price)): #when desired price is detected, mail is sent to the respective mail ids given
        send_mail(mailId,mailPass,toMailId)
        
    # df = pd.read_csv('H:\\projects\\amazon_wscrape_dataset.csv')

def start_checking(Time):
    while(True):
        check_price()
        time.sleep(Time)

def send_mail(mailId,passKey,toMailId):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(mailId,passKey)
    subject = 'The product you want is available at the price you want!'
    body = 'Hey Budy, This is the moment we have been waiting. Go grab the product now!'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(toMailId,msg)

def get_current_time():
    """Returns the current time as a formatted string."""
    now = datetime.now()  # Get the current date and time
    current_time = now.strftime("%H:%M:%S")  # Format the time (HH:MM:SS)
    return current_time


