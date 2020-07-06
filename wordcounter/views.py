from django.http import HttpResponse
from django.shortcuts import render

def homepage(req):
    return render(req,"home.html",{'title':'home page is here'})

def aboutpage(req):
    return HttpResponse("<h1>About page template is here</h1>")

def count(req):
    # letter_count = len(req.GET['text_area'])
    fulltext = req.GET['text_area']
    wordlist = fulltext.split()
    count = len(wordlist)
    word_dict = dict()
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return render(req,"count.html",{'count':count,'fulltext':fulltext,'dict':word_dict})