from django.db import models



class Category(models.Model):
    categoryid = models.IntegerField()
    categoryname = models.CharField(max_length=100)

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_experience = models.CharField(max_length=100)
    job_salary = models.CharField(max_length=100)

class JobApplication(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    address = models.TextField()
    skills = models.TextField()
    cv = models.FileField(upload_to='cv_uploads/')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='applications_for_job')
    
    def __str__(self):
        return f"Application by {self.name} for {self.job.job_title} in {self.job.job_category.categoryname}"
    
    