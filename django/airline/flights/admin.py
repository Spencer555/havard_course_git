from django.contrib import admin
from .models import Flight, Airport, Passanger

# Register your models here.
# customize ur admin
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passanger, PassengerAdmin)