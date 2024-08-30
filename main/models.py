from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser 




class User(AbstractUser):
    

    def __str__(self):
        return self.username

class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    
    token = models.CharField(max_length=20, unique=True)
    game =  models.ForeignKey(Game , on_delete=models.CASCADE)

    owner = models.ForeignKey(User , on_delete=models.CASCADE,related_name='owned_matches')
    opponent = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True, related_name='opponent_matches')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        opponent = self.opponent.username if self.opponent else "No opponent"
        return f"{self.game.name} match between {self.owner.username} and {opponent}"




# class RockPaperScissors(models.Model):
#     match = models.OneToOneField(Match, on_delete=models.CASCADE, primary_key=True)
#     # Additional fields specific to RockPaperScissors
#     player1_choice = models.CharField(max_length=10)
#     player2_choice = models.CharField(max_length=10)

#     def __str__(self):
#         return f"RockPaperScissors Match {self.match}"
