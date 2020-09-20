import requests
from bs4 import BeautifulSoup


def search(term: str) -> dict:
    formatted_term = "".join("%20" if i == " " else i for i in term)
    url = f"https://www.ishtar-collective.net/search/{formatted_term}"

    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    results: BeautifulSoup = soup.find(class_="search-results")

    headings = results.find_all("h3")
    entry_lists = results.find_all("ul")

    data = {}

    for x, element in enumerate(headings):
        heading = element.find(class_="text").text
        entries = [[i.find("a").text, "https://www.ishtar-collective.net/"+i.find("a")["href"]] for i in entry_lists[x].find_all("li")]
        data[heading] = entries
    return data
