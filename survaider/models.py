from django.db import models

class Adults(models.Model):
    age=models.IntegerField(db_index=True,default=None)
    work=models.CharField(db_index=True,max_length=200,default=None)
    fnlwgt=models.IntegerField(db_index=True,default=None)
    education=models.CharField(db_index=True,max_length=200,default=None)
    education_num=models.IntegerField(db_index=True,default=None)
    martial_status=models.CharField(db_index=True,max_length=200,default=None)
    occupation=models.CharField(db_index=True,max_length=200,default=None)
    relationship=models.CharField(db_index=True,max_length=200,default=None)
    race=models.CharField(db_index=True,max_length=200,default=None)
    sex=models.CharField(db_index=True,max_length=200,default=None)
    capital_gain=models.IntegerField(db_index=True,default=None)
    capital_loss=models.IntegerField(db_index=True,default=None)
    hours_per_week=models.IntegerField(db_index=True,default=None)
    native_country=models.CharField(db_index=True,max_length=200,default=None)
    salary=models.CharField(db_index=True,max_length=200,default=None)

    def __str__(self):
        return self.occupation

class Adultdata(models.Model):
    age=models.IntegerField(db_index=True,default=None)
    work=models.CharField(db_index=True,max_length=200,default=None)
    fnlwgt=models.IntegerField(db_index=True,default=None)
    education=models.CharField(db_index=True,max_length=200,default=None)
    education_num=models.IntegerField(db_index=True,default=None)
    martial_status=models.CharField(db_index=True,max_length=200,default=None)
    occupation=models.CharField(db_index=True,max_length=200,default=None)
    relationship=models.CharField(db_index=True,max_length=200,default=None)
    race=models.CharField(db_index=True,max_length=200,default=None)
    sex=models.CharField(db_index=True,max_length=200,default=None)
    capital_gain=models.IntegerField(db_index=True,default=None)
    capital_loss=models.IntegerField(db_index=True,default=None)
    hours_per_week=models.IntegerField(db_index=True,default=None)
    native_country=models.CharField(db_index=True,max_length=200,default=None)
    salary=models.CharField(db_index=True,max_length=200,default=None)

    def __str__(self):
        return self.occupation






