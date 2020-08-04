from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField()
    active = models.BooleanField(default=False)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class std(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    n_friends = models.IntegerField()
    n_brother = models.IntegerField()

    def __str__(self):
        return str(self.user)
