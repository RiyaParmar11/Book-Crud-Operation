from django.urls import path
from . import views

urlpatterns = [
     path('', views.main),
     path('add/', views.add),
     path('delete/<int:id>', views.delete),
     path('update/<int:id>', views.update),
     path('show/<int:id>', views.show)
]