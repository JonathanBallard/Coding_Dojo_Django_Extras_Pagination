from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import LeadForm
 
 
# Create your views here. 
def index(request): 
    form = LeadForm
    renderTable = []
    allLeads = Lead.objects.all()

    for i in range(5):
        renderTable.append(allLeads[i])

    context = {
        'lead_form' : form,
        'all_leads' : allLeads,
        'renderTable' : renderTable,

    }
    return render(request, 'page_app/index.html', context) 


def newLead(request):
    # create new lead here
    if request.method == "POST":
        newLead = Lead.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])

    renderTable = []
    allLeads = Lead.objects.all()

    for i in range(5):
        renderTable.append(allLeads[i])


    context = {
        'all_leads' : allLeads,
        'renderTable' : renderTable,
    }
    return render(request, 'page_app/partials/table.html', context)


def pagination(request, page):
    renderTable = []
    pageIt = page * 5
    allLeads = Lead.objects.all()

    for i in range(5):
        renderTable.append(allLeads[(pageIt - 5) + i ])
    

    context = {
        'all_leads' : allLeads,
        'renderTable' : renderTable,
    }
    return render(request, 'page_app/partials/table.html', context)



