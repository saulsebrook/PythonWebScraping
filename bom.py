import bs4, requests, re, sys

url = 'http://www.bom.gov.au/products/IDQ60901/IDQ60901.95551.shtml'

res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, features="html.parser")



#lineOfText = soup.find('tr', class_ ='rowleftcolumn')
#data = lineOfText.text
#print (data)
#mystring = data.replace('\n', ' ')
#print mystring


currentTemp = soup.select('td[headers="t1-tmp"]')
temp = currentTemp
testHot = float(temp[0].text)
testCold = float(temp[0].text)

#print temp[3].text

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



#print conversion
#rates = re.findall(r'\d+\.\d+', conversion)
#print rates

#print rate
