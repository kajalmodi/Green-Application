from django.db import models

# Create your models here.
class esp11(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    
class esp12(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    
class esp21(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    
class esp22(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    
class esp31(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
  
class esp32(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
  
class esp41(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    pm03 = models.IntegerField(default=0)
    pm05 = models.IntegerField(default=0)
    pm10 = models.IntegerField(default=0)
    pm25 = models.IntegerField(default=0)
    pm50 = models.IntegerField(default=0)
    pm100 = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    temperatureEsp = models.FloatField(default=0)
    soiltempC = models.FloatField(default=0)
    soiltempF = models.FloatField(default=0) 
class esp42(models.Model):
    status = models.IntegerField(default=0)
    moisturevalue = models.FloatField(default=0)
    topic = models.CharField(max_length=40,default='Null')
    