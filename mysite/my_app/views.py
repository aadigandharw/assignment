from urllib import request
from django.shortcuts import render
from .models import users
from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def New_User(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")

        users.objects.create(
            name=name,
            email=email,
            role=role
        )

        return redirect("/users/")

    return render(request, "new_user.html")


def UserList(request, id=None):
    if id:
        userData = users.objects.filter(pk=id)
    else:
        userData = users.objects.all()
    return render(request, "user.html", {"users": userData})

def HelloView(request):
    return HttpResponse("Hello World")
