#!/usr/bin/env python
# coding: utf-8

# In[50]:


import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
import csv
import time


def clearsession():
    label['text'] = ''
    row = ''
    with open('/home/tunq/Desktop/pymi/git_pymi/Crawling/coin_info.csv', 'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            
def coin_list():
    result = []
    data_link = requests.get('https://coinmarketcap.com')
    data_crawl = BeautifulSoup(data_link.text, 'html.parser')
    for tr in data_crawl.tbody.find_all('tr'):
        td_symbol = tr.find('td', attrs= {'class':'no-wrap currency-name'}).get_text()
        td_price = tr.find('td', attrs= {'class': 'no-wrap text-right'}).get_text()
        name = tr.find('a', attrs= {'class': 'currency-name-container link-secondary'}).get_text()
        symbol = td_symbol.split('\n')[2]
        price = td_price.split('\n')[1]
        result.append([name, symbol, price])
    return result
            
def coin_check(coin_name):   
    #clear old data
    #crawl data 
    label['text'] = ''
    result = []
    data_link = requests.get('https://coinmarketcap.com')
    data_crawl = BeautifulSoup(data_link.text, 'html.parser')
    for tr in data_crawl.tbody.find_all('tr'):
        td_symbol = tr.find('td', attrs= {'class':'no-wrap currency-name'}).get_text()
        td_price = tr.find('td', attrs= {'class': 'no-wrap text-right'}).get_text()
        name = tr.find('a', attrs= {'class': 'currency-name-container link-secondary'}).get_text()
        symbol = td_symbol.split('\n')[2]
        price = td_price.split('\n')[1]
        result.append([name, symbol, price])  
    #get file csv
    for row in result:
        with open('/home/tunq/Desktop/pymi/git_pymi/Crawling/coin_info.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
    with open('/home/tunq/Desktop/pymi/git_pymi/Crawling/coin_info.csv') as csvFile:
        readCSV = csv.reader(csvFile)
        for row in readCSV:
            if coin_name.upper() in row or coin_name in row:
                label['text'] = ', '.join(row)
                
                
def curset(event):#check listcoin
    try:
        label['text'] = ''
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        coin_check(picked)
    except IndexError:
        pass
        
    
#format_giaodien (relx right to left, rely top to bottom) 
width = 600
height = 320
root = tk.Tk()
root.title("Search Coinmarketcap v1.0")
canvas = tk.Canvas(root, width = width, height = height, bg= '#1866F9', bd= 20)
canvas.pack()
lower_frame = tk.Frame(root, bg= '#FEFEFF', bd = 10)
lower_frame.place(relx=0.025 ,rely= 0.05 ,relwidth= 0.95 ,relheight= 0.85 )
#textbox
textbox = tk.Entry(lower_frame, font = 40)
textbox.place(relx = 0.005, rely= 0.03, relwidth = 0.7, relheight= 0.2)
#search_coin
search = tk.Button(lower_frame, text = 'Search', font = 40, command=lambda:coin_check(textbox.get()))
search.place(relx = 0.735, rely = 0.03, relwidth= 0.25, relheight= 0.2)
#resultbox
label = tk.Label(lower_frame, bg = '#07F92F')
label.place(relx = 0.005, rely= 0.3, relwidth = 0.7, relheight= 0.7)

#clearsession
clear_session = tk.Button(lower_frame, text = 'Refesh_Session', font = 40, command=lambda:clearsession())
clear_session.place(relx = 0.735, rely = 0.3, relwidth= 0.25, relheight= 0.2)
#config scrollbar
scrollbar = tk.Scrollbar(lower_frame)
scrollbar.pack(side =  'right', fill = 'y')
scrollbar.place(relx = 0.945, rely = 0.55, relheight= 0.45)
#config table data
my_list_coin = tk.Listbox(lower_frame, yscrollcommand = scrollbar.set)
my_list_coin.bind('<<ListboxSelect>>', curset)
data = coin_list()
list_coinname = []
for name_symbol in data:
    list_coinname.append(name_symbol[1])
for item in list_coinname:
    my_list_coin.insert('end', item)
my_list_coin.pack(side = 'left', fill = 'both')
my_list_coin.place(relx = 0.735, rely = 0.55, relwidth= 0.2, relheight= 0.45)
scrollbar.config( command = my_list_coin.yview )#connect data with scrollbar
root.mainloop()

#textbox.configure()
#dropdown_list
#var1 = tk.StringVar()
#var1.set(list_coinname[0])
#drop = tk.OptionMenu(lower_frame, var1, *list_coinname, command= coin_check(var1.get()))
#drop.grid()
#drop.place(relx = 0.735, rely = 0.6, relwidth= 0.2, relheight= 0.2)


              


# In[ ]:





# In[ ]:





# In[ ]:




