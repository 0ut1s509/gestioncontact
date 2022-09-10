from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('add-contact/', views.add_contact, name = 'add_contact'),
    path('mod-contact/<str:non>', views.mod_contact, name = 'mod_contact'),
    path('search-contact/<str:non>', views.search_contact, name = 'search_contact'),
    path('list-contact/', views.list_contact, name = 'list_contact'),
    path('search/', views.search, name = 'search'),




]
