
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    #  path("<int:pk>", views.TextView.as_view(), name='view-txt'),
    path("<int:pk>/delete", views.TextDelete.as_view(), name='delete-txt')
]
