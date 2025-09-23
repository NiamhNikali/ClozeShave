from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Reading(models.Model):
    name = "reading"

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
