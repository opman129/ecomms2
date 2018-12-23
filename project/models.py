from django.urls import reverse

from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=120) #max_length is required
    description = models.TextField(blank=False, null= True)
    price       = models.DecimalField(decimal_places=7,max_digits=10000)
    summary     = models.TextField()
    featured    = models.BooleanField(default = True)    #null=True, default=True


    def get_absolute_url(self):
        return reverse ("project:project-detail", kwargs={"id": self.id}) #f"/project/{self.id}/"