from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method =='GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form}
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        #name = request.POST["name"]
        #lang = request.POST["lang"]
        #code = request.POST["code"]
        #snippet = Snippet(name=name, lang=lang, code=code)
        #snippet.save()
        form =SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snip-list')

def snippets_page(request):
    sn = Snippet.objects.all()
    cnt = len(sn)
    context = {
        "sn": sn,
        "cnt": cnt
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request):
    #
    pass


