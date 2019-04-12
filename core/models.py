from django.db import models
from accounts.models import DateMixin
from accounts.models import User


class Idea(DateMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=99, null=False)
    summary = models.TextField(max_length=200, null=True)
    detail = models.TextField(max_length=99999, null=False, verbose_name="detail")

    def __str__(self):
        return '%s' % self.title
