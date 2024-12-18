import math
from django.shortcuts import render
from .forms import ProductionMetricsForm

def calculate_production_metrics(N, S_H, S_D, S_X):
    n_0_exact = math.sqrt((2 * N * S_H) / S_X)
    n_0 = round(n_0_exact)
    average_inventory = n_0 / 2
    production_speed = N / 365
    annual_costs = ((N * S_H) / n_0) + (S_D * N) + (n_0 * S_X / 2)
    return average_inventory, production_speed, annual_costs, n_0, n_0_exact

def production_metrics_view(request):
    if request.method == "POST":
        form = ProductionMetricsForm(request.POST)
        if form.is_valid():
            N = form.cleaned_data["N"]
            S_H = form.cleaned_data["S_H"]
            S_D = form.cleaned_data["S_D"]
            S_X = form.cleaned_data["S_X"]

            avg_inventory, prod_speed, total_costs, n_0, n_0_exact = calculate_production_metrics(N, S_H, S_D, S_X)

            return render(request, "production_metrics_results.html", {
                "form": form,
                "results": {
                    "avg_inventory": avg_inventory,
                    "prod_speed": prod_speed,
                    "total_costs": total_costs,
                    "n_0": n_0,
                    "n_0_exact": n_0_exact,
                },
            })
    else:
        form = ProductionMetricsForm()

    return render(request, "production_metrics.html", {"form": form})
