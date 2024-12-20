from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.staticfiles.finders import find
from django.core.cache import cache
from django.core.exceptions import (
    ImproperlyConfigured,
    ValidationError,
    ObjectDoesNotExist,
)
from django.core.files.base import File
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Count, Exists, OuterRef, Sum

from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext, pgettext_lazy
from oscar.models.fields import AutoSlugField, NullCharField
from shop.apps.main.models import BaseLogModelMixin

class AbstractSeller(BaseLogModelMixin):
    name = models.CharField(_("Shop Name"), max_length=128, unique=True, blank=False, null=False, db_index=True)
    handle = models.SlugField(_("Shop Handle"), max_length=20, unique=True, blank=False, null=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, null=False,
        verbose_name=_("Seller User"), on_delete=models.PROTECT, related_name="seller")
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
        verbose_name=_("Shop Admin"), on_delete=models.PROTECT, related_name="seller_admins")
    ceo = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT, related_name="seller_ceos")

    class Meta:
        abstract = True
        app_label = "seller"
        ordering = ["name"]
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")
