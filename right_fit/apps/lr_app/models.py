from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        print("validator works...")
        errors = {}
        email_match = User.objects.filter(email = postData['email'])
        if len(postData['email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email_invalid'] = 'Please enter a valid email address.'
        elif len(email_match) > 0:
            errors['email_invalid'] = 'That email exists in the database already.'
        if len(postData['first-name']) == 0:
            errors['first_name_blank'] = 'The first name field cannot be blank.'
        elif len(postData['first-name']) < 2:
            errors['first_name_short'] = 'The first name field must be at least 2 characters.'
        elif postData['first-name'].isalpha() == False:
            errors['first_name_alpha'] = 'The first name field must contain only letters.'
        if len(postData['last-name']) == 0:
            errors['last_name_blank'] = 'The last name field cannot be blank.'
        elif len(postData['last-name']) < 3:
            errors['last_name_short'] = 'The last name field must be at least 2 characters.'
        elif postData['last-name'].isalpha() == False:
            errors['last_name_alpha'] = 'The last name field must contain only letters.'
        if len(postData['password']) == 0:
            errors['pword_blank'] = 'The password field cannot be blank.'
        elif len(postData['password']) < 8:
            errors['pword_short'] = 'The password field must be at least eight characters.'
        if (postData['password'] != postData['password-confirm']):
            errors['pword_match_fail'] = 'Passwords do not match.'
        return errors

    def login_validator(self,postData):
        errors={}
        user_to_login = User.objects.filter(email = postData['login-email'])
        if len(user_to_login) == 0:
            errors['invalid'] = "Invalid login credentials."
        else:
            user_to_login = User.objects.get(email = postData['login-email'])
            if postData['login-password'] == user_to_login.password:
                print("Password accepted, logging in...")
            else:
                errors['invalid'] = "Invalid login credentials."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()