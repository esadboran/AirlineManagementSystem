from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .filters import AirplaneFilter, FlightFilter, ReservationFilter
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AirplaneFilter

    @action(detail=True, methods=['get'])
    def flights(self, request, pk=None):
        airplane = self.get_object()
        flights = Flight.objects.filter(airplane=airplane)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class =  FlightFilter

    @action(detail=True, methods=['get'])
    def reservations(self, request, pk=None):
        flight = self.get_object()
        reservations = Reservation.objects.filter(flight=flight)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response



