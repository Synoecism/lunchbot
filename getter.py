
import urllib
from bs4 import BeautifulSoup

def getText(dayOfWeek):

    request_url = urllib.urlopen('https://www.nyaetage.se/veckans-meny?')
    read_content = request_url.read()
    soup = BeautifulSoup(read_content, 'html.parser')

    td_all = soup.find_all('td')
    print(len(td_all))
    print(td_all)

    # table data is seperated by five
    converted_day_of_week = dayOfWeek * 5

    # add asterisk for formatting
    alltext = td_all[converted_day_of_week].text
    newtext = alltext[:0] + 'DAGENS LUNCH @ NYA ETAGE\n* ' + alltext[0:]
    newertext = newtext.replace("\n", "\n\n* ",)

    return newertext
