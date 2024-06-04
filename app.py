import os
from db import Database
import streamlit as st
from dotenv import load_dotenv
from db import Database
from paper import Paper
from openai_api import OpenAIChat

load_dotenv()

def display_papers(papers):
    container = st.container()
    bottom_menu = st.columns((4, 2, 1))
    with bottom_menu[2]:
        batch_size = st.selectbox("Page Size", options=[25, 50, 100])
    with bottom_menu[1]:
        total_pages = (
            int(len(papers) / batch_size) if int(len(papers) / batch_size) > 0 else 1
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")

    with container:
        papers = papers[batch_size * (current_page-1) : batch_size * current_page - 1]
        if not papers:
            return
        for paper in papers:
            p = Paper(title=paper[1], idx=paper[0])
            # print(paper)
            co = st.columns((3, 1))
            with co[0]:
                st.markdown(f'{p.title}')
            with co[1]:
                if st.button('Chat with this paper!', key=hash(p)):
                    st.session_state['page'] = 'Chat'
                    st.session_state['paper'] = p
                    st.session_state['chat'] = OpenAIChat()
                    # st.session_state['id'] = p.id
                    st.rerun()
                    # st.session_state['data'] = p.get_paper()
        
def main_page():
    st.title('Arxiv Computational Linguistics Paper')

    st.markdown('---')

    # Search, sort, and filter bar
    search_query = st.text_input("Search papers")
    sort_column = st.selectbox("Sort by", ["title", "created_at"], index=1)
    sort_order = st.selectbox("Order by", ["from high to low", "from low to high"], index=0)
    # papers = []
    with Database(os.getenv('DATABASE_URL')) as db:
        papers = db.query_table(search_query, sort_column, sort_order)
        display_papers(papers)

def chat_page():
    if st.button('Go back to Main Page'):
        st.session_state['page'] = 'Main'
        st.session_state['chat'] = None
        st.session_state['paper'] = None
        st.rerun()
    paper = st.session_state['paper']
    chat = st.session_state['chat']
    st.title(paper.title)
    if len(chat.messages) == 1:
        chat.get_response('summarize the paper 100 words: '+ paper.get_paper())
    idx = 0
    
    for res in chat.messages[2:]:
        st.markdown(f'{res["role"]}: {res["content"]}')
    prompt = st.chat_input("Have a chat with the paper!")
    if prompt:
        # st.write(f"User: {prompt}")
        chat.get_response(prompt)
        for res in chat.messages[2:]:
            st.markdown(f'{res["role"]}: {res["content"]}')
    


if 'page' not in st.session_state:
    st.session_state['page'] = 'Main'
if 'paper' not in st.session_state:
    st.session_state['paper'] = None
if 'chat' not in st.session_state:
    st.session_state['chat'] = None


if st.session_state['page'] == 'Main':
    main_page()
elif st.session_state['page'] == 'Chat':
    chat_page()