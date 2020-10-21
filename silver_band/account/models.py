from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        default="",
    )
    email = models.EmailField(_("email address"), unique=True)
    wearer = models.ForeignKey("account.Wearer", on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Wearer(models.Model):
    name = models.CharField(max_length=100, default="", null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    sex = models.CharField(max_length=100, default="", null=True, blank=True)
    address = models.CharField(max_length=500, default="", null=True, blank=True)
