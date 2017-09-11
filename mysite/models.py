# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField

# Create your models here.
class Under_bozhu(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    videos_name = models.CharField(max_length=50)
    videos = models.CharField(max_length=200)
    def __unicode__(self):
        return self.img_name

#博客内容
class Bozhu(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    body = UEditorField(u'文章正文',height=300,width=800,default=u'',blank=True,
                        toolbars="mini",imagePath="aaa/%(basename)s_%(datetime)s.%",
                        filePath="bbb/",
                        )
    pub_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-pub_date',)
    def __unicode__(self):
        return self.title
        

    