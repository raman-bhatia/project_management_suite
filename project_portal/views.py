from django.shortcuts import render, redirect
from .models import Project
from django.db.models import Q, F
from .forms import ProjectForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .utils import get_current_date

def project_submission(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_submission.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects, 'today_date': get_current_date()})

def home_view(request):
    projects = Project.objects.all()
    query = request.GET.get('q')
    now = timezone.now()
    active_only = request.GET.get('active_only')
    
    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(details__icontains=query) |
            Q(capabilities_needed__icontains=query) |
            Q(disease_area__icontains=query) |
            Q(study_type__icontains=query) |
            Q(submitted_by__icontains=query)
        ).distinct()
    if active_only:
        projects = projects.filter(
            Q(start_date__lte=now) & Q(end_date__gte=now)
        )    
    context = {
        'projects': projects,
        'query': query,
        'active_only': active_only
    }
    return render(request, 'project_list.html', context)

def project_search(request):
    query = request.GET.get('q')
    projects = Project.objects.filter(title__icontains=query)
    return render(request, 'project_search.html', {'projects': projects})

def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {'project': project}
    return render(request, 'project_detail.html', context)

