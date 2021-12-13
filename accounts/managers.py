from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, full_name, age, username, email, password):
        if not full_name:
            return ValueError('full_name is required')
        if not age:
            return ValueError('age is required')
        if not username:
            return ValueError('username is required')
        if not email:
            return ValueError('email is required')

        user = self.model(email=self.normalize_email(email), full_name=full_name, age=age, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, age, username, email, password):
        user = self.create_user(full_name, age, username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
