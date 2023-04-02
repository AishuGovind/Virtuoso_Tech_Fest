from django.shortcuts import render, redirect
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegisterForm

# Create your views here.
def home(request):
    newdata = RegisterForm.objects.all()
    if (newdata != ''):
        return render(request,"home.html", {'data':newdata})
    else:
        return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Registration completed successfully!')
                return redirect ("home")
            except:
                pass
    else:
        form = MyRegisterForm()
    return render(request, "register.html", {'form':form})

def update(request, id):
    data = RegisterForm.objects.get(id =id)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        event = request.POST['event']
        contact = request.POST['contact']
        email = request.POST['email']

        data.Name = name
        data.Age = age
        data.Event_Name = event
        data.Contact_Number = contact
        data.Email_ID = email
        data.save()
        messages.success(request,'Registration updated successfully!')
        return redirect('home')

    return render(request, "update.html", {'data':data})

def delete(request, id):
    data = RegisterForm.objects.get(id =id)
    data.delete()
    messages.error(request,'Deleted the record successfully!')
    return redirect('home')

