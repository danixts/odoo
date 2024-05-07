clean:
	find . | grep -E "(__pycache__$|\.pyc$|\.pyo$|.idea$)" | xargs rm -rf

dev:
	docker compose -f setup/docker-compose.yml up --build --remove-orphans

# staging commands
_staging_up:
	docker-compose -f setup/docker-compose.yml up -d --build --remove-orphans

_staging_down:
	docker-compose -f setup/docker-compose.yml down --remove-orphans

staging: _staging_down _staging_up

clean_idea_cached_files:
	git rm -r --cached .idea/

install_hooks:
	pre-commit install

format:
	python3 -m black .

lint:
	python3 -m flake8

push: format lint