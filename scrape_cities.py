from requests import get
from bs4 import BeautifulSoup
import bs4

def getCityNames():

    url = "https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Russia"

    response = get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup.prettify())

    tab = soup.find_all("table", class_="wikitable sortable")[0]

    names_n_links = [c.contents[0].decode() if type(c.contents[0])!=bs4.element.NavigableString else c.contents[0] for c in tab.find_all("td")]

    names = []

    for i in names_n_links:
        if "</a>" not in i and "\n" not in i:
            names.append(i)

    return names

