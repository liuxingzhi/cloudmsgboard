from django.db import models

# Create your models here.
"""
查看migration的sql
python manage.py sqlmigrate msgapp 0002
"""
class MsgBoard(models.Model):
    sender = models.CharField(max_length=64)
    receiver = models.CharField(max_length=64)
    message = models.CharField(max_length=1024)
    time = models.DateTimeField(primary_key=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} : {self.message} at {self.time}"