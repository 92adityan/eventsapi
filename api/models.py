from django.db import models
from django.contrib.auth.models import User




class Event(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    open_to_book = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, limit_choices_to={'open_to_book': True}, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.event.name}'