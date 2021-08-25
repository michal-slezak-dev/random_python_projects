import json
import requests
import os
import time
from pprint import pprint

#Info about my program
print("Autorem tego programu jest Michał Ślęzak. Pamiętaj, żeby zamiast przecinka (,) używać kropki(.) :-)")

#waits 5 sec and clears the prompt
time.sleep(5)
os.system("cls")

# join example C/EUR/2016-04-04/
# ask user about currency code and date
currency_code = input("Podaj walutę(EUR, USD, GBP itp.): ")
currency_date = input("Podaj datę(RRRR-MM-DD): ")

# JSON format instead of XML
params = {"format": "json"}

# join url
currency_url = currency_code + "/" + currency_date + "/"

# program makes a request
response = requests.get(
    "http://api.nbp.pl/api/exchangerates/rates/C/" + currency_url, params
)

# ask = sell bid = buy
try:
    content = response.json()
except json.decoder.JSONDecodeError:
    print("NIEPRAWIDŁOWY FORMAT!")
else:
    # content["rates"] --> ask, bid etc.
    # currencyFullName --> full name of chosen currency --> EUR - euro, USD - dolar amerykański
    currencyContent = content["rates"]
    currencyFullName = content["currency"]

    # converting values of chosen currency into string
    currencyAskString = str(currencyContent[0]["ask"])
    currencyBidString = str(currencyContent[0]["bid"])

    # converting values of chosen currency into float
    currencyAskFloat = float(currencyContent[0]["ask"])
    currencyBidFloat = float(currencyContent[0]["bid"])

    # It displays info about chosen currency (ask and bid)
    print("Kurs " + currencyFullName + " (sprzedaż) = " + currencyAskString)
    print("Kurs " + currencyFullName + " (kupno) = " + currencyBidString)

    # There is a menu inside the while loop, when user types something different than 'kupno' or 'sprzedaż'm the loop stops and the program ends
    while True:
        # ask whether user wants to buy or sell some currency
        choice = input("Chcesz kupić " + currencyFullName + "(kupno) czy sprzedać " + currencyFullName + "(sprzedaż) czy zakończyć(zakończ)" + ": ")

        # if our user wants to buy some currency, program asks about its amount and calculates the cost of purchase(in PLN)
        if choice.lower() == "kupno":
            amountOfMoney = float(input("Ile chcesz kupić: " + "(" + currencyFullName + "): "))
            purchaseCost = amountOfMoney * currencyBidFloat

            # displays the cost
            print("Koszt kupna " + str(amountOfMoney) + " " + currencyFullName + ": " + str(purchaseCost) + " zł.")

        # if our user wants to sell some currency, program asks about its amount and calculates the (profit) of sale(in PLN)
        elif choice.lower() == "sprzedaż":
            amountOfMoney = float(input("Ile chcesz sprzedać: " + "(" + currencyFullName + "): "))
            purchaseCost = amountOfMoney * currencyAskFloat

            # displays the profit
            print("Za sprzedaż " + str(amountOfMoney) + " " + currencyFullName + ": " + str(purchaseCost) + " zł.")
        else:
            break
