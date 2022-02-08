import bs4
import requests
import re,os

def remove_html_tags(text):
     
    
    pattern = r'"(.+?)"'
    m = re.search(pattern, text)
    m = m.group()
    
    string = re.sub('"', '', m)
    return string
def final_string():
    res = requests.get('https://simcoecountyschoolbus.ca/')
    type(res)
    res.raise_for_status()

    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    bob = noStarchSoup.select('#zone_icon_2')

    thing =  str(bob)
    cleaned_string =remove_html_tags(thing)

    c = cleaned_string[0:2] 

    if(c== "go"):
        print("Bus is going")
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'go.png')
        img = filename
    else:
        print("Bus is not going")
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'stop.png')
        img = filename
    return img
