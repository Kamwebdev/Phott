from django.db import models
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

def make_thumbnail(image, size=(100, 100)):
    im = Image.open(image)
    im.convert('RGB') # convert mode
    im.thumbnail(size) # resize image
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'JPEG', quality=85) # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name) # create a django friendly File object
    return thumbnail

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)
    image = ResizedImageField(size=[1200, 1200], quality=95, upload_to='photos')
    thumb = models.ImageField(upload_to='thumb', null=True, blank=True)
    top = models.BooleanField(default=True)
    height = models.IntegerField(default=1)
    width = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.thumb = make_thumbnail(self.image, size=(800, 800))
        super(Photo, self).save(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.thumb.url))