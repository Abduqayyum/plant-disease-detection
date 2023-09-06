from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="images", null=False, blank=False)
    prediction = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)


