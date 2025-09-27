from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Letter(models.Model):
  title = models.CharField(verbose_name="タイトル", max_length=30)
  content = models.TextField(verbose_name="おたより")

  image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)

  index_main = ImageSpecField(
    source="image",
    processors=[ResizeToFill(540, 360)],
    format="jpeg",
    options={"quality": 80}
  )

  detail_main = ImageSpecField(
    source="image",
    processors=[ResizeToFill(640, 480)],
    format="jpeg",
    options={"quality": 80}
  )

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "おたより"
    verbose_name_plural = "おたより"

  def __str__(self):
    return self.title