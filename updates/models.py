from django.conf import settings
from django.db import models

def upload_update_img(instance, filename):
    return "update/{user}/{filename}".format(user=instance.user, filename =filename)

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField (blank=True, null= True)
    #image = models.ImageField(upload_to = upload_update_img , blank= True, null =True)
    Updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.content or ""