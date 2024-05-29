from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# global var
tasks = ["foo", "bar", "baz"]

def index(request):
    # if tasks not in sessions add it to session
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {"tasks":request.session["tasks"]})


class NewTaskForm(forms.Form):
    tasks = forms.CharField(label='new task')
    priority = forms.IntegerField(label='priority', min_value=1, max_value=10)
    

def add(request):
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse('tasks:index', ))
            
        else:
            return render(request, 'tasks/add.html', {
        "form":form
    })
    return render(request, 'tasks/add.html', {
    "form":NewTaskForm()
})