from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
html = urlopen('https://kubernetes.io/docs/concepts/services-networking/service/')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])

f = open('output.txt', 'w+')
for title in titles:
    content = re.search(">.+<",str(title))
    heading = re.search("<..",str(title)).group()[1:]
    spacing = ""
    match heading:
        case "h1": spacing = "\n"
        case "h2": spacing = "\n  "
        case "h3": spacing = "     "
        case "h4": spacing = "         "
    f.writelines(spacing + str(content.group()[1:-1]) + "\n")
