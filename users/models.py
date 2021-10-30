from django.db import models

# Create your models here.
class userm(models.Model):
    username = models.CharField(max_length=255,unique=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    adhaar_number= models.IntegerField()
    isadmin = models.BooleanField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_anonymous(self):
        return False
    @property
    def is_authenticated(self):
        return False

    




