import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class question(models.Model):
    quest = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.quest
    def publish_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class choice(models.Model):
    ques = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice

