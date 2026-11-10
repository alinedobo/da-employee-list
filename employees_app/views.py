from django.shortcuts import render
from .models import Employee, Department
from django.db.models import Avg, Q
from datetime import date
from decimal import Decimal


def employee_overview(request):
    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    employees = Employee.objects.all()

    rich_employees = employees.filter(salary__gt=3000)

    num_fivekay = employees.filter(salary=5000).count()

    avg_sal_sales = employees.filter(department=1).aggregate(Avg("salary"))
    avg_sal_sales_rounded = avg_sal_sales['salary__avg']

    old_employees = employees.exclude(Q(hire_date__gt=date(2022, 1, 1)) | Q(department=3))

    template_name = "employees_app/employee_list.html"
    
    return render(request, 'employee_list.html', {'employee_list': employees, 'rich_employees': rich_employees, 'num_fivekay': num_fivekay, 'avg_sal_sales_rounded': avg_sal_sales_rounded, 'old_employees': old_employees})
