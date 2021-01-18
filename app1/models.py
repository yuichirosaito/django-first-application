from django.db import models

class Touroku(models.Model):

    name = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    
    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name


