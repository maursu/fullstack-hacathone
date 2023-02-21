##
Description: forum for Makers students and mentors. Users may discuss/aks questions and get an answer, upvote/downvote comments and answers for getting rating point. If your rating more then 3000 you get a "fireman" status. In addition to that you can find similar questions with answers on makersoverflow and use parser to find similar question on stakoverflow.
#
##
You can use make commands (make migrate, make run, make admin and etc.).

Check .env_template to get more information about required data for .env.

Install celery + redis (https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)


#
'''

bash:

python3 -m venv <venv_name>

. venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manahe.py migrate

python manage.py createsuperuser

python manage.py runserver

python3 -m celery -A core worker -l info (use second terminal)

'''


Visit our website: https://makersoverflow.net/