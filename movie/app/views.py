from django.shortcuts import render
from app.models import Movie
from app.forms import Movieform
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def base(request):
    return render(request, 'base.html')
# def home(request):
#     movies = Movie.objects.all()
#     return render(request,'home.html',{'movies': movies})

class MovieList(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movies"

# def addmovie(request):
#     if(request.method=="POST"): #after submission
#         form=Movieform(request.POST,request.FILES) #Creates form object initialised with values inside request.POST
#         if form.is_valid():
#             form.save() #saves the form object inside Db table
#         return home(request)
#     form=Movieform()   #empty form object with no values
#     return render(request, 'addmovie.html',{'form':form})

class Movieadd(CreateView):
    model = Movie
    template_name = "addmovie.html"
    fields = '__all__'
    success_url=reverse_lazy('app:home')


# def viewmovie(request,p):
#     # return HttpResponse("Welcome")
#     k=Movie.objects.get(id=p)
#     return render(request,'viewmovie.html',{'movie':k})

class MovieDetail(DetailView):
    model = Movie
    template_name = "viewmovie.html"
    context_object_name = "movie"

# def update(request, p):
#     movie = Movie.objects.get(id=p)
#     if request.method == "POST":
#         form = Movieform(request.POST, request.FILES, instance=movie)
#         if form.is_valid():
#             form.save()
#         return home(request)
#
#     form = Movieform(instance=movie)
#     return render(request, 'update.html', {'form': form})

class Movieupdate(UpdateView):
    model = Movie
    template_name = "addmovie.html"
    fields = '__all__'
    success_url = reverse_lazy('app:home')

# def deletemovie(request, p):
#     movie = Movie.objects.get(id=p)
#     movie.delete()
#     return home(request)

class Moviedelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('app:home')
    template_name = "deletemovie.html"



