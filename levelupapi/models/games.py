from django.db import models


class Game(models.Model):

    title = models.CharField(max_length=30)
    maker = models.CharField(max_length=30)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()

    
   