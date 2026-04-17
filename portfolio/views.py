from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
from .models import Project, Profile, BlogPost, SiteSettings, Certification

def project_list(request):
    projects = Project.objects.filter(is_published=True)
    profile = Profile.objects.first()
    blog_posts = BlogPost.objects.filter(is_published=True)[:3]
    site_settings = SiteSettings.objects.first()
    certifications = Certification.objects.filter(is_published=True)
    
    return render(request, 'portfolio/project_list.html', {
        'projects': projects,
        'profile': profile,
        'blog_posts': blog_posts,
        'site_settings': site_settings,
        'certifications': certifications,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    profile = Profile.objects.first()
    site_settings = SiteSettings.objects.first()
    
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'profile': profile,
        'site_settings': site_settings,
    })

def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    profile = Profile.objects.first()
    site_settings = SiteSettings.objects.first()
    
    return render(request, 'portfolio/blog_detail.html', {
        'blog_post': blog_post,
        'profile': profile,
        'site_settings': site_settings,
    })

def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            send_mail(
                subject=f'Portfolio Contact from {name}',
                message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['michaelyahaya442@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent! I will get back to you soon.')
        except Exception as e:
            messages.error(request, 'Error sending message. Please email me directly.')
        
        return redirect('/#contact')
    
    return redirect('/')