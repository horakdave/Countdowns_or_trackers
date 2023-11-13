import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os

url = 'https://www.ssps.cz'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_articles = soup.find_all('div', class_='new')
    
    for article in news_articles:
        text_div = article.find('div', class_='text')
        if text_div:
            headline = text_div.find('h3')
            if headline:
                headline_text = headline.text
                tts = gTTS(text=headline_text, lang='cz')
                tts.save("headline.mp3")
                os.system("your_audio_player headline.mp3")
        else:
            print("Headline not found in this article.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
