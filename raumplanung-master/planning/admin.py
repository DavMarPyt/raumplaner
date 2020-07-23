from django.contrib import admin

from .models import Space, Calendar, Timeslot, Booking

# admin.site.register(User)
admin.site.register(Space)
admin.site.register(Calendar)
admin.site.register(Timeslot)
# admin.site.register(BookingTime)
# admin.site.register(BookedRoom),
admin.site.register(Booking)