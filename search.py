import requests
from bs4 import BeautifulSoup

def scrape_google(query: str) -> str:
    api_key = "456135c8e9019893e97dc9b8216fed6617035c420f3139c50d24086cd0db146b"
    url = "https://serpapi.com/search"
    
    params = {
        "q": query,
        "api_key": api_key,
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        
        organic_results = search_results.get("organic_results", [])
        """
        for result in organic_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}\n")
        """
        result = organic_results[0]
        url = result['link']
    else:
        print(f"Error: {response.status_code}, {response.text}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = "\n".join([para.get_text() for para in paragraphs])
    return content
