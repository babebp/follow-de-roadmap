build:
	docker build -t follow-de-roadmap .

run:
	docker run --name follow-de-roadmap -d follow-de-roadmap

start:
	docker start follow-de-roadmap

stop:
	docker stop follow-de-roadmap