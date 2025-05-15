from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Skill, Contact

def home(request):
    projects = Project.objects.all()[:3]  # Pegando os 3 projetos mais recentes
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'skills': skills
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {
        'projects': projects
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {
        'project': project
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('portfolio:contact')
    
    return render(request, 'portfolio/contact.html')