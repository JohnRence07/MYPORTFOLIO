from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation 

def home(request):
    return render(request, "main/index.html")

def about(request):
    personal = PersonalInformation.objects.first()
    return render(request, "main/about.html", {"personal": personal})

def contact(request):
    personal = PersonalInformation.objects.first()
    return render(request, 'main/contact.html', {"personal": personal})
    
def projects(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects": projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "main/project_detail.html", {"project": project})