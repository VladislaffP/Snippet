from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import SnippetForm
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth

from Snippets.MainApp.forms import UserRegistrationForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required()
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
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect('snip-list')

def snippets_page(request):
    #sn = Snippet.objects.all()
    #username = request.user
    #if not request.user.is_authenticated:
    #    sn = Snippet.objects.filter(user__username=None)
    #else:
    #    sn = Snippet.objects.filter(user__username=username)
    sn = SnippetForm.objects.filter(is_public=True)
    #cnt = Snippet.objects.count()
    cnt = sn.count()
    context = {
        "sn": sn,
        "cnt": cnt
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, snippet_id):
    snippet = SnippetForm.objects.get(id=snippet_id)
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippet': snippet
    }
    return render(request, 'pages/snippet-detail.html', context)


def snippet_delete(request, snippet_id):
    snippet = SnippetForm.objects.get(id=snippet_id)
    snippet.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')
    #return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required()
def snippets_my(request):
    username = request.user
    sn = SnippetForm.objects.filter(user__username=username)
    cnt = sn.count()
    context = {
        "sn": sn,
        "cnt": cnt
    }
    return render(request, 'pages/view_snippets.html', context)

def create_user(request):
    context = {'pagename': 'Регистрация пользователя'}
    if request.method == "GET":
        form = UserRegistrationForm()
        context["form"] = form
        return render(request, 'pages/registration.html', context)
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


