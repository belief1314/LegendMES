from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Enterprise(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class Site(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    enterprise=models.ForeignKey(Enterprise)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class ProductLine(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    site=models.ForeignKey(Site)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)


class Document(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    path=models.URLField(max_length=500)
    version=models.IntegerField(max_length=4)
    documentGroup=models.ManyToManyField()
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)


class DocumentGroup(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class Unit(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class Operation(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=20,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    documentGroup=models.ForeignKey(DocumentGroup,verbose_name="Document Group",blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    

class Process(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=20,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    documentGroup=models.ForeignKey(DocumentGroup,verbose_name="Document Group",blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    

class ParameterCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class Parameter(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    unit=models.ForeignKey(Unit)
    minValue=models.CharField(max_length=20,blank=True,null=True,verbose_name="Min Value")
    value=models.CharField(max_length=20,blank=True,null=True)
    maxValue=models.CharField(max_length=20,blank=True,null=True,verbose_name="Max Value")
    parameterGroup=models.ManyToManyField(parameterGroup,verbose_name="Max Value")
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)
    
    
class ParameterGroup(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True,null=True)
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)

    
    
    
class ProcessOperation(models.Model):
    process=models.ForeignKey(Process)
    operation=models.ForeignKey(Operation)
    sequency=models.IntegerField(max_length=4)
    collectionParameterGroup=models.ForeignKey(ParameterGroup,verbose_name="Collection Parameter Group")
    
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)

    
    
class Employee(models.Model):
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    description=models.CharField(max_length=500,blank=True,null=True)
    site=models.ForeignKey(site)
    onboardDate=models.DateTimeField(verbose_name="OnBoard Date")
    
    creator=models.CharField(max_length=20)
    createDate=models.DateTimeField(verbose_name="Create Date")
    modifier=models.CharField(max_length=20,blank=True,null=True)
    modifyDate=models.DateTimeField(verbose_name="Modify Date",blank=True,null=True)