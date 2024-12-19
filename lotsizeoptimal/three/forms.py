from django import forms


class InputForms(forms.Form):
    n = forms.IntegerField(label="Количество (n)", min_value=1, initial=5)


class TableForms(forms.Form):
    N_1 = forms.FloatField(label="Введите значение N_1: ")
    t_1 = forms.FloatField(label="Введите значение t_1: ")
    p_s = forms.FloatField(label="Введите значение p_s: ")
    a_u = forms.FloatField(label="Введите значение a_u: ")
    tau = forms.FloatField(label="Введите значение tau: ")
    V_1 = forms.FloatField(label="Введите значение V_1: ")
    Ц_1 = forms.FloatField(label="Введите значение Ц_1: ")
    V_u = forms.FloatField(label="Введите значение V_u: ")
    N_u = forms.FloatField(label="Введите значение N_u: ")
    t_u = forms.FloatField(label="Введите значение t_u: ")
    U_s = forms.CharField(label="Введите значение U_s: ", required=False)
