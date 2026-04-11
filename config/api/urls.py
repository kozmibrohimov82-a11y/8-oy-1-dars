from django.urls import path
from .views import *
urlpatterns=[
    path('cars/',CarPostGet.as_view(),name='cars'),
    path('cars/<int:car_id>/',CarUpdateDelete.as_view(),name='cars'),
    path('categories/',CategoryListView.as_view(),name='categories'),
    path('categories/<int:pk>/',CategoryUpdateView.as_view(),name='categories'),

]