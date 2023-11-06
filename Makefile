up:
	sudo docker compose -f docker-compose.yaml up -d
down:
	sudo docker compose -f docker-compose.yaml down && docker network prune --force