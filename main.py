import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

link = 'https://www.amazon.com/dp/B00X9JNWGS/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0'

header = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36 '
}

response = requests.get(link,headers=header)

soup = BeautifulSoup(response.text,'lxml')

item = soup.select_one(selector=".a-price.a-text-price.a-size-medium.apexPriceToPay .a-offscreen")

price = float(item.getText().split("$")[1])


target_price = 550

if price < target_price :
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user="{mail id}",password="{password}")
        connection.sendmail(from_addr="{mail id}",to_addrs="{password}",
                            msg=f"subject:Price target achieved \n\n the price is currently at {price} quickly purchase it")
