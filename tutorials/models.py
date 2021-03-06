from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True)

    def save_profile(self):
        self.save()                   

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'        

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tutorials(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=150)
    tutorial_image = CloudinaryField('images')    
    tutorial_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
          
    def save_tutorial(self):
        self.save()
    
    def delete_tutorial(self):
        self.delete()
        
    @classmethod
    def get_tutorials(cls):
        tutorials = cls.objects.all()
        return tutorials
    
    @classmethod
    def search_tutorials(cls, search_term):
        tutorials = cls.objects.filter(title__icontains=search_term)
        return tutorials
    
    
    @classmethod
    def get_by_author(cls, author):
        tutorials = cls.objects.filter(author=author)
        return tutorials
    
    
    @classmethod
    def get_tutorial(request, id):
        try:
            tutorial = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return tutorial
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Tutorial'
        verbose_name_plural = 'Tutorials'