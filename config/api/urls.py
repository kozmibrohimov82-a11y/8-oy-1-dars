from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns=[
    path('cars/',CarPostGet.as_view(),name='cars'),
    path('cars/<int:car_id>/',CarUpdateDelete.as_view(),name='cars'),
    path('categories/',CategoryListView.as_view(),name='categories'),
    path('categories/<int:pk>/',CategoryUpdateView.as_view(),name='categories'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/',RegisterView.as_view(),name='register'),

]