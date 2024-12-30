# Scrape Letras.com

Esse projeto faz um scrape da página web da letras.com
e coloca em formato json.

```bash
make run URL="https://www.letras.com/natal/509388"
```

Output:

```json
{
  "id": "natal-noite-feliz",
  "name": "Noite Feliz",
  "artist": "Natal",
  "letra_url": "https://www.letras.com/natal/509388",
  "youtube_url": "",
  "cifra_url": "",
  "content": [
    "Noite feliz, noite feliz<br>Ó Senhor, Deus de amor<br>Pobrezinho nasceu em Belém<br>Eis na lapa Jesus, nosso bem",
    "Dorme em paz, ó Jesus<br>Dorme em paz, ó Jesus",
    "Noite feliz, noite feliz<br>Eis que, no ar, vêm cantar<br>Aos pastores, os anjos do céu<br>Anunciando a chegada de Deus",
    "De Jesus, Salvador<br>De Jesus, Salvador",
    "Noite feliz, noite feliz<br>Ó Jesus, Deus da luz<br>Quão afável é o Teu coração<br>Que quiseste nascer nosso irmão",
    "E a nós todos salvar<br>E a nós todos salvar"
  ]
}
```
