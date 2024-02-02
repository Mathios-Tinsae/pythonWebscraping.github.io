from bs4 import BeautifulSoup
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = "6823763803:AAHEDfTsZ6bHoczI4X08DgGY1aJ8JV8bN2U"
chat_id = "674315603"

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

response = requests.get('https://ebstv.tv/category/news/')
soup = BeautifulSoup(response.text, 'lxml')

titles = soup.find_all('h2', class_='cm-entry-title')
descriptions = soup.find_all('div', class_='cm-entry-summary')
links = soup.find_all('a', class_='cm-entry-button')
author=soup.find_all('a', class_='url fn n')
date=soup.find_all('time', class_='entry-date published updated')

for title, description, link, writer, date in zip(titles, descriptions, links, author, date):
    title_text = title.text.strip()
    description_text = description.text.strip()
    link_href = link['href']
    writer_text = writer.text.strip()
    date_text = date.text.strip()

    if title_text:
        print("Title:", title_text)
        print(f'written by : {writer_text} on {date_text}')
        print("Description:", description_text)
        print("Link:", link_href)

        message = f"Title: {title_text}\nWritten by: {writer_text} on {date_text}\nDescription: {description_text}\nLink: {link_href}"
        send_to_telegram(bot_token, chat_id, message)
    else:
        print(f'written by : {writer_text} on {date_text}')
        print("Description:", description_text)
        print("Link:", link_href)
        
        message = f"Written by: {writer_text} on {date_text}\nDescription: {description_text}\nLink: {link_href}"
        send_to_telegram(bot_token, chat_id, message)
    

