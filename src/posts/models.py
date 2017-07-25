from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title= models.CharField(max_length=120)
    image=models.FileField(null=True,blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp =models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        reverse("posts:detail",kwargs={"id": self.id})
        #return "/post/%s/" %self.id