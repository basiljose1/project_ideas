from django.db import models
from accounts.models import DateMixin
from accounts.models import User

class Idea(DateMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=99, blank=False, null=False)
    detail = models.TextField(max_length=999, null=False, verbose_name="detail")

    # voters = models.ManyToManyField(User,through="Vote", null=True,related_name="idea_vote_creator")

    def __str__(self):
        return '%s' % self.title
