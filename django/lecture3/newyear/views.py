from django.shortcuts import render
import datetime
# Create your views here.
def newyear(request):
    now = datetime.datetime.now()        
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now == 1
    })