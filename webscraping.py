import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Hindustan_(newspaper)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")
    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("First 5 Headlines from the Hindustan Wikipedia page:\n\n")
        for i, h2_tag in enumerate(headlines[:5], start=1):
            file.write(f"Headline {i}: {h2_tag.get_text(strip=True)}\n")
            
    print("Successfully saved the headlines to headlines.txt")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
except IOError as e:
    print(f"Error writing to file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
