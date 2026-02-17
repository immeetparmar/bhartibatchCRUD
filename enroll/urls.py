from django.urls import path
from enroll import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("product/<int:id>", views.product_detail, name="product_detail"),
    path("update/<int:id>", views.update, name="update_data"),
    path("delete/<int:id>", views.delete, name="deletedata")
]
