from django.db import models
from django.contrib.auth.models import User

class Daily(models.Model):
  bt = models.FloatField('体温', max_length=4)
  meal = models.TextField('食事', blank=True)
  sleep = models.TextField('睡眠', blank=True)
  stool = models.TextField('便', blank=True)
  medicine = models.TextField('薬', blank=True)

  OPTION_CHOICES = [
      ('good', '良い'),
      ('normal', '普通'),
      ('bad', '悪い'),
  ]
  mood = models.CharField('機嫌', max_length=10, choices=OPTION_CHOICES)

  contact = models.TextField('家庭での様子', blank=True)

  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "連絡帳"
    verbose_name_plural = "連絡帳"

  def __str__(self):
    return self.created.strftime('%Y-%m-%d')
