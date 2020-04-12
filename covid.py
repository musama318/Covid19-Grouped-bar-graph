import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
import locale

barWidth = 0.25

def getData(country):
	locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
	url = 'https://www.worldometers.info/coronavirus/country/'+country
	r = requests.get(url)
	s = BeautifulSoup(r.text,'html.parser')
	data = s.find_all("div",class_="maincounter-number")
	casedata = [locale.atoi(data[i].text.strip()) for i in range(len(data))]
	casedata.append(casedata[0]-casedata[1]-casedata[2]) # appending for active Cases
	return casedata


 
bars1=getData('china') #china
bars2=getData('italy') #italy
bars3=getData('us')   #USA
bars4=getData('india')  #India

print("""\
██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    ██████╗ ██╗   ██╗    ██╗   ██╗███████╗ █████╗ ███╗   ███╗ █████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗╚██╗ ██╔╝    ██║   ██║██╔════╝██╔══██╗████╗ ████║██╔══██╗
██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║    ██████╔╝ ╚████╔╝     ██║   ██║███████╗███████║██╔████╔██║███████║
██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    ██╔══██╗  ╚██╔╝      ██║   ██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║
██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    ██████╔╝   ██║       ╚██████╔╝███████║██║  ██║██║ ╚═╝ ██║██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝    ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
""")
r1 = np.arange(0,len(bars1)*2,2)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='CHINA')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='ITALY')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='USA')
plt.bar(r4, bars4, color='#ffa500', width=barWidth, edgecolor='white', label='INDIA')

plt.yscale('log')
 
plt.ylabel('Cases', fontweight='bold')
plt.xticks([(r + barWidth)*2 for r in range(len(bars1))], ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases'])
plt.title('COVID-19 live Data')

#Annotating every bar with its value
def annotate(r,b):
	for x,y in zip(r,b):

   		 label = "{}".format(y)

   		 plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,3), # distance from text to points (x,y)
                 ha='center')
annotate(r1,bars1)
annotate(r2,bars2)
annotate(r3,bars3)
annotate(r4,bars4)
 
plt.legend()
plt.show()
                
