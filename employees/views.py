
from django.http import  HttpResponse
from django.shortcuts import get_object_or_404, render
from employees.models import Employee

# Create your views here.

def employee_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    context ={
        'employee':employee,
    }
    return render (request,'employee_detail.html',context)

 
 
 
 
 
 
    # return HttpResponse(employee) - to return the employee name using http response
    #     employee = Employee.objects.get(pk=pk)#to get one data we use get()
    #     print(employee)
    # except:
    #     raise Http404("Employee does not exist")
    
    
