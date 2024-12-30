build:
	docker build -t scrape-letras .

run:
	docker run --rm scrape-letras $(URL)
