from django.db import models

# Create your models here.

class dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    LOC=models.CharField(max_length=100)

    def __str__(self):
        return self.DNAME

class emp(models.Model):
    DEPTNO=models.ForeignKey(dept,on_delete=models.CASCADE)
    EMPNO=models.IntegerField()
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField(default=None,null=True,blank=True)

    def __str__(self):
        return self.ENAME
