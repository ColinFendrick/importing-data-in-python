import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage to the shell
print(soup.title)

# Print Guido's text to the shell
print(soup.get_text())
