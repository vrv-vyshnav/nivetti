from django.shortcuts import render
from .forms import DetailForm
from .models import PASSIVE
# Create your views here.

def index(request):
    form = DetailForm
    form = form(request.POST or None)
    if request.method == 'POST':
        print(request.POST.get('name'))
        if form.is_valid():
            form.save()
    return render(request, 'library/form.html', {
        'form' : form,
    })

def profile_view(request):
    profiles = Detail.objects.raw('SELECT * FROM Details WHERE name = "A*" ')
    
    return render(request, 'library/profile.html', {
        'profiles' : profiles,
    })