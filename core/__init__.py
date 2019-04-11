from core.models import MPTTComment
from core.forms import MPTTCommentForm

def get_model():
    return MPTTComment

def get_form():
    return MPTTCommentForm