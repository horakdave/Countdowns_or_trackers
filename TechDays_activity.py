import time
import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSd15j0zSDbtcyT5NKU_01N0J2IRYzzQECkHff2dFTrVkucyDw/closedform"
expected_text = "Formulář TechDays! 2023 již nepřijímá odpovědi."

while True:
    response = requests.get(url)
    
    if expected_text in response.content.decode("utf-8"):
        print(f"{time.ctime()}   tech days este nejsou")
    else:
        print(f"{time.ctime()}   tech days uz jsou")

    time.sleep(3600)