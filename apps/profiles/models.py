from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    phone_number = PhoneNumberField(
        _('Phone Number'), max_length=20, default='+989120000000')
    about_me = models.TextField(
        _('About me'), default='Say something about yourself')
    licence = models.CharField(
        _("Licence"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(
        _("Profile Photo"), upload_to='profile_photos/', default='/profile_photos/default.png')
    gender = models.CharField(
        _('Gender'), max_length=20, choices=Gender.choices, default=Gender.OTHER)
    country = CountryField(_('Country'), default='IR')
    city = models.CharField(_('City'), max_length=50, default='Tehran')
    is_buyer = models.BooleanField(_('Buyer'), default=False, help_text=_(
        'Are you looking to buy a property?'))
    is_seller = models.BooleanField(_('Seller'), default=False, help_text=_(
        'Are you looking to sell a property?'))
    is_agent = models.BooleanField(
        _('Agent'), default=False, help_text=_('Are you an agent?'))
    top_agent = models.BooleanField(_('Top Agent'), default=False)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        _('Number of Reviews'), default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
