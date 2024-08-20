from django.shortcuts import render, redirect
from . import models
from  django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dict={"tweets": all_tweets}
    return render(request,'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:       
        tweet=request.POST["tweet"]
        models.Tweet.objects.create(user=request.user, tweet=tweet)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request,'tweetapp/addtweet.html')
    
@login_required
def deletetweet(request,id):
    tweet=models.Tweet.objects.get(pk=id)
    if request.user == tweet.user:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweetapp:listtweet')
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



