from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('dojos', views.index, name='dojos'),
    path('add_ninja', views.add_ninja, name='add_ninja'),
    path('show_ninjas/<int:dojo_id>', views.show_ninjas, name='show_ninjas'),
    path('create_dojo', views.create_dojo, name='create_dojo'),
    path('create_ninja', views.create_ninja, name='create_ninja'),
]