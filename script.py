import requests
from bs4 import BeautifulSoup
import json
import sys

def scrape_lyrics(letra_url):
  response = requests.get(letra_url)
  if response.status_code != 200:
    print(f"Erro ao acessar a página: {response.status_code}")
    return

  soup = BeautifulSoup(response.content, 'html.parser')

  title = soup.find("h1", class_="textStyle-primary").text.strip()
  artist = soup.find("h2", class_="textStyle-secondary").text.strip()
  
  lyrics_div = soup.find("div", class_="lyric-original")
  if not lyrics_div:
    print("Letra não encontrada.")
    return
  
  content = [
    "<br>".join(stanza.stripped_strings)
    for stanza in lyrics_div.find_all("p")
  ]

  music_data = {
    "id": f"{artist.replace(' ', '-').lower()}-{title.replace(' ', '-').lower()}",
    "name": title,
    "artist": artist,
    "youtube_url": "",
    "cifra_url": "",
    "letra_url": letra_url,
    "content": content,
  }
  
  print(json.dumps(music_data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    letra_url = sys.argv[1]
    scrape_lyrics(letra_url)
  else:
    print("Nenhuma URL fornecida.")
