# Importing the required modules 
import os 
import sys 
import pandas as pd 
import urllib.request
from bs4 import BeautifulSoup 



urltable = [
    "https://www.medicineindia.org/medicine-brands/a",
    "https://www.medicineindia.org/medicine-brands/b",
    "https://www.medicineindia.org/medicine-brands/c",
    "https://www.medicineindia.org/medicine-brands/d",
    "https://www.medicineindia.org/medicine-brands/e",
    "https://www.medicineindia.org/medicine-brands/f",
    "https://www.medicineindia.org/medicine-brands/g",
    "https://www.medicineindia.org/medicine-brands/h",
    "https://www.medicineindia.org/medicine-brands/i",
    "https://www.medicineindia.org/medicine-brands/j",
    "https://www.medicineindia.org/medicine-brands/k",
    "https://www.medicineindia.org/medicine-brands/l",
    "https://www.medicineindia.org/medicine-brands/m",
    "https://www.medicineindia.org/medicine-brands/n",
    "https://www.medicineindia.org/medicine-brands/o",
    "https://www.medicineindia.org/medicine-brands/p",
    "https://www.medicineindia.org/medicine-brands/q",
    "https://www.medicineindia.org/medicine-brands/r",
    "https://www.medicineindia.org/medicine-brands/s",
    "https://www.medicineindia.org/medicine-brands/t",
    "https://www.medicineindia.org/medicine-brands/u",
    "https://www.medicineindia.org/medicine-brands/v",
    "https://www.medicineindia.org/medicine-brands/w",
    "https://www.medicineindia.org/medicine-brands/x",
    "https://www.medicineindia.org/medicine-brands/y",
    "https://www.medicineindia.org/medicine-brands/z"
]


list_header = [
    'Brand',
    'Company',
    'Package',
    'Strength',
    'Price'
] 



# empty list 
data = [] 

# for getting the header from 
# the HTML file 

for url in urltable:
    req =  urllib.request.Request(url, headers= {'User-Agent': 'Mozilla/5.0'} )
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html) 
    table = soup.find(lambda tag: tag.name=='table') 

    # header = table.find_all("tbody")[0].find("tr") 

    # for items in header: 
    # 	try: 
    # 		list_header.append(items.get_text()) 
    # 	except: 
    # 		continue


    # for getting the data 
    HTML_data = soup.find_all("tbody")[1].find_all("tr") 

    for element in HTML_data: 
        sub_data = [] 
        for sub_element in element: 
            try: 
                sub_data.append(sub_element.get_text()) 
            except: 
                continue
        data.append(sub_data) 
    print(url)        
    print(len(data))

# Storing the data into Pandas 
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header) 

# Converting Pandas DataFrame 
# into CSV file 
dataFrame.to_csv('meds.csv') 



