import bs4, requests, re, sys

url = 'http://www.bom.gov.au/products/IDQ60901/IDQ60901.95551.shtml'

res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

currentTemp = soup.select('td[headers="t1-tmp"]')
temp = currentTemp
testHot = float(temp[0].text)
testCold = float(temp[0].text)

for list in temp:
    if float(list.text) > testHot:
        testHot = float(list.text)
    if float(list.text) < testCold:
        testCold = float(list.text)
        
print 'The maximum temp for today was ' + str(testHot)
print 'The minimum was ' + str(testCold)

for tempp in soup.findAll('table', {'class':'rowleftcolumn'} ):
    table = tempp.findAll('tr')
    print table