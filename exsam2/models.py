from django.db import models

class TexnikShart(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='texnikshart_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
