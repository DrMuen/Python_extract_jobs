#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

print('content-type: text/html; charset=utf-8\n')

url = 'https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_popular&searchword=%EA%B0%9C%EB%B0%9C%EC%9E%90&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting='
f_url_one = 'https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_popular&searchword=%EA%B0%9C%EB%B0%9C%EC%9E%90&recruitPage='
f_url_two = "&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting="
def extract_saram_number():
    pages = requests.get(url)
    soup = BeautifulSoup(pages.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'}).find_all('a')
    return int(pagination[-2].text)

def extract_form(css):
    title = css.find('a', {'class': 'data_layer'})
    location = css.find('div', {'class': 'job_condition'})
    company = css.find('a', {'class': 'track_event data_layer'}).string
    return {
        'company': company,
        'title': title.text,
        'location': location.text,
        'link': f"https://www.saramin.co.kr{title['href']}"
    }

def extract_saram_pages(last_page):
    list = []
    for page in range(last_page):
        # print(f'이건페이지{page+1}\n{f_url_one}{page+1}{f_url_two}')
        html = requests.get(f'{f_url_one}{page+1}{f_url_two}')
        soup = BeautifulSoup(html.text,'html.parser')
        all_inf = soup.find_all('div', {'class': 'item_recruit'})
        for a in all_inf:
            yeah = extract_form(a)
            list.append(yeah)
        
    return list
        
def all():
    job_pages = extract_saram_number()
    job = extract_saram_pages(job_pages)
    return job



        
    


