# makefile

start-dev:
	docker-compose up

start-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

stop-compose:
	@eval docker stop $$(docker ps -a -q)
	docker-compose down

ssh-nginx:
	docker exec -it nginx_server bash

ssh-web:
	docker exec -it myshop_web bash

ssh-db:
	docker exec -it db bash

check-network-config-details:
	docker network inspect myshop_default

build-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

build-dev:
	docker-compose build