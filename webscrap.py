#!/usr/bin/env python3
from job_one import extract_whole_page as jobskorea ,final_page_num
from save import save_to_file

korea = jobskorea(final_page_num())

save_to_file(korea)




















# from bs4 import BeautifulSoups
# import requests
# print('content-type: text/html; charset=utf-8\n')


# jobs_pages = requests.get(
#     'https://www.jobkorea.co.kr/Search/?stext=%EA%B0%9C%EB%B0%9C%EC%9E%90&tabType=recruit&Page_No=1')
# jobs_soup = BeautifulSoup(jobs_pages.text, 'html.parser')

# pagination = jobs_soup.find('div', {'class': 'tplPagination newVer wide'})

# pages = pagination.find_all('a')

# list = []
# for page_number in pages[:-1]:
#     list.append(int(page_number.string))
# print(list)

# max_page = list[-1]
# for page_num_url in range(max_page):
#     print(f'Page_No={page_num_url+1}')



