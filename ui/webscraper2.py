import requests
from bs4 import BeautifulSoup
import json

def google_search(search_term, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_term,
        "key": api_key,
        "cx": cse_id,
        "num": 1
    }
    response = requests.get(url, params=params)
    search_results = response.json()
    if 'items' in search_results:
        return search_results['items'][0]['link']
    else:
        raise ValueError("No search results found")

def scrape_webpage(url):
    data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in ['head', 'header', 'footer', 'nav', 'script']:
            for element in soup.find_all(tag):
                element.decompose()

        content_text = soup.get_text(" ", strip=True)

        data.append({"doc": content_text})

        return data
    else:
        raise ValueError(f"Error accessing url: {url}")


def search_and_scrape(search_term, api_key, cse_id):
    final_url = google_search(search_term, api_key, cse_id)
    scraped_data = scrape_webpage(final_url)

    with open(f"../data/data.jsonl", "w") as f:
        json.dump(scraped_data, f)
        f.write("\n")


    print(scraped_data)
    return scraped_data
    