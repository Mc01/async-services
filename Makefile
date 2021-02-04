run:
	docker-compose exec marcin-client python run.py

rerun:
	docker-compose up -d --force-recreate && make run
