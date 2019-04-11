from django.db import models
from accounts.models import DateMixin
from accounts.models import User

from django_comments.models import Comment
from mptt.models import MPTTModel, TreeForeignKey

class Idea(DateMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=99, blank=False, null=False)
    detail = models.TextField(max_length=999, null=False, verbose_name="detail")

    # voters = models.ManyToManyField(User,through="Vote", null=True,related_name="idea_vote_creator")

    def __str__(self):
        return '%s' % self.title

class MPTTComment(MPTTModel, Comment):
    """ Threaded comments - Add support for the parent comment store and MPTT traversal"""

    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['submit_date']

    class Meta:
        ordering=['tree_id','lft']