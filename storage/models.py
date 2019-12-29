from django.db import models

# Create your models here.

class Storage(models.Model):
	key = models.CharField(max_length=10,blank=True, null=True)
	value = models.CharField(max_length=10,blank=True, null=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Storage'
		app_label = 'storage'
		db_table = 'key_value_storage'

	def __str__(self):
		return 'key :' + self.key + 'value: ' + self.value \
			   + 'updated on ' + self.updated_at.strftime('%Y-%m-%d')
