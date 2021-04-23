from django.shortcuts import render
from app.models import Employee
from django.core.paginator import Paginator

# Create your views here.



def index(request):

    # all_data = Employee.objects.all()
    user_list = Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 1)
    try:
        portfolio = paginator.page(page)
    except :
        portfolio = paginator.page(1)

    return render(request,'index.html',{'portfolio' : portfolio})

