from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def class_temp(request):
    return render(request, 'second_task/class_template.html')


def func_temp(request):
    return render(request, 'second_task/func_template.html')


#def m_p(request):
    #return HttpResponse('Главная Страница')
