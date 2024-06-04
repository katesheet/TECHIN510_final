import requests
from bs4 import BeautifulSoup
import re
base_link = 'https://arxiv.org/{type}/{id}'

class Paper:
    def __init__(self, title, idx) -> None:
        self.title = title
        self.id = idx
        self.paper = ''
        # self.paper = self.get_paper()

    def get_link(self, type='html'):
        return base_link.format(type=type, id=self.id)

    def get_paper(self):
        if self.paper:
            return self.paper
        html_link = self.get_link(type='html')
        res = requests.get(html_link)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            text = re.sub(r'\s+', ' ', soup.select('div.ltx_page_content')[0].text).strip()
            # print(text)
            self.paper = text
            return text
        else:
            return self.get_link()
        
    def __eq__(self, other):
        if isinstance(other, Paper):
            return self.title == other.title and self.id == other.id
        return False

    def __hash__(self):
        return hash((self.title, self.id))

