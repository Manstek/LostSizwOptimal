from django import forms

class ProductionMetricsForm(forms.Form):
    N = forms.IntegerField(label="Годовой объем производства (N)", min_value=1, initial=12)
    S_H = forms.FloatField(label="Затраты на подготовку одной партии (S_H)", min_value=0, initial=14.0)
    S_D = forms.FloatField(label="Себестоимость одной детали (S_D)", min_value=0, initial=15.0)
    S_X = forms.FloatField(label="Затраты на хранение одной детали (S_X)", min_value=0, initial=16.0)
