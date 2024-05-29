from django.db import models
from django.utils import timezone

class Thesis(models.Model):
    callno = models.AutoField(primary_key=True, db_column='callno')
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    adviser = models.CharField(max_length=50)
    abstract = models.CharField(max_length=1000)
    sub_date = models.DateField()
    college = models.CharField(max_length=50)
    program = models.CharField(max_length=50)

    class Meta:
        db_table = 'thesis'

    def __str__(self):
        return str(self.title)
    
class thesisapp_comments(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    theses = models.ForeignKey('Thesis', related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'thesisapp_comments'
        verbose_name_plural = 'Thesis App Comments'

    def __str__(self):
        return f"Comment for Thesis {self.thesis.call_no}"
    
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True, db_column='admin_id')
    admin_username = models.CharField(max_length=50)
    admin_email = models.EmailField(unique=True)
    admin_password = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return str(self.admin_username)
