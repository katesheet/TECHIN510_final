import os
from db import Database
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from db import Database
from paper import Paper

load_dotenv()


def get_data(db:Database):
    URL= 'https://arxiv.org/list/cs.CL/recent'
    res = requests.get(URL)
    if res.status_code != 200:
        return
    soup = BeautifulSoup(res.text, 'html.parser')
    paper_links = soup.select('dt')
    paper_infos = soup.select('dd')
    for paper_link, paper_info in zip(paper_links, paper_infos):
        herf = paper_link.select('a')[1].text.strip().strip('arXiv:')
        title = paper_info.select('div')[1].text.strip().strip('Title:').strip()
        paper = Paper(title, herf)
        db.insert_paper(paper)

with Database(os.getenv('DATABASE_URL')) as db:
    db.create_table()
    get_data(db)