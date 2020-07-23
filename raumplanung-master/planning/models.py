from django.db import models
from django.contrib.auth.models import User
from datetime import date as pydate, time

# Anlegen der Models zur Datenhaltung
# Entgegen der ursprünglichen Planung werden Foreign Keys zur Referenzierung auf andere Objekte verwendet
# um nicht manuell über die Felder die zugehörigen Objekte suchen zu müssen
# from planning.models import User, Space, Calendar, Timeslot, BookingTime, BookedRoom, Booking


# User Model
# class User(models.Model):
#    username = models.CharField(max_length=50)
#    password = models.CharField(max_length=50)
#    email = models.CharField(max_length=50)
#    admin = models.BooleanField()


# Spaces Model
class Space(models.Model):
    title = models.CharField(max_length=50)
    size = models.IntegerField()
    equipment = models.CharField(max_length=300)

    def __str__(self):
        return '{}'.format(self.title)


# Calendar Model
class Calendar(models.Model):
    date = models.DateField()

    def __str__(self):
        return '{}'.format(pydate.strftime(self.date, '%d.%m.%Y'))


# Timeslot Model
class Timeslot(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return '{} bis {}'.format(time.strftime(self.start, '%H:%M'), time.strftime(self.end, '%H:%M'))


# BookingTime Model
# class BookingTime(models.Model):
#    date = models.ForeignKey(Calendar, models.CASCADE)  # Referenz auf das Kalenderdatum
#    slot = models.ForeignKey(Timeslot, models.CASCADE)  # Referent auf den Timeslot


# BookedRoom Model
class Booking(models.Model):
    space = models.ForeignKey(Space, models.CASCADE, default=0)  # Referenz auf den betroffenen Raum
    # bookingTime = models.ForeignKey(BookingTime, models.CASCADE)
    date = models.ForeignKey(Calendar, models.CASCADE, default=0)  # Referenz auf das Kalenderdatum
    slot = models.ForeignKey(Timeslot, models.CASCADE, default=0)  # Referent auf den Timeslot
    user = models.ForeignKey(User, models.CASCADE, default=0)  # Referenz auf den User der die Buchung getätigt hat.

    def __str__(self):
        return '{}: {}, {} ({})'.format(self.space, self.date, self.slot, self.user)


# Booking Model
# class Booking(models.Model):
#    user = models.ForeignKey(User, models.CASCADE)  # Referenz auf den User der die Buchung getätigt hat.
#    bookedRoom = models.ForeignKey(BookedRoom, models.CASCADE)  # Referenz auf die

