from django.db import models

# Create your models here.

class Blogs(models.Model):
    name = models.CharField(max_length = 255, null = False)
    

    class Meta:
        verbose_name = 'BlogsList'
        verbose_name_plural = 'BlogsLists'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)


class Blog(models.Model):
    Title = models.CharField(max_length = 255, null = False)
    Description = models.CharField(max_length = 255, null = False)
    Owner = models.CharField(max_length = 255, null = True)
    blog_list = models.ForeignKey(Blogs, null = True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogers'
    
    def __str__(self):
        return 'ID: {}, Name:',format(self.id, self.name)