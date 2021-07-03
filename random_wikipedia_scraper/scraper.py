import requests, bs4, pyperclip

response = requests.get('pyperclip.paste()')
soup = bs4.BeautifulSoup(response.text,'html.parser')
title = soup.find(id='firstHeading').get_text()
content = soup.find(id='mw-content-text')

file = open(f'scraped/{title}.txt','w')
file.write(f'{title}\n')

file.write(content.get_text())
file.close()