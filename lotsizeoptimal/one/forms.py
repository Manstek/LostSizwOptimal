from django import forms


class BatchCalculatorForm(forms.Form):
    n = forms.IntegerField(label="Количество операций (n)", min_value=1, initial=5)
    alpha = forms.FloatField(label="Коэффициент допустимых потерь времени (alpha)", min_value=0, max_value=1, initial=0.02)
    t_pz = forms.CharField(label="Время на подготовительно-заключительные работы (t_pz)", initial="1,2,3,4,5")
    t_sht = forms.CharField(label="Норма штучного времени (t_sht)", initial="6,7,8,9,10")
