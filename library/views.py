from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
model_list = [PASSIVE,CLOCK_TIMING]
def index(request, *args, **kwargs):
    passive = request.POST['passive'] 
    clock_Timing = request.POST['passive'] 
    form = DetailForm
    form = form(request.POST or None)
    if request.method == 'POST':
        print(request.POST.get('name'))
        if form.is_valid():
            if request.POST.get('ctype') == 'passive':
                form.save()
            elif request.POST.get('ctype') == 'Clock_Timing':
                form = Clockform(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'CONNECTOR':
                form = CONNECTOR(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'DISCRETE_ANALOG':
                form = DISCRETE_ANALOG(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'ELECTRO_MECHANICAL':
                form = ELECTRO_MECHANICAL(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'ANALOG_POWER':
                form = ANALOG_POWER(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'IC_CLASS_A':
                form = IC_CLASS_A(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'IC_MEMORY':
                form = IC_MEMORY(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'INTERFACE_LOGIC':
                form = INTERFACE_LOGIC(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'MECHANICAL':
                form = MECHANICAL(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'IC_RF':
                form = IC_RF(request.POST)
                form.save()
            elif request.POST.get('ctype') == 'IC_SENSOR':
                form = IC_SENSOR(request.POST)
                form.save()
    # if request.method == 'POST':
    #     search = request.POST.get('search').split('=')[1]
    #     print(search)
    #     search_result = PASSIVE.objects.filter(name__contains=search)
    #     print(search_result)
    # return render(request, 'library/form.html', {
    #     'form' : form,
        
        # 'search_result' : search_result
    })

    