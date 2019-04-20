#!/usr/bin/env python
from __future__ import print_function
from collections import OrderedDict
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
details = soup.select('tr', class_ ='rowleftcolumn')[3:4]

amendDetails = []

for x in details:
    amendDetails.append(x.text.split('\n'))

    
    
flat_list = [item for sublist in amendDetails for item in sublist] # Flattening a list of lists
flat_list.pop(0)
string2 = ' '.join(flat_list)    
newString = ''
for i in amendDetails:
    newString += ', '.join(i)
    newString += '\n'
    #print(i)
#', '.join(amendDetails)
#print(newString)
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
print('\n\n')
print('\n\n')       
print(('The maximum temp for today was ' + str(testHot)).center(40 + 10, '-'))
print('\n')
print(('The minimum was ' + str(testCold)).center(40 + 10, '-'))
print('\n\n')

#print(string2)

listofNames = ['Date/Time', 'Temp', 'App Temp', 'Dew Point', 'Rel Humidity', 'Delta-T', 'Wind Direction', 'Speed', 'Gust', 'Speed KTS', 'Gust KTS', 'Press QNH', 'Press MSL', 'Rain since 9am']

#for i in range(len(listofNames)):
#    weatherDict[listofNames[i]] = flat_list[i]
#zipbObj = zip(listofNames, flat_list)
#weatherDict = dict(zipbObj)
#for key in listofNames:
 #   weatherDict[key] = weatherDict.pop(key)

weatherDict = zip(listofNames, flat_list)   
weatherDict = OrderedDict(weatherDict)
    
    
print('Weather Data'.center(40 + 10, '-'))
for k, v in weatherDict.items():
    print(k.ljust(40, '.') + str(v).rjust(10))

print('\n\n')
print('\n\n')


#print conversion
#rates = re.findall(r'\d+\.\d+', conversion)
#print rates

#print rate
