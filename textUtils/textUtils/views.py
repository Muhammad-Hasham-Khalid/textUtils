# user defined
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    # params = {'name' : 'Coder', 'place' : 'Earth'}
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    analyzed = text
    purposes = []

    if request.POST.get('fullcaps', 'off') == 'on':
        purposes.append('Changed to UpperCase.')
        analyzed = analyzed.upper()

    if request.POST.get('removepunc', 'off') == 'on':
        temp = analyzed; analyzed = ''
        purposes.append('Removed Punctuations.')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in temp:
            if char not in punctuations:
                analyzed += char
        del temp

    if request.POST.get('newlineremover', 'off') == 'on':
        purposes.append('New lines Removed.')
        temp = analyzed; analyzed = ''
        for char in temp:
            if char != '\n' and char!='\r':
                analyzed += char
        del temp

    if request.POST.get('extraspaceremover', 'off') == 'on':
        purposes.append('Extra spaces removed.')
        temp = analyzed; analyzed = ''
        for idx, char in enumerate(temp):
            if idx != len(temp):
                if not (temp[idx] == ' ' and temp[idx + 1]==' '):
                    analyzed += char
        del temp

    if request.POST.get('charcount', 'off') == 'on':
        purposes.append('Total number of Characters in your text are : ' + str(len(text)))

    if len(purposes) == 0: purposes.append('No change.')

    params = {'purpose' : purposes, 'analyzed_text' : analyzed}
    return render(request, 'analyze.html', params)

