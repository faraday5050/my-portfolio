from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(max_length=300)
    full_description = models.TextField()
    
    # Images
    main_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    extra_image_1 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    extra_image_2 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    extra_image_3 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    extra_image_4 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    
    # Technical Details
    technologies = models.CharField(max_length=500)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    
    # Results
    key_results = models.TextField(blank=True)
    
    # Detailed Sections
    problem_statement = models.TextField(blank=True)
    business_value = models.TextField(blank=True)
    data_source_preprocessing = models.TextField(blank=True)
    limitations_future = models.TextField(blank=True)
    
    # Model Metrics
    metrics_mae = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metrics_rmse = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metrics_r2 = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    metrics_mape = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metrics_precision = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    metrics_recall = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    metrics_f1 = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    metrics_dataset_size = models.IntegerField(blank=True, null=True)
    metrics_training_date = models.DateField(blank=True, null=True)
    
    # GitHub Stats
    github_stars = models.IntegerField(default=0)
    github_forks = models.IntegerField(default=0)
    show_github_badge = models.BooleanField(default=True)
    
    # Dataset Information
    dataset_name = models.CharField(max_length=200, blank=True)
    dataset_source = models.CharField(max_length=200, blank=True)
    dataset_size = models.CharField(max_length=100, blank=True)
    dataset_link = models.URLField(blank=True)
    data_quality_issues = models.TextField(blank=True)
    cleaning_steps = models.TextField(blank=True)
    
    # API/Production Info
    api_endpoint = models.URLField(blank=True)
    api_documentation = models.URLField(blank=True)
    containerized = models.BooleanField(default=False)
    docker_repo = models.URLField(blank=True)
    deployment_platform = models.CharField(max_length=100, blank=True)
    
    # Status
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Certification(models.Model):
    title = models.CharField(max_length=200, help_text='Name of the certification')
    issuing_organization = models.CharField(max_length=200, help_text='Who issued the certificate')
    issue_date = models.DateField(help_text='Date the certification was earned')
    expiry_date = models.DateField(blank=True, null=True, help_text='Leave blank if no expiry')
    credential_id = models.CharField(max_length=100, blank=True, help_text='Certificate ID/License number')
    credential_url = models.URLField(blank=True, help_text='Link to verify the certificate online')
    certificate_image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    description = models.TextField(blank=True, help_text='Brief description of what you learned')
    skills_covered = models.CharField(max_length=500, blank=True, help_text='Comma-separated skills')
    display_order = models.IntegerField(default=0, help_text='Lower numbers appear first')
    is_published = models.BooleanField(default=True, help_text='Show on portfolio')
    
    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"
    
    class Meta:
        ordering = ['display_order', '-issue_date']
        verbose_name_plural = "Certifications"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(max_length=300)
    content = models.TextField()
    
    # Images
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Main blog image')
    extra_image_1 = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Additional image 1')
    extra_image_2 = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Additional image 2')
    extra_image_3 = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Additional image 3')
    extra_image_4 = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Additional image 4')
    extra_image_5 = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Additional image 5')
    
    tags = models.CharField(max_length=200, blank=True)
    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    read_time = models.IntegerField(default=5)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']


class Profile(models.Model):
    name = models.CharField(max_length=200, default='Yahaya Eneojo Michael')
    title = models.CharField(max_length=200, default='Data Science & Machine Learning Engineer')
    bio = models.TextField(default='ML Engineer specializing in predictive modeling, anomaly detection, ETL pipelines, and business intelligence')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default='michaelyahaya442@gmail.com')
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    show_hobbies_section = models.BooleanField(default=True)
    hobbies_footer_text = models.CharField(max_length=500, blank=True, default='🎵 Music & Arts · 📚 Reading & Learning · 🏋️ Fitness & Wellness · ☕ Coffee & Conversations')
    
    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    show_blog_section = models.BooleanField(default=True)
    show_metrics_section = models.BooleanField(default=True)
    show_dataset_section = models.BooleanField(default=True)
    show_api_section = models.BooleanField(default=True)
    
    def __str__(self):
        return "Site Settings"
    
    class Meta:
        verbose_name_plural = "Site Settings"