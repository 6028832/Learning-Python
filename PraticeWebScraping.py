import requests
import sys
from bs4 import BeautifulSoup

def get_search_term():
    return sys.argv[1]

def fetch_url_data(url):
    return requests.get(url)

def parse_html_content(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    results = soup.find(id="ResultsContainer")
    return results.find_all("div", class_="card-content")

def filter_and_print_data(job_elements, *terms):
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        if terms:
            if any(term.lower() in title_element.text.lower() for term in terms):
                print(title_element.text.strip())
                print(company_element.text.strip())
                print(location_element.text.strip())
        else:
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())

def main():
    url = "https://realpython.github.io/fake-jobs/"
    search_term = get_search_term()
    page = fetch_url_data(url)
    job_elements = parse_html_content(page.content)
    filter_and_print_data(job_elements, search_term)

if __name__ == "__main__":
    main()