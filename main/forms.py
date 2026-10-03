from django import forms
from .models import Project, Inquiry, Testimony, Techstack

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = "__all__"


class CreateProjectForm(forms.ModelForm):
    technology_stack = forms.ModelMultipleChoiceField(
        queryset=Techstack.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'technology_stack', 'link']

class CreateTechstackForm(forms.ModelForm):
    class Meta:
        model = Techstack
        fields = ["name"]