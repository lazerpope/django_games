from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from . import models

from random import choice

def get_token():
    return ''.join([choice('abcdefghijklmnopqrstuvwxyz1234567890') for i in range(5)]).lower()


def index(request):

    if request.method == 'POST':

        if not request.user.is_authenticated:            
            return redirect('login')
        
        try:
            game_id = int(request.body)
            token = get_token()
            number_of_existing_match_with_same_token = models.Match.objects.filter(token=token).count()
            while number_of_existing_match_with_same_token != 0 :
                token = get_token()
                number_of_existing_match_with_same_token = models.Match.objects.filter(token=token).count()
           
            _match = models.Match.objects.create(
                token=token,
                owner= request.user,
                game=models.Game.objects.get(id=game_id)
            )
            _match.save()

            return redirect('connect_to_game' , token=token , )
        except Exception as e:
            print(e)
            redirect('home')
        



    games = models.Game.objects.all()

    context = {"games": games}
   

    return render(request, "main/index.html", context)




@login_required(login_url="/login")
def connect_to_game(request, **kwargs):

    try:
        match_token = kwargs.get('token')
        if match_token is None:
            raise ValueError('match token not provided')
        match_token = match_token.lower()

        match_obj = models.Match.objects.get(token=match_token)

        if match_obj.owner != request.user and match_obj.opponent == None:
            match_obj.opponent = request.user
            match_obj.save()

     
        context = {"match_obj": match_obj , }

    except Exception as e:
        print(e)
        return redirect('home')

    return render(
        request,
        "main/start_new_game.html",
        context
    )





# @login_required(login_url="/login")
# def start_new_game(request):


#     games =  models.Game.objects.all()

#     context = {'games':games}
#     print(context)
#     return render(request , 'main/index.html' , context )