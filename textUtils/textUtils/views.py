# user defined
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', 'default')
    analyzed = text
    purposes = []

    if request.GET.get('fullcaps', 'off') == 'on':
        purposes.append('Changed to UpperCase.')
        analyzed = analyzed.upper()

    if request.GET.get('removepunc', 'off') == 'on':
        temp = analyzed; analyzed = ''
        purposes.append('Removed Punctuations.')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in temp:
            if char not in punctuations:
                analyzed += char
        del temp

    if request.GET.get('newlineremover', 'off') == 'on':
        purposes.append('New lines Removed.')
        temp = analyzed; analyzed = ''
        for char in temp:
            if char != '\n' and char!='\r':
                analyzed += char
        del temp

    if request.GET.get('extraspaceremover', 'off') == 'on':
        purposes.append('Extra spaces removed.')
        temp = analyzed; analyzed = ''
        for idx, char in enumerate(temp):
            if idx != len(temp):
                if not (temp[idx] == ' ' and temp[idx + 1]==' '):
                    analyzed += char
        del temp

    if request.GET.get('charcount', 'off') == 'on':
        purposes.append('Total number of Characters in your text are : ' + str(len(text)))

    if len(purposes) == 0: purposes.append('No change.')

    params = {'purpose' : purposes, 'analyzed_text' : analyzed}
    return render(request, 'analyze.html', params)

