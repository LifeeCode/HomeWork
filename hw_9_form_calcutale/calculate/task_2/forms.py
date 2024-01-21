from django import forms

OPERATION_CHOICES = (
    ('min', 'Минимум из трёх'),
    ('max', 'Максимум из трёх'),
    ('avg', 'Среднеарифметическое из трёх')
)

class CalculationForm(forms.Form):
    number1 = forms.FloatField(label='Число 1')
    number2 = forms.FloatField(label='Число 2')
    number3 = forms.FloatField(label='Число 3')
    operation = forms.ChoiceField(label='Операция', choices=OPERATION_CHOICES)