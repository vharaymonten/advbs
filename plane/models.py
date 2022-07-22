from operator import mod
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.
class AgeGroup(models.Model):
    name = models.CharField(max_length=10, unique=True)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'age_group'

class City(models.Model):
    code = models.CharField(primary_key=True, max_length=4, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.code + " " + self.name 
    class Meta:
        db_table = "city"

class Meal(models.Model)  :
    name = models.CharField(max_length=255, unique=True)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'meal'
    
class MealType(models.Model):
    type_name = models.CharField(max_length=255, unique=True)
    meal = models.ManyToManyField(Meal)
    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'meal_type'

class Airline(models.Model):
    company_name = models.CharField(max_length=255)
    airline_name = models.CharField(max_length=255, unique=True)
    first_class_seat = models.PositiveIntegerField()
    business_seat = models.PositiveIntegerField()
    premium_seat = models.PositiveIntegerField()
    economy_seat = models.PositiveIntegerField()
    has_max_pessanger = models.BooleanField(default=False)
    
    def __str__(self):
        return self.company_name + "-" + self.airline_name
    class Meta:
        db_table = 'airline'

class Pessanger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()

    class Meta:
        db_table = 'pessanger'

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=255)
    airline = models.ManyToManyField(Airline)
    class Meta:
        db_table = 'service'

    def __str__(self) :
        return self.name

class FlightType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'flight_type'
    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_code = models.CharField(max_length=10)
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    base_price = models.IntegerField()
    is_reserverable = models.BooleanField()
    class Meta:
        db_table = 'flight'
    
    def __str__(self):
        return self.flight_code + '-' + str(self.airline.airline_name) + '-' + str(self.flight_type.name)

class SeatType(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = "seat_type"
    
    def __str__(self) :
        return self.name

class Departure(models.Model):
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    date = models.DateField()
    depart_time = models.TimeField()
    arrive_time = models.TimeField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    flight_duration_m = models.IntegerField()

    class Meta:
        db_table = 'departure'

    def __str__(self):
        return f"{self.origin} - {self.destination}"


class Booking(models.Model):
    booking_date = models.DateField()
    code = models.CharField(max_length=255, unique=True, blank=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE)
    class Meta:
        db_table = 'booking'

    def __str__(self):
        return str(self.id)
    

class BookingDetail(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    pessanger = models.ForeignKey(Pessanger, on_delete=models.PROTECT)
    in_seat = models.BooleanField(default=True)
    seat_type = models.ForeignKey(SeatType, on_delete=models.PROTECT)
    baggage_kg = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    age = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)

    class Meta: 
        db_table = 'booking_detail'

    def __str__(self) :
        return f"{self.booking} - {self.pessanger}"

class Ticket(models.Model):
    status = models.CharField(max_length=255) # RESERVED, CANCELLED, RESCHEADULED
    booking_detail = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ticket'

    def __str__(self):
        return str(self.id)

class PessangerCredit(models.Model):
    pessanger = models.ForeignKey(Pessanger, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    expiry_date = models.DateField()
    class Meta:
        db_table = 'pessanger_credit'
