from django.urls import path
from .views import *
urlpatterns=[
    path('cars/',CarView.as_view(),name='cars'),
    path('cars/<int:pk>/',CarView.as_view(),name='cars'),
    path('categories/',CategoryView.as_view(),name='categories'),
    path('categories/<int:pk>/',CategoryView.as_view(),name='categories')
]