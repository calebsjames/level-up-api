
from levelupapi.models.gamer import Gamer
from levelupapi.models.events import GameEvent
from django.db import models


class GamerEvent(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(GameEvent, on_delete=models.CASCADE)