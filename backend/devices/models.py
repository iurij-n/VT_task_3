from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=24)
    ip_adress = models.GenericIPAddressField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Features(models.Model):
    device = models.ForeignKey(Device,
                               related_name='features',
                               on_delete=models.CASCADE)
    feature = models.CharField(max_length=250)
    unit = models.CharField(max_length=50,
                            blank=True,
                            null=True)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.feature
