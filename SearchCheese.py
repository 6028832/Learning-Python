import sys
import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.cheese.com/alphabetical?per_page=100"

def search_term():
    if len(sys.argv) > 1:
        second_command = sys.argv[1]
        print("The search term: " + second_command)
        return second_command
    else:
        print("There is no second command been given")
        return ""

def fetch_url_data(url):
    return requests.get(url)
     
def getting_amount_page(content):
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find(class_="pagination")
    return results.find_all(class_="page-link")[-1].get_text() if results else "0"

def filter_and_store_results(urls, cursor):
    for url in urls:
        response = fetch_url_data(url)
        soup = BeautifulSoup(response.content, "html.parser")
        deeper_soup = soup.find(class_="row")
        results = deeper_soup.find_all(class_="cheese-item")
        for result in results:
            title = result.find("h3")
            name = title.find("a").get_text()
            cursor.execute("SELECT COUNT(*) FROM cheeses WHERE title = ?", (name,))
            # If the title is already in the sqlite db then it doesnt insert a new title
            if cursor.fetchone()[0] == 0:
                cursor.execute("INSERT INTO cheeses (title) VALUES (?)", (name,))
    
def getting_all_urls(amount):
    current = 1
    urls = []
    while current <= amount:
        link = f"https://www.cheese.com/alphabetical?page={current}&per_page=100"
        urls.append(link)
        current += 1
    return urls

def main():
    conn = sqlite3.connect('cheeses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cheeses
                      (title text)''')
    
    page = fetch_url_data(url)
    page_content = page.content
    amounts = int(getting_amount_page(page_content))
    print(amounts)
    all_urls = getting_all_urls(amounts)
    filter_and_store_results(all_urls, cursor)
    search_terms = search_term()
    cursor.execute("SELECT title FROM cheeses WHERE title LIKE ?", ('%' + search_terms + '%',))
    results = cursor.fetchall()
    for result in results:
        print(result[0])
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    main()