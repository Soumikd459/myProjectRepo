from django.db import models

# Create your models here.
class Status(models.Model):
    
    status_id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=100, default="ADMIN", null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    ##### To give custom table name specify under Meta class
    # class Meta:
    #     db_table = 'status'

    def __str__(self) -> str:
        return self.name
