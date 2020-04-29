from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import LeadForm
import math
 
 
# Create your views here. 
def index(request): 
    entriesOnPage = 10
    form = LeadForm
    renderTable = []
    allLeads = Lead.objects.all()

    numPages = math.ceil(len(allLeads) / entriesOnPage)
    if len(allLeads) % entriesOnPage > 0:
        numPages += 1

    if len(allLeads) > entriesOnPage:
        for i in range(entriesOnPage):
            renderTable.append(allLeads[i])
    elif len(allLeads) < 1 or not len(allLeads):
        renderTable = [
            Lead(first_name="Empty", last_name="User", email="fakeuser@fakeemail.com")
        ]
    else:
        renderTable = allLeads
    
    context = {
        'lead_form' : form,
        'all_leads' : allLeads,
        'renderTable' : renderTable,
        'numPages' : range(1,numPages),

    }
    return render(request, 'page_app/index.html', context) 


def newLead(request):
    entriesOnPage = 10
    # create new lead here
    if request.method == "POST":
        newLead = Lead.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])

    renderTable = []
    allLeads = Lead.objects.all()

    numPages = math.ceil(len(allLeads) / entriesOnPage)
    if len(allLeads) % entriesOnPage > 0:
        numPages += 1

    if len(allLeads) > entriesOnPage:
        for i in range(entriesOnPage):
            renderTable.append(allLeads[i])
    elif len(allLeads) < 1 or not len(allLeads):
        renderTable = [
            Lead(first_name="Empty", last_name="User", email="fakeuser@fakeemail.com")
        ]
    else:
        renderTable = allLeads


    context = {
        'all_leads' : allLeads,
        'renderTable' : renderTable,
        'numPages' : range(1,numPages),
    }
    return render(request, 'page_app/partials/table.html', context)


def pagination(request, page):
    entriesOnPage = 10
    renderTable = []
    allLeads = Lead.objects.all()
    pageAmt = page * entriesOnPage
    pageIt = len(allLeads)


    numPages = math.ceil(len(allLeads) / entriesOnPage)
    if len(allLeads) % entriesOnPage > 0:
        numPages += 1


    if len(allLeads) < pageAmt and len(allLeads) > entriesOnPage:
        for i in range(entriesOnPage): 
            renderTable.append(allLeads[(pageIt - entriesOnPage) + i ])
    elif len(allLeads) >= pageAmt:
        for i in range(entriesOnPage): 
            renderTable.append(allLeads[(pageAmt - entriesOnPage) + i ])
    elif len(allLeads) <= entriesOnPage:
        renderTable = allLeads
    elif len(allLeads) < 1 or not len(allLeads):
        renderTable = [
            Lead(first_name="Empty", last_name="User", email="fakeuser@fakeemail.com")
        ]
    

    context = {
        'all_leads' : allLeads,
        'renderTable' : renderTable,
        'numPages' : range(1,numPages),
    }
    return render(request, 'page_app/partials/table.html', context)



