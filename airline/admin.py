from django.contrib import admin
from .models import Airplane, Flight, Reservation

class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('tail_number', 'model', 'capacity', 'production_year', 'status')
    search_fields = ('tail_number', 'model')

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure', 'destination', 'departure_time', 'arrival_time', 'airplane')
    search_fields = ('flight_number', 'departure', 'destination')
    list_filter = ('departure', 'destination')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'passenger_email', 'reservation_code', 'flight', 'status', 'created_at')
    search_fields = ('passenger_name', 'passenger_email', 'reservation_code')
    list_filter = ('status', 'flight')

admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Reservation, ReservationAdmin)
