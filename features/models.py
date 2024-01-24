


from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class SocietyMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    is_approved = models.BooleanField(default=False)  

    def __str__(self):
        return self.full_name

@receiver(post_save, sender=User)
def create_society_member(sender, instance, created, **kwargs):
    if created:
        SocietyMember.objects.create(user=instance)

@receiver(post_save, sender=SocietyMember)
def create_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create(username=instance.user.username, email=instance.email)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    created_by = models.ForeignKey(SocietyMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(SocietyMember, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    posted_by = models.ForeignKey(SocietyMember, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    related_announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.related_announcement.title}"
