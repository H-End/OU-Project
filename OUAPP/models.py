from django.db import models

# Create your models here.
class app_name(models.Model):

    title_logo = models.CharField( max_length = 30 )
    
    class Meta:
        verbose_name = ("app_name")
        verbose_name_plural = ("app_names")

    def __str__(self):
        return self.title_logo

    def get_absolute_url(self):
        return reverse("app_name_detail", kwargs={"pk": self.pk})


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

class search_results(models.Model):

    title_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("search_results_detail", kwargs={"pk": self.pk})
