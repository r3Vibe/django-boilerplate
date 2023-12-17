server:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
push:
	git add .
	git commit -m "script update"
	git push