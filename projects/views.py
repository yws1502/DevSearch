from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':project_obj})

def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project':project}
    return render(request, 'projects/delete_template.html', context)