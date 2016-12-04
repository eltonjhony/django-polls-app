import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    # retrieve a boolean to check if was published at the same
    # current day
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)