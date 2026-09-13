from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation, Inquiry, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm
from django.shortcuts import render, redirect 
from django.views.generic import ListView

def home(request):
    return render(request, "main/index.html")

def about(request):
    personal = PersonalInformation.objects.first()
    return render(request, "main/about.html", {"personal": personal})

def contact(request):
    personal = PersonalInformation.objects.first()

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = InquiryForm()
    return render(request, 'main/contact.html', {"personal": personal, "form": form})

def projects(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects": projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "main/project_detail.html", {"project": project})

def adding_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")
    else:
        form = ProjectForm()
    return render(request, "main/adding_project.html", {"form": form})

def add_testimony(request):
    if request.method == "POST":
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testimony_list")
    else:
        form = TestimonyForm()

    return render(request, "main/add_testimony.html", {"form": form})

class TestimonyListView(ListView):
    model = Testimony
    template_name = "main/testimony_list.html" 
    context_object_name = "testimonies"

def testimony_detail(request, testimony_id):
    testimony = get_object_or_404(Testimony, id=testimony_id)
    return render(request, "main/testimony_detail.html", {"testimony": testimony})