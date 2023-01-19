from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
link = "https://kubernetes.io/docs/concepts/services-networking/service/"

req = Request(
    url=link,
    headers={'User-Agent': 'Mozilla/5.0'}
)
html = urlopen(req)
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
f = open('./output.txt', 'w+')
for title in titles:
    try:
        content = re.search(">\\s*\\n*\\s*.+\\s*\\n*\\s*<",str(title))
        heading = re.search("<..",str(title)).group()[1:]
        spacing = ""
        match heading:
            case "h1": spacing = "\n"
            case "h2": spacing = "\n  "
            case "h3": spacing = "      "
            case "h4": spacing = "           "
            case "h5": spacing = "                "
            case "h6": spacing = "                      "
        f.writelines(spacing + (content.group()[1:-1]).strip() + "\n")
    except:
            f.write("Error: Need debugging" + "\n")
f.close()