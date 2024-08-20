from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Tweets',{"fields": ["tweet"]}),
        ('Usernames',{"fields": ["username"]}),
    ]
   #fields= ['username', 'tweet']




admin.site.register(Tweet, TweetAdmin)
