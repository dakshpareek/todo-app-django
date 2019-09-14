from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category
# Create your views here.
def home(request):
    obj=Category.objects.all()
    return render(request,'task/home.html',{'object':obj})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
        #print(form)
    return render(request, 'task/add_category.html', {'form': form})
