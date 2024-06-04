# Arxiv Paper Chatbot and Scraper

## Summary
The Arxiv Paper Chatbot and Scraper is a web application designed to display all recent Arxiv NLP papers, with chatbot connect to every paper. 

## Technologies Used
- **Web Scraping**: To gather the latest papers from Arxiv.
- **Frontend Development**: For building a user-friendly interface using streamlit.
- **Databases**: Postgres database to store and manage paper data.
- **OpenAI API**: To implement the chatbot feature for interacting with paper content.

## What problems we are addressing

We believe our app can help two kinds of users. 

- **Researcher in ML**: As a researcher in machine learning, I want to quickly check and filter new paper updates from my fields of interest, so I can stay up-to-date with the latest developments.
- **Academic Paper Enthusiast**: As a person interested in reading frontier academic papers, I want to quickly access paper content and chat with the paper to understand it better.



## How to run
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/MatthewYZhang/TECHIN510_final
    ```
2. Navigate to the project directory:
    ```sh
    cd TECHIN510_final
    ```
3. Install dependencies for the backend:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Start the application:
    ```sh
    streamlit run app.py
    ```

2. Visit deployment page: https://techin510final.streamlit.app/

## Reflections

### What I learned
1. Object oriented programming
2. Use of databases
3. Web scraping

### What questions did I face
1. Unstable connection
2. difficulty in web scraping

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- [Arxiv](https://arxiv.org/) for providing access to a wealth of academic papers.
- [OpenAI](https://www.openai.com/) for the API to create the chatbot.
