import requests
from bs4 import BeautifulSoup

url = "https://www.chuncheon.go.kr/cityhall/citizen-participation/participation-forum/free/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for post in soup.find_all('div', class_='post'):
    number = post.find('span', class_='number').text.strip()
    title = post.find('a', class_='title').text.strip()
    author = post.find('span', class_='author').text.strip()
    date = post.find('span', class_='date').text.strip()
    url = "https://www.chuncheon.go.kr" + post.find('a', class_='title')['href']
    print(f"번호: {number}, 제목: {title}, 작성자: {author}, 작성일: {date}, URL: {url}")
