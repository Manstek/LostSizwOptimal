import math
from django.shortcuts import render
from .forms import InputForms, TableForms


def index(request):
    if request.method == 'POST':
        form = InputForms(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            forms = [TableForms(prefix=f"form_{i}") for i in range(n)]
            return render(request, "index.html", {"form": form, "forms": forms})
    else:
        form = InputForms()

    return render(request, "index.html", {"form": form})


def calculate(request):
    if request.method == 'POST':
        n = int(request.POST.get("n", 0))
        forms = [TableForms(request.POST, prefix=f"form_{i}") for i in range(n)]
        if all(form.is_valid() for form in forms):
            batches = []
            for form in forms:
                data = form.cleaned_data

                # Константы
                F = 0.1  # 10%
                F_star_gamma_1 = 0.1  # 10%
                Ф_gamma_1 = 800
                m_gamma_1 = 0
                D_gamma_1 = 10**3
                T = 900

                # Числитель
                numerator = (
                    data["N_1"] * data["Ц_1"] +
                    data["N_1"] * data["tau"] * ((D_gamma_1 * F_star_gamma_1) / Ф_gamma_1) -
                    m_gamma_1 * data["N_1"] * data["tau"]
                )

                if not data['U_s']:
                    # Знаменатель для независимой партии
                    tmp = (
                        data["V_u"] * data["a_u"] * ((data["N_1"] / T) * data["t_1"] - 1 + (2 * data["N_u"] * data["t_u"]) / T) +
                        data["V_1"] * (1 - (data["N_1"] * data["t_1"]) / T)
                    )
                    denominator = (F / 2) * tmp

                    if denominator <= 0:
                        raise ValueError("Знаменатель равен 0 или отрицателен, проверьте входные данные!")

                    p_1s = math.sqrt(numerator / denominator)
                else:
                    # Знаменатель для зависимой партии
                    denominator_tmp = []
                    U_s = data['U_s'].split(',')
                    for el in U_s:
                        idx = int(el) - 1
                        dependent_data = batches[idx]

                        tmp = (
                            dependent_data["V_u"] * data["a_u"] * ((data["N_1"] / T) * data["t_1"] - 1 + (2 * dependent_data["N_u"] * dependent_data["t_u"]) / T) +
                            data["V_1"] * (1 - (data["N_1"] * data["t_1"]) / T)
                        )
                        denominator = (F / 2) * tmp

                        if denominator <= 0:
                            raise ValueError("Знаменатель равен 0 или отрицателен, проверьте входные данные!")

                        denominator_tmp.append(denominator)

                    # Вычисление минимального значения p_1s среди зависимых партий
                    p_1s_values = [math.sqrt(numerator / d) for d in denominator_tmp]
                    p_1s = min(p_1s_values)

                # Сохранение данных о партии
                batch_data = data.copy()
                batch_data["p_1s"] = p_1s
                batch_data["p_1s_rounded"] = round(p_1s)

                batches.append(batch_data)

            return render(request, "results.html", {"batches": batches})
    else:
        form = InputForms()

    return render(request, "calculate.html", {"form": form})
