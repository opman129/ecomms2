from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save

from django.utils.text import slugify
# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Cinema(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=False, null=True, default=1)
    title   = models.CharField(max_length=120, blank=False)
    image   = models.ImageField(upload_to=upload_location,
        null=True, 
        blank=True, 
        width_field="width_field",
        height_field="height_field")
    height_field =models.IntegerField(default=0)
    width_field =models.IntegerField(default=0)
    content = models.TextField()
    draft   = models.BooleanField(default=False)
    published = models.DateField(auto_now=False, auto_now_add=False)
    active  = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("cinema:cinema-detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

#def pre_save_post_receiver(sender, instance, *args, **kwargs):
 #   slug = slugify(instance.title)
  #  exits = Post.objects.filter(slug=slug).exists()
   # if exists:
    #    slug = "%s=%s" %(slugify(instance.title), instanceid)
    #instance.slug = slug


#pre_save.connect(pre_save_post_receiver, sender=Post)