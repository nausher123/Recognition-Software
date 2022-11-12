from django.db import models




class ThresholdData(models.Model):
    searchID= models.CharField( max_length= 256)
    subject= models.CharField(max_length=35)
    year= models.IntegerField()
    variant= models.IntegerField()
    z= models.IntegerField()
    a= models.IntegerField()
    b= models.IntegerField()
    c= models.IntegerField()
    d= models.IntegerField()
    e= models.IntegerField()
    u= models.IntegerField()




class ThresholdData1(models.Model):
    searchID= models.CharField( max_length= 256)
    subject= models.CharField(max_length=35)
    year= models.IntegerField()
    variant= models.IntegerField()
    month= models.CharField(max_length=50)
    a= models.IntegerField()
    b= models.IntegerField()
    c= models.IntegerField()
    d= models.IntegerField()
    e= models.IntegerField()
    



class ThresholdData_O(models.Model):
    searchID= models.CharField( max_length= 256)
    subject= models.CharField(max_length=35)
    year= models.IntegerField()
    variant= models.IntegerField()
    month= models.CharField(max_length=50)
    
    a= models.IntegerField()
    b= models.IntegerField()
    c= models.IntegerField()
    d= models.IntegerField()
    e= models.IntegerField()
    





class Sat_Curves(models.Model):
    s_id= models.CharField(max_length=7)
    raw_score_math= models.IntegerField()
    raw_score_read= models.IntegerField()
    raw_score_write=models.IntegerField()
    points_math= models.IntegerField()
    points_read= models.IntegerField()
    points_write= models.IntegerField()



class Sat_Curves1(models.Model):
    s_id= models.CharField(max_length=7)
    raw_score_math= models.IntegerField()
    raw_score_read= models.IntegerField()
    raw_score_write=models.IntegerField()
    points_math= models.IntegerField()
    points_read= models.IntegerField()
    points_write= models.IntegerField()
    

