from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
from PIL import Image
from django.core import validators

def SizeCheck(image):

    img = Image.open(image)
    x, y = img.size
    if x < 500 or y < 500:
        raise ValidationError("Minimum size required. The image size must be at least 500*500 and is actually {0},{1}".format(x, y))
    if img.format != "JPEG" and img.format != "PNG":
        raise ValidationError("Image must be jpeg or png.")
    
class MyImage(models.Model):
        image = models.ImageField(upload_to="img", max_length=None, validators=[SizeCheck])
        date = models.DateTimeField(default=timezone.now)
        verified = models.BooleanField(default=False)
        rejected = models.NullBooleanField(default=None)


