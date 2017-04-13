from django.db import models
from redactor.fields import RedactorField
from accounts.models import User

from utils import get_file_path


class Publication(models.Model):
    title = models.CharField(max_length=255)
    body = RedactorField(verbose_name=u'Text')
    image = models.FileField(upload_to=get_file_path)
    author = models.ForeignKey(User)
    added = models.DateTimeField(auto_now_add=True)

