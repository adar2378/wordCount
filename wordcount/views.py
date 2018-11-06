from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def getKey(item):
    return item[0]


def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedList = sorted(
        worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {"fulltext": text, 'count': len(wordlist), "worddict": sortedList})
