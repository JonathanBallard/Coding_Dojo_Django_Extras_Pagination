from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import LeadForm
import math
 
 
# Create your views here. 

def root(request):
    return redirect('/1')


def index(request, page): 
    entriesOnPage = 3
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
    

    currentPage = page


    maxPages = numPages


    

    if page <= 3:
        minPage = 1
    else:
        minPage = page - 2

    if page >= numPages - 2:
        maxPage = numPages
    else:
        maxPage = page + 2


    firstPage = 1
    lastPage = numPages
    
    context = {
        'lead_form' : form,
        'all_leads' : allLeads,
        'renderTable' : renderTable,
        'numPages' : range(1,numPages),
        'rangeOfPages' : range(minPage,maxPage+1),
        'maxPages' : maxPages,
        'currentPage' : currentPage,
        'firstPage' : firstPage,
        'lastPage' : lastPage,
        'minPage' : minPage,
        'maxPage' : maxPage,

    }
    return render(request, 'page_app/index.html', context) 


def newLead(request):
    entriesOnPage = 3
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
    entriesOnPage = 3
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
    currentPage = page


    maxPages = numPages


    

    if page <= 3:
        minPage = 1
    else:
        minPage = page - 2

    if page >= numPages - 2:
        maxPage = numPages
    else:
        maxPage = page + 2


    firstPage = 1
    lastPage = numPages

    context = {
        'all_leads' : allLeads,
        'renderTable' : renderTable,
        'numPages' : range(1,numPages),
        'rangeOfPages' : range(minPage,maxPage+1),
        'maxPages' : maxPages,
        'currentPage' : currentPage,
        'firstPage' : firstPage,
        'lastPage' : lastPage,
        'minPage' : minPage,
        'maxPage' : maxPage,
    }

    return render(request, 'page_app/partials/table.html', context)



