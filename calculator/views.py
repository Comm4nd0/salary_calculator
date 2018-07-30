from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Calc
import json


# Create your views here.

def calc(request):
    calc = Calc.objects
    return render(request, 'calc.html', {'calc': calc})


def net_calc(request):
    if request.is_ajax() and request.POST:
        per = request.POST.get('per')
        salary = request.POST.get('salary')
        salary = float(salary)

        if per == 'yearly':
            # Do nothing!
            pass
        elif per == 'monthly':
            salary = salary * 12
        elif per == 'weekly':
            salary = salary * 52
        elif per == 'daily':
            salary = salary * 261

        if salary > 11850:
            taxable_salary = salary - 11850
            twenty_percent_of_salary = (20 * taxable_salary) / 100.0
            twenty_percent_bracket = taxable_salary - twenty_percent_of_salary
            net_salary = twenty_percent_bracket + 11850

            if salary > 46351 and salary < 150000:
                taxable_salary = (salary - 11850) - 46350
                fourty_percent_of_salary = (40 * taxable_salary) / 100.0
                fourty_percent_bracket = taxable_salary - fourty_percent_of_salary
                net_salary = net_salary + fourty_percent_bracket
        else:
            net_salary = salary

        data = {'salary': round(salary, 2),
                'monthly_salary': round(salary / 12, 2),
                'weekly_salary': round(salary / 52, 2),
                'daily_salary': round(salary / 261, 2),
                'net_salary': round(net_salary, 2),
                'net_monthly_salary': round(net_salary / 12, 2),
                'net_weekly_salary': round(net_salary / 52, 2),
                'net_daily_salary': round(net_salary / 261, 2),
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
