from django.db import models


class Newsletter(models.Model):
    """ Subscribe model """

    email = models.EmailField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
