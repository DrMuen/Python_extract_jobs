#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
print('content-type: text/html; charset=utf-8\n')

url = "https://www.jobkorea.co.kr/Search/?stext=%EA%B0%9C%EB%B0%9C%EC%9E%90&tabType=recruit&Page_No=1"
another_url = "https://www.jobkorea.co.kr/Search/?stext=%EA%B0%9C%EB%B0%9C%EC%9E%90&tabType=recruit&Page_No="
whole = requests.get(url)
soup = BeautifulSoup(whole.text, 'html.parser')

def final_page_num():
    pagination = soup.find('div', {'class':'tplPagination newVer wide'})
    num = pagination.find_all('li')
    return int(num[-1].text)

def make_dic(css):
    company = css.find('a', {'class': 'name dev_view'})
    location = css.find('span', {'class': 'loc long'})
    title = css.find('a', {'class', 'title dev_view'})
    link = title
    if company and location and title is not None:
        return {
            'company': company['title'],
            'title': title['title'],
            'location': location.string,
            'link': f"https://www.jobkorea.co.kr/{link['href']}"
        }

def extract_whole_page(pages):
    list = []
    for page in range(pages):
        html = requests.get(f"{another_url}{page+1}")
        source = BeautifulSoup(html.text,'html.parser')
        Whole_division = source.find_all('li', {'class': 'list-post'})
        for division in Whole_division:
            list.append(make_dic(division))
    return list
            








