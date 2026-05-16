from django.shortcuts import render
from .forms import ProjectForm
from .models import Project

# Create your views here.
def project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm()
    

    return render(request, 'project.html', {'form': form})

def show_projects(request):

    data = Project.objects.all()

    return render(request, 'project_view.html', {'data': data})
