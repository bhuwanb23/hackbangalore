from django.db import models

class Innovator(models.Model):
    first_name = models.CharField(max_length=50,default=0)
    last_name = models.CharField(max_length=50,default=1)
    username = models.CharField(primary_key=True,unique=True, max_length=50,default=0)
    password = models.CharField(max_length=50,default=0)
    age = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to='home/project_image/innovation_image', blank=True, null=True)
    email = models.EmailField(unique=True,default=0)
    contact_number = models.BigIntegerField(default=123456789)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    project_list = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    no_of_projects = models.PositiveIntegerField(blank=True, null=True)
    desc = models.CharField(max_length=500,default=None)
    education = models.CharField(max_length=100,default=None)
    professional_history = models.CharField(max_length=500,default=None)
    interest = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.username

class Investor(models.Model):
    first_name = models.CharField(max_length=50,default=0)
    last_name = models.CharField(max_length=50,default=0)
    username = models.CharField(primary_key=True,unique=True, max_length=50)
    password = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='home/project_image/investor_image')
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,default='2001-01-01')
    email = models.EmailField(unique=True,default=0)
    contact_number = models.BigIntegerField(default=1112223333)
    project_list = models.ManyToManyField('Project', related_name='investors')
    address = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Project(models.Model):
    PROJECT_FUNDING_TYPES = [
        (1, 'Equity'),
        (2, 'Debt'),
        (3, 'Donation'),
        (4, 'Reward'),
    ]
    project_id = models.CharField(primary_key=True,unique=True, max_length=50,default=None)
    project_name = models.CharField(max_length=200)
    owner_username = models.CharField(max_length=50,default=None)
    description = models.CharField(max_length=500,default=None)
    funding_goal = models.DecimalField(max_digits=8, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=8, decimal_places=2, default='0')
    number_of_investors = models.PositiveSmallIntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    owner = models.CharField(max_length=50)
    is_sdg = models.BooleanField(default=False)  # is it a Sustainable Development Goal project?
    partner = models.CharField(max_length=200)
    images_1 = models.ImageField(upload_to='home/project_images', blank=True, null=True, max_length=255)
    images_2 = models.ImageField(upload_to='home/project_images', blank=True, null=True, max_length=255)
    images_3 = models.ImageField(upload_to='home/project_images', blank=True, null=True, max_length=255)
    images_4 = models.ImageField(upload_to='home/project_images', blank=True, null=True, max_length=255)
    video = models.FileField(upload_to='home/project_videos', blank=True, null=True, max_length=255)
    funding_type = models.IntegerField(choices=PROJECT_FUNDING_TYPES, default=1)

    def __str__(self):
        return self.project_name
