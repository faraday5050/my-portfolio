from django.contrib import admin
from .models import Project, Certification, BlogPost, Profile, SiteSettings

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'full_description')
        }),
        ('Images', {
            'fields': ('main_image', 'extra_image_1', 'extra_image_2', 'extra_image_3', 'extra_image_4'),
        }),
        ('Technical Details', {
            'fields': ('technologies', 'github_link', 'live_demo_link')
        }),
        ('Results & Impact', {
            'fields': ('key_results',)
        }),
        ('Problem & Value', {
            'fields': ('problem_statement', 'business_value', 'data_source_preprocessing', 'limitations_future'),
        }),
        ('Model Metrics', {
            'fields': ('metrics_mae', 'metrics_rmse', 'metrics_r2', 'metrics_mape', 'metrics_precision', 'metrics_recall', 'metrics_f1', 'metrics_dataset_size', 'metrics_training_date'),
        }),
        ('GitHub Stats', {
            'fields': ('github_stars', 'github_forks', 'show_github_badge'),
        }),
        ('Dataset Information', {
            'fields': ('dataset_name', 'dataset_source', 'dataset_size', 'dataset_link', 'data_quality_issues', 'cleaning_steps'),
        }),
        ('API & Production', {
            'fields': ('api_endpoint', 'api_documentation', 'containerized', 'docker_repo', 'deployment_platform'),
        }),
        ('Publication', {
            'fields': ('is_published',)
        }),
    )


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date', 'is_published', 'display_order')
    list_filter = ('issuing_organization', 'is_published')
    search_fields = ('title', 'issuing_organization', 'skills_covered')
    list_editable = ('display_order', 'is_published')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'issuing_organization', 'description')
        }),
        ('Dates & ID', {
            'fields': ('issue_date', 'expiry_date', 'credential_id')
        }),
        ('Links & Media', {
            'fields': ('credential_url', 'certificate_image')
        }),
        ('Skills & Display', {
            'fields': ('skills_covered', 'display_order', 'is_published')
        }),
    )


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published', 'read_time')
    list_filter = ('is_published',)
    search_fields = ('title', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'summary', 'content', 'tags', 'read_time', 'is_published')
        }),
        ('Images', {
            'fields': ('featured_image', 'extra_image_1', 'extra_image_2', 'extra_image_3', 'extra_image_4', 'extra_image_5'),
            'description': 'Upload main image and up to 5 additional images'
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'profile_image', 'email')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url')
        }),
        ('Resume', {
            'fields': ('resume_file',),
        }),
        ('Section Controls', {
            'fields': ('show_hobbies_section', 'hobbies_footer_text'),
        }),
    )


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    fieldsets = (
        ('Section Visibility Controls', {
            'fields': ('show_blog_section', 'show_metrics_section', 'show_dataset_section', 'show_api_section'),
        }),
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)