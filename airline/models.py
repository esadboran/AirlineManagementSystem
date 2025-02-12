from django.db import models
import uuid

class Airplane(models.Model):
    tail_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tail_number} - {self.model}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField(db_index=True)
    arrival_time = models.DateTimeField(db_index=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")

    def __str__(self):
        return f"{self.flight_number}: {self.departure} -> {self.destination}"

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper())
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.reservation_code}"

