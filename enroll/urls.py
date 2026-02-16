from django.urls import path
from enroll import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update/<int:id>", views.update, name="update_data"),
    path("delete/<int:id>", views.delete, name="deletedata")
]


