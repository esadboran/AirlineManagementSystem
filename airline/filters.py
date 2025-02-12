import django_filters
from .models import Airplane, Flight, Reservation


class AirplaneFilter(django_filters.FilterSet):
    tail_number = django_filters.CharFilter(lookup_expr='icontains')
    model = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.BooleanFilter(field_name='status')

    production_year_from = django_filters.NumberFilter(field_name='production_year', lookup_expr='gte')
    production_year_to = django_filters.NumberFilter(field_name='production_year', lookup_expr='lte')

    capacity_from = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    capacity_to = django_filters.NumberFilter(field_name='capacity', lookup_expr='lte')

    class Meta:
        model = Airplane
        fields = ['tail_number', 'model', 'status', 'production_year', 'capacity']


class FlightFilter(django_filters.FilterSet):
    flight_number = django_filters.CharFilter(field_name="flight_number", lookup_expr='icontains')
    departure = django_filters.CharFilter(lookup_expr='icontains')
    destination = django_filters.CharFilter(lookup_expr='icontains')

    departure_time_from = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='gte')
    departure_time_to = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='lte')

    arrival_time_from = django_filters.DateTimeFilter(field_name='arrival_time', lookup_expr='gte')
    arrival_time_to = django_filters.DateTimeFilter(field_name='arrival_time', lookup_expr='lte')

    airplane = django_filters.ModelChoiceFilter(queryset=Airplane.objects.all(), field_name='airplane')

    class Meta:
        model = Flight
        fields = ['flight_number', 'departure', 'destination', 'departure_time', 'arrival_time', 'airplane']


class ReservationFilter(django_filters.FilterSet):
    passenger_name = django_filters.CharFilter(lookup_expr='icontains')
    passenger_email = django_filters.CharFilter(lookup_expr='icontains')
    flight = django_filters.NumberFilter(field_name='flight__id')
    status = django_filters.BooleanFilter()
    reservation_code = django_filters.CharFilter(lookup_expr='iexact')

    created_at_from = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Reservation
        fields = ['passenger_name', 'passenger_email', 'flight', 'status', 'reservation_code', 'created_at']
