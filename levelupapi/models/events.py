from django.db import models


class Event(models.Model):

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="attending")



