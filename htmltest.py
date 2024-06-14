from requests_html import HTMLSession
session=HTMLSession()
url='http://xcmh.com/rexue/dianjuren'
response=session.get(url)
table=response.html.find('div.cy_plist')
for element in table:
    print(element.text)