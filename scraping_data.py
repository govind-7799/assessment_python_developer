import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/"


response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")

    headings = []
    sub_headings = []
    code_blocks = []


    for heading in soup.find_all(["h2"]):
        headings.append(heading.text.strip())

    for sub_heading in soup.find_all("h4"):
        sub_headings.append(sub_heading.text.strip())

    for code_block in soup.find_all('div', class_='tab-content docutils container'):
        code_blocks.append(code_block.text.strip())
        print(code_block)
  
    max_length = max(len(headings), len(sub_headings), len(code_blocks))
    headings += [''] * (max_length - len(headings))
    sub_headings += [''] * (max_length - len(sub_headings))
    code_blocks += [''] * (max_length - len(code_blocks))

    data = pd.DataFrame({"Headings": headings, "Sub-Headings": sub_headings, "Code": code_blocks})

    data.to_csv("scraped_data.csv", index=False)
    print("Data has been scraped and saved to 'scraped_data.csv'.")

else:
    print("Error: Failed to download the webpage")
