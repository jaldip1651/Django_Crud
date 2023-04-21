from django.db import models


# Create your models here.
class User(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'usermaster'


class salary(models.Model):
    userid = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(null=True, blank=True)
    pf = models.CharField(max_length=100)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'app1_salary'
