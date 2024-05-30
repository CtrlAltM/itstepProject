from django.urls import path
from .views import views, forms_views


urlpatterns = [
    path("team/", views.team, name="team"),
    path("contact", forms_views.contact_form, name="contact_form"),
    path("lectures/", views.team, name="lectures"),
    path("team/taskdetail/<int:id>/", views.taskdetail, name="details"),
]