# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    years_of_experience = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dishtype(models.Model):

    #__Dishtype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Dishtype_FIELDS__END

    class Meta:
        verbose_name        = _("Dishtype")
        verbose_name_plural = _("Dishtype")


class Cook(models.Model):

    #__Cook_FIELDS__
    years_of_experience = models.IntegerField(null=True, blank=True)

    #__Cook_FIELDS__END

    class Meta:
        verbose_name        = _("Cook")
        verbose_name_plural = _("Cook")


class Dish(models.Model):

    #__Dish_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.TextField(max_length=255, null=True, blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ForeignKey(Cook, on_delete=models.CASCADE)

    #__Dish_FIELDS__END

    class Meta:
        verbose_name        = _("Dish")
        verbose_name_plural = _("Dish")


class Ingredient(models.Model):

    #__Ingredient_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(max_length=255, null=True, blank=True)
    dishes = models.ForeignKey(Dish, on_delete=models.CASCADE)

    #__Ingredient_FIELDS__END

    class Meta:
        verbose_name        = _("Ingredient")
        verbose_name_plural = _("Ingredient")



#__MODELS__END
