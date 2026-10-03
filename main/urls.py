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

    path("sign-in/", views.admin_login, name="admin_login"),
    path("sign-out/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/projects/", views.dashboard_projects, name="dashboard_projects"),
    path("dashboard/techstacks/", views.dashboard_techstacks, name="dashboard_techstacks"),
    path("dashboard/projects/create/", views.create_project, name="create_project"),
    path("dashboard/techstacks/create/", views.create_techstack, name="create_techstack"),
]
