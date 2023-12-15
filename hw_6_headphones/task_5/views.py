from django.shortcuts import render
from .models import HeadPhone


def headphone_info(request):
    model_name = request.GET.get('model')
    try:
        headphone = HeadPhone.objects.get(model=model_name)
    except:
        HeadPhone.DoesNotExist: headphone = None
    return render(request, 'task_5/index.html', {'headphone': headphone})