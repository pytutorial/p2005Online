from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request, 'index.html')

#@login_required
@staff_member_required
def staffView(request):
    return render(request, 'staff.html')