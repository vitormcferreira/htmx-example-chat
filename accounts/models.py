from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        if self.first_name is not None:
            return self.first_name
        return self.username

    def __repr__(self) -> str:
        return self.__str__()
