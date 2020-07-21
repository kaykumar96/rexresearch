from django.db import models
import pytz

# Create your models here.


class Content(models.Model):
    id           = models.AutoField(primary_key=True)
    content_name = models.CharField(max_length=150)
    content_type = models.CharField(max_length=150, null=True, blank=True) 
    status       = models.SmallIntegerField(default=0)
    added_date   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return '%s' % self.content_name 

class ContentDetails(models.Model):
	id              = models.AutoField(primary_key=True)
	content         = models.ForeignKey(Content,on_delete=models.SET_NULL,blank=True,null=True)      
	heading         = models.CharField(max_length=200)
	heading_details = models.TextField(null=True, blank=True)
	file            = models.FileField(upload_to='file/',blank=True,null=True)
	image           = models.ImageField(upload_to='image/',blank=True,null=True)

	class Meta:
		db_table = 'content_details'

	def __str__(self):
		return '%s' % self.heading	
          