from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(User)
admin.site.register(Match)

admin.site.register(Game)


admin.site.register(TicTacToe)
admin.site.register(RockPaperScissors)