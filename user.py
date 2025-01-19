import random

from constants import email_prefix, email_domain

class User:
    def __init__(self):
        self.name = 'TestUser'
        self.email = f'{email_prefix}100{email_domain}'
        self.password = '123qwe'

    def create_random_email(self):
        self.email = f'{email_prefix}{random.randint(100, 999)}{email_domain}'

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return  self.password
