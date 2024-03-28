from django.urls import path
from .views import Smart

urlpatterns = [
    path("get/<int:pk>",Smart.as_view()),
    path("getall/",Smart.as_view()),
    path("add/",Smart.as_view()),
    path("delete/",Smart.as_view())
]
