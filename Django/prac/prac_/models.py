from django.db import models

class Images(models.Model):
    sno=models.AutoField
    images=models.ImageField(upload_to="media/img/",default='')

    def __str__(self):
        split_str=str(self.images).split('.')
        return split_str[0]

# class To_image(models.Model):
#     sno=models.AutoField
#     images=models.CharField(max_length=100,default=' ')

    
class Contact(models.Model):
    name=models.CharField(max_length=20,default=' ')
    phone=models.IntegerField(default=' ')
    mail=models.CharField(max_length=100,default=' ')
    message=models.CharField(max_length=200,default=' ')

    def __str__(self):
        return self.name 
