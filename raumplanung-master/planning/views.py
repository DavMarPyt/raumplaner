from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Space, Calendar, Timeslot, Booking
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    spaces = Space.objects.order_by('title')
    context = {
        'spaces' : spaces
    }
    return render(request, 'planning/index.html', context)


@login_required
def space(request, space_id):
    space = get_object_or_404(Space, pk=space_id)
    dates = Calendar.objects.all().filter(date__gte = date.today()).order_by('date')
    timeslots = Timeslot.objects.order_by('start')

    details = []

    for calendarDate in dates:
        for timeslot in timeslots:
            details.append({
                'date': calendarDate,
                'timeslot': timeslot,
                'booked': len(Booking.objects.all().filter(space=space, date=calendarDate, slot=timeslot)) > 0
            })


    context = {
        'space': space,
        'details': details
    }
    return render(request, 'planning/space.html', context)


@login_required
def book_space(request, space_id, date_id, slot_id):
    space = get_object_or_404(Space, pk=space_id)
    calendarDate = get_object_or_404(Calendar, pk=date_id)
    timeslot = get_object_or_404(Timeslot, pk=slot_id)
    user = request.user
    show_form = True
    existing = Booking.objects.all().filter(user=user, date__date__gte=date.today()).first()
    message = ''

    if request.method == 'POST': # Hier wird geprüft ob das Formular abgesendet wurde.
        show_form = False
        if request.POST['choice'] == 'confirm':
            if len(Booking.objects.all().filter(space=space, date=calendarDate, slot=timeslot)) > 0:
                message = 'Der Raum ist bereits gebucht'
            else:
                if existing is not None:
                    existing.delete()
                booking = Booking(space=space, slot=timeslot, date=calendarDate, user=user)
                booking.save()
                message = 'Raum gebucht!'
        else:
            message = 'Der Raum wurde nicht gebucht'


    context = {
        'message': message,
        'space': space,
        'date': calendarDate,
        'slot': timeslot,
        'existing': existing,
        'show_form': show_form,
    }

    return render(request, 'planning/booking.html', context)


@login_required
def all_bookings(request):
    bookings = Booking.objects.all().filter(date__date__gte=date.today()).order_by('date', 'slot')

    context = {
        'bookings': bookings
    }
    return render(request, 'planning/all_bookings.html', context)