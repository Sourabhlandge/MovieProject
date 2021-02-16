from django.shortcuts import render
from mapp.models import Movies
from mapp import forms

# Create your views here.
def showIndex(request):
    return render(request,"movies_index.html")

def addmovie(request):
    form = forms.MovieForm()
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Data inserted Successfully')
    return render(request, "addmovie.html",{"form":form})


def listmovies(request):
    listmovie  = Movies.objects.all()
    my_dict = {"listmovies":listmovie}
    return render(request,"listmovies.html",context=my_dict)