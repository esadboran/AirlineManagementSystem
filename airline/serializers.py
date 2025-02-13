import random
import string
import uuid
from rest_framework import serializers
from .models import Airplane, Flight, Reservation
import datetime

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

    def validate_tail_number(self, value):
        if not value:
            raise serializers.ValidationError("Tail number zorunludur.")
        if not value.isalnum():
            raise serializers.ValidationError("Tail number sadece harf ve rakam içermelidir.")
        return value

    def validate_model(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Model adı en az 3 karakter olmalıdır.")
        return value

    def validate_capacity(self, value):
        if value < 1:
            raise serializers.ValidationError("Kapasite en az 1 olmalıdır.")
        return value

    def validate_production_year(self, value):
        """Üretim yılı 1900  ile bugünkü yıl arasında olmalıdır."""
        current_year = datetime.datetime.now().year
        if value < 1903 or value > current_year:
            raise serializers.ValidationError(f"Üretim yılı 1900 ile {current_year} arasında olmalıdır.")
        return value


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(self, value):
        if not value:
            raise serializers.ValidationError("Uçuş numarası zorunludur.")
        return value

    def validate_departure(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Kalkış noktası en az 3 karakter olmalıdır.")
        return value

    def validate_destination(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Varış noktası en az 3 karakter olmalıdır.")
        if value == self.initial_data.get('departure'):
            raise serializers.ValidationError("Kalkış ve varış noktaları aynı olamaz.")
        return value

    def validate_departure_time(self, value):
        if value <= datetime.datetime.now():
            raise serializers.ValidationError("Kalkış zamanı bugünden sonra olmalıdır.")
        return value

    def validate(self, data):
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')

        if departure_time and arrival_time and arrival_time <= departure_time:
            raise serializers.ValidationError({"arrival_time": "Varış zamanı kalkıştan sonra olmalıdır."})

        return data


class ReservationSerializer(serializers.ModelSerializer):
    reservation_code = serializers.ReadOnlyField()

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate_passenger_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Yolcu adı en az 3 karakter olmalıdır.")
        return value

    def validate_passenger_email(self, value):
        if "@" not in value or "." not in value:
            raise serializers.ValidationError("Geçerli bir e-posta adresi giriniz.")
        return value

    def validate_flight(self, flight):
        if flight.reservations.count() >= flight.airplane.capacity:
            raise serializers.ValidationError("Bu uçuşun kapasitesi dolu!")
        return flight

    def validate_status(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Rezervasyon durumu True veya False olmalıdır.")
        return value

    def create(self, validated_data):
        validated_data['reservation_code'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        reservation = super().create(validated_data)
        return reservation
