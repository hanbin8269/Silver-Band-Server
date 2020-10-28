from django.db import models

# Create your models here.
class Location(models.Model):
    wearer = models.ForeignKey("account.Wearer", on_delete=models.CASCADE, null=False)
    loc_x = models.FloatField()
    loc_y = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)