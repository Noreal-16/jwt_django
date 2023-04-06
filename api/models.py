from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '{0},{1}'.format(self.last_name, self.name)
