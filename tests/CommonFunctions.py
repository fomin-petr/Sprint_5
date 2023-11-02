import random
from random import choice
from string import ascii_letters


class Helper:
    @staticmethod
    def email_randomizer():
        email = ''
        for i in range(8):
            email += choice(ascii_letters)
        email += '__' + str(random.randint(0, 99999999)) + '@yaya.ru'
        return email

    @staticmethod
    def password_randomizer():
        password = random.randint(100000, 999999)
        return password