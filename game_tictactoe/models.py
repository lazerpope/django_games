from django.db import models

# Create your models here.

from main.models import Match

class TicTacToe(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, primary_key=True)
    # Additional fields specific to TicTacToe
    board_state = models.CharField(max_length=9, default=" " * 9)  # Simplistic representation

    def __str__(self):
        return f"TicTacToe Match {self.match}"