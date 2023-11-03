from django.contrib import admin
from .models import Category, JobApplication, Jobs

class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_category_name', 'job_description', 'job_location', 'job_experience', 'job_salary')

    def job_category_name(self, obj):
        return obj.job_category.categoryname
    job_category_name.short_description = 'Job Category'

admin.site.register(Category)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(JobApplication)



