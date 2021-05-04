from django.db import models


class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    player_limit = models.IntegerField()
    difficulty = models.IntegerField()
   