import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
res = requests.get("https://github.com/" + github_user)
res.raise_for_status()

soup = bs(res.text,'html.parser')
elems = soup.select("#js-pjax-container > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.flex-shrink-0.col-12.col-md-3.mb-4.mb-md-0 > div > div.js-profile-editable-replace > div.clearfix.d-flex.d-md-block.flex-items-center.mb-4.mb-md-0 > div.position-relative.d-inline-block.col-2.col-md-12.mr-3.mr-md-0.flex-shrink-0 > a > img")

print(elems[0]['src'])