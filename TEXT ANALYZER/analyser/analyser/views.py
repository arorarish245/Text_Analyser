from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #GET THE TEXT
    mytext=request.POST.get('text','default')
    #CHECK CHECKBOX IN ON OR OFF
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=='on':
        punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for  char in mytext:
            if char not in punc:
                analyzed=analyzed+char
        d={'purpose':'Remove Punctuations' , 'analyzed_text':analyzed}
        mytext=analyzed
        #return render(request,'analyze.html',d)
    if (fullcaps=="on"):
        analyzed=""
        for char in mytext:
            analyzed=analyzed+char.upper()
        d={'purpose':'Capitilise the text' , 'analyzed_text':analyzed}
        mytext=analyzed
        #return render(request,'analyze.html',d)
    if (newlineremover=="on"):
        analyzed=""
        for char in mytext:
            if char!="\n":
                analyzed=analyzed+char
        d={'purpose':'New Line Remover' , 'analyzed_text':analyzed}
        mytext=analyzed
        #return render(request,'analyze.html',d)
    if (spaceremover=="on"):
        analyzed=""
        for index,char in enumerate(mytext):
            if not(mytext[index]==' ' and mytext[index+1]==' '):
                analyzed=analyzed+char
        d={'purpose':'Space Remover' , 'analyzed_text':analyzed}
        mytext=analyzed
        #return render(request,'analyze.html',d)
    return render(request,'analyze.html',d)
    #else:
        #return HttpResponse("Error")

#def newlinerremove(request):
    #return HttpResponse("New Liner Remover")

#def spaceremover(request):
    #return HttpResponse("Space Remover") 

#def charcount(request):
    #return HttpResponse("Char count")  