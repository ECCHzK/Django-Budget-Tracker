from operator import neg
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BudgetItem
from .forms import AddToBudget
from datetime import date

# Create your views here.

def home(response):
    #Only displays the items associated with the user on the table.
    if response.user.is_authenticated == True:
        it = response.user.budgetitem.all()
        total = 0
        neg = False
        for instance in it:
    #Checks if an item is income or an expense in order to add or subtract from the total.
            if instance.iscost != True:
                total += instance.amount
            else: total -= instance.amount
    #Functionality for the delete button.
        if response.method == 'POST':
            for item in it:
                if response.POST.get('del' + str(item.id)):
                    item.delete()
                    return HttpResponseRedirect('/')
        if total < 0:
            total *= -1
            neg = True
        return render(response, 'main/home.html', {'it':it, 'total':total, 'neg':neg})
    else: return render(response, 'main/home.html', {})

def add(response):
    if response.method == 'POST':
        form = AddToBudget(response.POST)

        if form.is_valid():
            d = form.cleaned_data.get('date')
            #Fills in today's date if the 'Date' field is blank.
            if d is None:
                d = date.today()
            n = form.cleaned_data.get('name')
            a = form.cleaned_data.get('amount')
            c = form.cleaned_data.get('iscost')
            i = BudgetItem(date=d, name=n, amount=a, iscost=c)
            i.save()
            response.user.budgetitem.add(i)
            return HttpResponseRedirect('/')
    else:
        form = AddToBudget()
    return render(response, 'main/add.html', {'form':form})
