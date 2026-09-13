from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path("projects/", views.projects, name="projects"),
    path("projects/add/", views.adding_project, name="adding_project"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),

    path("testimonies/", views.TestimonyListView.as_view(), name="testimony_list"),
    path("testimonies/add/", views.add_testimony, name="add_testimony"),
    path("testimonies/<int:testimony_id>/", views.testimony_detail, name="testimony_detail"),
]
