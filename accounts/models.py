from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
CITY = [ #database , #user
    ("Karthum", "Karthum"),
    ("omdrman", "omdrman"),
    ("bahri", "bahri"),
    ("sharq alnel", "sharq alnel"),
]



class TeacherProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=20)
    educitons = models.TextField(max_length=300, null=True, blank=True)
    exprince = models.TextField(max_length=150, null=True, blank=True)
    number =models.CharField(max_length=12)
    city = models.CharField(max_length=12, choices=CITY)
    tech = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'techer')  
    subject = models.CharField(null=True,blank=True, max_length=20)
    def __str__(self) -> str:
        return f"{str(self.user)} - {self.name}"
class Oder(models.Model):
    name = models.CharField(max_length = 20)
    number = models.CharField(max_length = 15)
    number2 = models.CharField(max_length = 15)
    date = models.DateTimeField()
    regin = models.CharField(max_length = 20)
    city = models.CharField(max_length=12, choices=CITY)
    techer = models.ForeignKey(TeacherProfile , models.SET_NULL , null = True , blank = True)
    def __str__(self) -> str:
        return f"oder to {str(self.techer)} from {self.name}"
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)
