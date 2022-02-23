from django.shortcuts import redirect, render
from app1.forms import employeeforms
from .models import employees

# Create your views here.



#index for form
# def form(request):
#     return render(request,'form.html')

#add is a denoted as form input
def add(request):
    form=employeeforms()
    return render(request, 'form.html',{'form':form})

#store data from form to sql database
def product_details(request):
    if request.method == 'POST':
        form = employeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')
    form=employeeforms()
    return render(request,'form.html',{'form':form})
    

#show products
def view(request):
    products=employees.objects.all() #fetch all data from database to products(productis a veriable)
    return render(request,'view.html', {'products':products})


#eUpdate page
def edit_details(request,pk):
    empl=employees.objects.get(id=pk)
    form=employeeforms(instance=empl)
    if request.method =='POST':
        form=employeeforms(request.POST,instance=empl)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'edit.html',{'form':form})



#delete

def delete(request,pk):
    products=employees.objects.get(id=pk)
    return render(request,'delete.html', {'products':products})

#deleting products

def delete_product(request,pk):
    products=employees.objects.get(id=pk)
    products.delete()
    return redirect('view')