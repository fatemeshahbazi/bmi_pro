from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class BmiMeasurement(models.Model):
    UNDERWEIGHT = 1
    NORMAL = 2
    OVERWEIGHT = 3
    OBESE = 4

    RESULTS = (

        (UNDERWEIGHT, 'underweight'),
        (NORMAL, 'normal'),
        (OVERWEIGHT, 'overweight'),
        (OBESE, 'obese'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('user'))
    height = models.FloatField(verbose_name=_('height'))
    weight = models.FloatField(verbose_name=_('weight'))
    bmi = models.DecimalField(verbose_name=_('bmi'), max_digits=10, decimal_places=2, blank=True)
    result = models.PositiveSmallIntegerField(blank=True, choices=RESULTS, verbose_name=_('result'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    class Meta:
        db_table = 'bmimeasurement'
        verbose_name = 'bmi'
        verbose_name_plural = 'bmis'

    @staticmethod
    def validate_height(value):
        if value > 3:
            return value / 100
        return value

    @staticmethod
    def get_result(bmi):
        if bmi < 18.5:
            return 1
        elif bmi > 30:
            return 4
        elif bmi <= 24.9:
            return 2
        return 3

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.height = self.validate_height(self.height)
        self.bmi = self.weight / self.height ** 2
        self.result = self.get_result(self.bmi)
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
