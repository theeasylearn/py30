import requests
from bs4 import BeautifulSoup

def extract_between(url, start_marker, end_marker):
    # Try raw requests first
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        html = resp.text
    except Exception:
        html = None

    for source in ('raw', 'selenium'):
        if source == 'selenium' or html is None:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html = driver.page_source
            driver.quit()

        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(separator=" ").strip()
        if start_marker in text and end_marker in text:
            start = text.find(start_marker) + len(start_marker)
            end = text.find(end_marker)
            return text[start:end].strip(" ·:-–")
    return None

url = "https://www.divyabhaskar.co.in/rashifal/13/today?ref=inbound_RHS"
result = extract_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
# print("Extracted text:", result)
with open("kathan.txt", "w", encoding="utf-8") as f:
    f.write(result)
print("File saved as kathan.txt")