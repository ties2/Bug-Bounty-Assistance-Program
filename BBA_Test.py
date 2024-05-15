import requests
from bs4 import BeautifulSoup, Comment
import re

url = "https://www.shatel.ir"

def find_comments(url):
    # Fetch the HTML content of the web application
    response = requests.get(url)
    html_content = response.text

    # Find all single-line comments
    single_line_comments = re.findall(r'<!--.*?-->', html_content, re.DOTALL)
    print("Single-line comments:")
    for comment in single_line_comments:
        print(comment)

    # Find all multi-line comments
    multi_line_comments = re.findall(r'/\*(.*?)\*/', html_content, re.DOTALL)
    print("\nMulti-line comments:")
    for comment in multi_line_comments:
        print(comment)


find_comments(url)