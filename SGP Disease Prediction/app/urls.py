from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('heart/', func1, name='heart'),  # Heart disease page
    path('diabetes/', func2, name='diabetes'),  # Diabetes page
    path('lung_cancer/', lung_cancer_predict, name='lung_cancer'),  # Lung cancer page
    path('predict/', heart_disease_predict, name='heart_disease_predict'),
    path('predict2/', diabetes_predict, name='diabetes_predict'),
    path('contact/', contact, name='contact'),  # Contact page
]

