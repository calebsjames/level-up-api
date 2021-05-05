from django.db import models


class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    event_date = models.DateField()
    event_time = models.TimeField()
    description = models.CharField(max_length=200)
    attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="attending")



