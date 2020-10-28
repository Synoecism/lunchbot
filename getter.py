
# coding=utf-8
import urllib
from bs4 import BeautifulSoup

def getText(dayOfWeek):

    request_url = urllib.urlopen('https://www.nyaetage.se/veckans-meny?')
    read_content = request_url.read()
    soup = BeautifulSoup(read_content, 'html.parser')

    td_all = soup.find_all('td')

    # table data is seperated by five
    converted_day_of_week = dayOfWeek * 5

    # add asterisk for formatting
    alltext = td_all[converted_day_of_week].text
    newtext = alltext[:0] + 'DAGENS LUNCH @ NYA ETAGE\n* ' + alltext[0:]
    newertext = newtext.replace("\n", "\n\n* ",)

    return newertext

def getDailyInWeek(day):

    request_url = urllib.urlopen('https://www.nyaetage.se/veckans-meny?')
    read_content = request_url.read()
    soup = BeautifulSoup(read_content, 'html.parser')

    td_all = soup.find_all('td')

    # table data is seperated by five
    converted_day_of_week = day * 5
    
    title_of_day = "Dagens"
    if day == 1:
        title_of_day = "MANDAGENS"
    if day == 2:
        title_of_day = "TISDAGENS"
    if day == 3:
        title_of_day = "ONSDAGENS"
    if day == 4:
        title_of_day = "TORSDAGENS"
    if day == 5:
        title_of_day = "FREDAGENS"
    
    # add asterisk for formatting
    alltext = td_all[converted_day_of_week].text
    newtext = alltext[:0] + title_of_day + ' LUNCH @ NYA ETAGE\n* ' + alltext[0:]
    newertext = newtext.replace("\n", "\n\n* ",)

    return newertext