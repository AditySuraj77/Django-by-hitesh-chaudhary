from django.shortcuts import render
from .forms import TweetForms
from .models import Tweet
from django.shortcuts import get_object_or_404,redirect


# def Tweet(request):
#     return render(request,'index.html')


def Tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request,'tweet_list.html',{'tweets':tweets})


def Tweet_create(request):
    if request.method == "POST":
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(Tweet_list)
    else:
        form = TweetForms()
    return render(request,'tweet_form.html',{"form":form})





def Tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        form = TweetForms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(Tweet_list)
    else:
        form = TweetForms(instance=tweet)
    return render(request,'tweet_form.html',{"form":form})


def Tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk= tweet_id, user= request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect(Tweet_list)
    return render(request,'tweet_deletion_form.html',{"tweets":tweet})

