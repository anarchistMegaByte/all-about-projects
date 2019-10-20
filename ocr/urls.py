from django.urls import path
from ocr import views

urlpatterns = [
	path("test_score/", views.test_score)
]