from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # I don't want to this to db. because this is parts for extending other models
    # so write code like below
    class Meta:
        abstract = True
