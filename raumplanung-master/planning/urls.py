from django.urls import path

from . import views

app_name = 'planning'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_bookings', views.all_bookings, name='all_bookings'),
    path('space/<int:space_id>/', views.space, name='space'),
    path('space/<int:space_id>/<int:date_id>/<int:slot_id>/book/', views.book_space, name='book_space'),

]