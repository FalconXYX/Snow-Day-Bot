import bs4
import requests
import re
res = requests.get('https://simcoecountyschoolbus.ca/')

def remove_html_tags():
    type(res)
    res.raise_for_status()

    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    bob = noStarchSoup.select('#zone_status_2')

    text =  str(bob)
    clean = re.compile('<.*?>')
    temp = str(re.sub(clean, '', text))
    
    string = temp.replace("[", "")
    string = string.replace(" ]", "")
    return(string)



