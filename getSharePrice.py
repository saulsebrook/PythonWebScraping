#!/usr/bin/env python
import bs4, requests, re, sys

url = 'https://markets.businessinsider.com/stocks/airbus-stock?op=1'
url1 = 'https://www.x-rates.com/calculator/?from=EUR&to=AUD&amount=1'

res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
res.raise_for_status()

res1 = requests.get(url1, headers = {'User-agent': 'your bot 0.1'})
res1.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

soup1 = bs4.BeautifulSoup(res1.text, features="html.parser")


spans = soup.find('span', class_ ='push-data aktien-big-font text-nowrap')
price = spans.text
print '\n\n\nAirbus share price is ' + price + 'EUR'

euro = soup1.find('span', class_ ='ccOutputRslt')
conversion = euro.text
#print conversion
rates = re.findall(r'\d+\.\d+', conversion)
#print rates
rate = rates[0]
#print rate
totalPrice = float(rate) * float(price)
audTotal = float(totalPrice) * 22
formataudTotal = float("{0:.2f}".format(audTotal))
print 'Current price in AUD is $' + str(totalPrice)
print
print 'For a total of 22 shares, total value is $' + str(formataudTotal) + '\n\n'
