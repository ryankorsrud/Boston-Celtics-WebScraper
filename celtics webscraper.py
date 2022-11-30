# Author: Ryan Korsrud
# Version: November 29th, 2022
from bs4 import BeautifulSoup
import urllib.request
import csv

# writes data to a csv file
# args(2d list)
# returns(none)
def writeCSV(data):
    file = open('player stats.csv', 'w')
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
    file.close()

# gets html from website using BeautifulSoup
# args(none)
# returns(bs4.BeautifulSoup)
def getHTML():
    url = 'https://www.espn.com/nba/team/stats/_/name/bos'
    content = urllib.request.urlopen(url).read()
    return BeautifulSoup(content, 'lxml')

# gets data from a table on a website
# args(bs4.BeautifulSoup, int, int, int)
# returns(2d list)
def getTableData(html, i, firstRow, lastRow):
    data = []
    table = html.find_all('table')
    table_rows = table[i].find_all('tr')
    for tr in table_rows[firstRow:lastRow]:
        td = tr.find_all('td')
        if td != None:
            data.append([i.text for i in td])
    return data

# main program function
def start():
    html = getHTML()
    names = getTableData(html, 0, 1, -1)
    stats = getTableData(html, 1, 1, len(names)+1)

    #combines data from the stats table and names table
    for i in range(len(stats)):
        stats[i].insert(0, names[i][0])
    writeCSV(stats)
    
start()
