import requests
from bs4 import BeautifulSoup
import csv

url = '...'  

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

h2_elements = soup.find_all('h2', class_='subtitle-big faq__heading')
h3_elements = soup.find_all('h3', class_='subtitle')

with open('output1.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Heading Level', 'Text'])
    
    for h2 in h2_elements:
        writer.writerow(['h2', h2.get_text(strip=True)])
    
    for h3 in h3_elements:
        writer.writerow(['h3', h3.get_text(strip=True)])

print("save in log1.csv")
