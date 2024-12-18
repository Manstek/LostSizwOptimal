from django.shortcuts import render
from django.http import JsonResponse

from .forms import BatchCalculatorForm


def calculate_batch_size(alpha, t_pz, t_sht):
    """
    Рассчитывает размер партии для одной операции.
    :param alpha: коэффициент допустимых потерь времени на переналадку оборудования
    :param t_pz: время на подготовительно-заключительные работы (в минутах)
    :param t_sht: норма штучного времени для обработки одной детали (в минутах)
    :return: минимальный размер партии для одной операции
    """
    return (1 - alpha) * t_pz / (alpha * t_sht)

def calculate_min_batch(alpha, t_pz_list, t_sht_list):
    """
    Определяет общий минимальный размер партии.

    :param alpha: коэффициент допустимых потерь времени на переналадку оборудования
    :param t_pz_list: список времен на подготовительно-заключительные работы (в минутах)
    :param t_sht_list: список норм штучного времени для обработки одной детали (в минутах)
    :return: список минимальных величин партий для каждой операции и общий минимальный размер партии
    """
    batch_sizes = [
        calculate_batch_size(alpha, t_pz, t_sht)
        for t_pz, t_sht in zip(t_pz_list, t_sht_list)
    ]
    return batch_sizes, max(batch_sizes)

def batch_calculator(request):
    if request.method == "POST":
        form = BatchCalculatorForm(request.POST)
        if form.is_valid():
            try:
                n = form.cleaned_data["n"]
                alpha = form.cleaned_data["alpha"]
                t_pz = list(map(float, form.cleaned_data["t_pz"].split(",")))
                t_sht = list(map(float, form.cleaned_data["t_sht"].split(",")))

                if len(t_pz) != n or len(t_sht) != n:
                    return JsonResponse({"error": "Длины списков t_pz и t_sht должны совпадать с n."}, status=400)

                batch_sizes, min_batch_size = calculate_min_batch(alpha, t_pz, t_sht)

                # return JsonResponse({
                #     "batch_sizes": batch_sizes,
                #     "min_batch_size": min_batch_size
                # })
                return render(request, "batch_calculator_result.html", {"batch_sizes": batch_sizes,
                    "min_batch_size": min_batch_size})

            except (ValueError, TypeError) as e:
                return JsonResponse({"error": f"Ошибка ввода данных: {str(e)}"}, status=400)
        else:
            return JsonResponse({"error": "Некорректные данные формы."}, status=400)

    else:
        form = BatchCalculatorForm()

    return render(request, "batch_calculator.html", {"form": form})