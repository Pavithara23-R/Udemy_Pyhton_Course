import requests
import smtplib
from bs4 import BeautifulSoup


YOUR_EMAIL = "pavithara8300@gmail.com"

YOUR_PASSWORD = #password is removed due to the security purpose

BUY_PRICE = 100
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"


header = {
    "User-Agent": "Chrome/84.0.4147.125",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user = YOUR_EMAIL, password = YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs="pavithara8300@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")

        )
        print("Email sent")
else:
    print("Price is still high")



