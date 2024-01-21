from django.shortcuts import render
from .forms import CalculationForm


def calculate(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            number3 = form.cleaned_data['number3']
            operation = form.cleaned_data['operation']

            if operation == 'min':
                result = min(number1, number2, number3)
            elif operation == 'max':
                result = max(number1, number2, number3)
            elif operation == 'avg':
                result = (number1 + number2 + number3) / 3

            return render(request, 'result.html', {'result': result})

    else:
        form = CalculationForm()

    return render(request, 'task_2/calculate.html', {'form': form})

