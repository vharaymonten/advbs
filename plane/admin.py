from django.contrib import admin

from plane.models import AgeGroup, Airline, Booking, BookingDetail, City, Departure, Flight, FlightType, Meal, MealType, Pessanger, PessangerCredit, SeatType, Service, Ticket

# Register your models here.
admin.site.register(AgeGroup)
admin.site.register(City)
admin.site.register(Meal)
admin.site.register(MealType)
admin.site.register(Airline)
admin.site.register(Pessanger)
admin.site.register(Service)
admin.site.register(Flight)
admin.site.register(FlightType)
admin.site.register(SeatType)
admin.site.register(Booking)
admin.site.register(BookingDetail)
admin.site.register(Departure)
admin.site.register(Ticket)
admin.site.register(PessangerCredit)