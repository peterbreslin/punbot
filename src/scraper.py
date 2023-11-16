"""
Scrapes puns from https://onelinefun.com/puns/ (website with many, many puns).
 - Note that the selector is based on the HTML structure of this particular website.
 - Output saves the collectd puns into a text file.
"""

import requests
from bs4 import BeautifulSoup

def get_puns(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    puns = []
    elements = soup.find_all('div', class_='o')
    for elem in elements:
        pun = elem.find('p').text.strip()
        puns.append(pun)
    return puns

def save_to_file(puns, filename='puns.txt'):
    with open(filename, 'a', encoding='utf-8') as file:
        for pun in puns:
            file.write(f"{pun}\n")

def main():
    url = 'https://onelinefun.com/puns/'
    total_pages = 101 
    for page in range(1, total_pages + 1):
        url = f"{url}?page={page}"
        puns = get_puns(url)
        save_to_file(puns)
        print(f"Scraped and recorded puns from {url}")

if __name__ == "__main__":
    main()