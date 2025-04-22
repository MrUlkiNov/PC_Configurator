from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/Configurator', permanent=False)),
    path('Configurator', views.home, name='configurator'),
    path('Processor', views.show_processors, name='processors'),
    path('Processor/<str:name_processor>', views.show_one_processor, name='processor_url'),
    path('Motherboard', views.show_motherboards, name='motherboards'),
    path('Motherboard/<str:name_motherboard>', views.show_one_motherboard, name='motherboard_url'),
    path('Videocard', views.show_videocards, name='videocards'),
    path('Videocard/<str:name_videocard>', views.show_one_videocard, name='videocard_url'),
    path('RAM', views.show_RAMS, name='RAMS'),
    path('RAM/<str:name_ram>', views.show_one_RAM, name='ram_url'),
    path('HDD', views.show_HDD, name='HDDS'),
    path('HDD/<str:name_hdd>', views.show_one_HDD, name='hdd_url'),
    path('Powerblock', views.show_powerblocks, name='powerblocks'),
    path('Powerblock/<str:name_powerblock>', views.show_one_powerblock, name='powerblock_url'),
    path('Cooler', views.show_coolers, name='coolers'),
    path('Cooler/<str:name_cooler>', views.show_one_cooler, name='cooler_url'),
    path('Case', views.show_cases, name='cases'),
    path('Case/<str:name_case>', views.show_one_case, name='case_url'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order_created/', views.order_created, name='order_created'),
]
