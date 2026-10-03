from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation, Inquiry, Testimony, Techstack
from .forms import ProjectForm, InquiryForm, TestimonyForm, CreateProjectForm, CreateTechstackForm
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
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

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")
        else:
            error_message = "Invalid credentials or not an admin."
            return render(request, "main/admin_login.html", {"error_message": error_message})
    return render(request, "main/admin_login.html")

def admin_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect("sign_in")

def dashboard(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("admin_login")

    projects = Project.objects.all()
    inquiries = Inquiry.objects.all()
    testimonies = Testimony.objects.all()
    techstacks = Techstack.objects.all()

    return render(request, "main/dashboard.html", {
        "projects": projects,
        "inquiries": inquiries,
        "testimonies": testimonies,
        "techstacks": techstacks
    })

def dashboard_projects(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("admin_login")

    projects = Project.objects.all()
    return render(request, "main/dashboard_projects.html", {"projects": projects})

def dashboard_techstacks(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("admin_login")

    techstacks = Techstack.objects.all()
    return render(request, "main/dashboard_techstacks.html", {"techstacks": techstacks})

def create_project(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("admin_login")

    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_projects")
    else:
        form = CreateProjectForm()

    return render(request, "main/create_project.html", {"form": form})

def create_techstack(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("admin_login")

    if request.method == "POST":
        form = CreateTechstackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_techstacks")
    else:
        form = CreateTechstackForm()

    return render(request, "main/create_techstack.html", {"form": form})