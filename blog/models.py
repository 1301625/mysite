from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from django.utils import timezone
from django.urls import reverse
# Create your models here.
from account.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account , on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name = 'Title' , help_text = 'Please enter a posting title')
    text = models.TextField(verbose_name='Contents')
    photo = ProcessedImageField(blank=True, upload_to = 'blog/post/%Y' ,processors = [Thumbnail(300,300)],format='JPEG' ,options={'quality': 60})
    created_date= models.DateTimeField(default =timezone.now)
    published_date = models.DateTimeField(blank=True , null=True)
    tags = models.CharField(max_length=100, blank=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])



