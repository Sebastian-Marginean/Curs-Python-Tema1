import requests
from bs4 import BeautifulSoup

def get_page_info(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"
        description_tag = soup.find('meta', attrs={'name': 'description'})
        description = description_tag.get('content').strip() if description_tag else "No description found"
        return title, description
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None, None

if __name__ == "__main__":
    input_url = input("Introduceți URL-ul paginii web: ")
    title, description = get_page_info(input_url)
    if title and description:
        print(f"Titlul paginii: {title}")
        print(f"Descrierea: {description}")
    else:
        print("Nu s-a putut obține informația despre pagină.")
