from django.shortcuts import render

from account.models import User


def account(request):
    return render(request,'account/account.html',{'users':User.objects.all()})
