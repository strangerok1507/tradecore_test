import os
import random
import requests

from faker import Faker

from django.core.management import BaseCommand

NUMBER_OF_USERS = os.environ.get('NUMBER_OF_USERS', default=5)
MAX_POSTS_PER_USER = os.environ.get('MAX_POSTS_PER_USER', default=5)
MAX_LIKES_PER_USER = os.environ.get('MAX_LIKES_PER_USER', default=10)

BASE_URL = os.environ.get('URL', default='http://127.0.0.1:9000/')
POSTS_URL = f'{BASE_URL}api/post/'
LIKE_URL = f'{BASE_URL}api/like/'
USER_URL = f'{BASE_URL}api/user/'


class User:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.password = fake.password()

        self._pk = None
        self.created = False
        self._token = None

    def get_headers(self):
        if self._token is None:
            self.login()
        return {'Authorization': f'Bearer {self._token}'}

    def create_user(self):
        data = {'email': self.email, 'password': self.password}
        response = requests.post(USER_URL, data=data)
        if response.status_code == 201:
            self.created = True
            self._pk = response.json()['id']

    def login(self):
        data = {'email': self.email, 'password': self.password}
        response = requests.post(f'{BASE_URL}api/login/', data=data).json()
        self._token = response['access']
        return response


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        users = []
        for counter in range(NUMBER_OF_USERS):
            user = User()
            user.create_user()
            user.login()
            users.append(user)
            for step in range(random.randint(1, MAX_POSTS_PER_USER)):
                title = fake.sentence()
                text = fake.text()
                user.create_post(title, text)

        emails = [user.email for user in users]
        print(emails)
