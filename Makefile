drone-exec:
	drone exec --secret-file .env

docker-run:
	docker-compose run --rm importer
