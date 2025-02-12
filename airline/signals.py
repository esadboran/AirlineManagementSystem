from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Reservation

@receiver(post_save, sender=Reservation)
def send_reservation_email(sender, instance, created, **kwargs):
    if created:
        flight = instance.flight
        passenger_name = instance.passenger_name
        passenger_email = instance.passenger_email
        reservation_code = instance.reservation_code

        subject = 'Rezervasyon Onaylandı!'
        message = f"""
        Merhaba {passenger_name},

        {reservation_code} kodlu rezervasyonunuz başarıyla oluşturuldu!

        Uçuş Numarası: {flight.flight_number}
        Kalkış: {flight.departure}
        Varış: {flight.destination}
        Kalkış Saati: {flight.departure_time}

        İyi yolculuklar dileriz!
        """

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [passenger_email]

        send_mail(subject, message, from_email, recipient_list)
