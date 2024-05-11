from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm, ItemForm, OrderForm

# Create your views here.






def home(request):
    context={}
    return render(request, "myApp/home.html", context)
def Login(request):
    context={}
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not null:
                login(request, user)
                return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, "myApp/Login.html", context, {'form': form})
def Admin(request):
    context={}
    return render(request, "myApp/Admin.html", context)
def Menu(request):
    context={}
    return render(request, "myApp/Menu.html", context)

def Order(request):
    context={}
    if request.method == 'POST':
        form = OrderForm(request)
        if form.is_valid():
            order = form.save()
            total = order.total_price
            return render(request, 'myApp/confirmOrder.html', {'order': order, 'total': total})
    else:
        form = OrderForm()
    return render(request, "myApp/Order.html", context)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post:list")
        form = UserCreationForm()
    return render(request, "myApp/Register.html", {"form": form })

def admin_check(user):
    return user.is_superuser
@user_passes_test(admin_check)
def addItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'myApp/addItem.html', {'form': form})




