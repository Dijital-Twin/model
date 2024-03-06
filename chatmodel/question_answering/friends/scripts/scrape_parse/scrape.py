import requests
from bs4 import BeautifulSoup

url = "https://www.friends-tv.org/epshort.html#101"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

count = 0
with open('all_episodes.txt', 'w', encoding='utf-8') as file:
    for dl in soup.find_all('dl'):
        dts = dl.find_all('dt')
        dds = dl.find_all('dd')
        
        for dt, dd in zip(dts, dds):
            title = dt.find('h3').text if dt.find('h3') else 'No Title'
            description = dd.text.strip()
            file.write(f"{title}\n{description}\n\n")

print("İşlem tamamlandı, 'episodes.txt' dosyasına kaydedildi.")
