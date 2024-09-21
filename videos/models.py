from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='media/video_files', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov'])])
    video_thumbnail = models.FileField(upload_to='media/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['png','jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)



    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
    
