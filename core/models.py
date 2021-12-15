from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class BmiMeasurement(models.Model):
    UNDERWEIGHT = 'underweight'
    NORMAL = 'normal'
    OVERWEIGHT = 'overweight'
    OBESE = 'obese'
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
    result = models.CharField(blank=True, choices=RESULTS, verbose_name=_('result'), max_length=50)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    class Meta:
        db_table = 'bmimeasurement'
        verbose_name = 'bmi'
        verbose_name_plural = 'bmis'

    @staticmethod
    def get_bmi(height, weight):
        bmi = weight / height ** 2
        return bmi

    @staticmethod
    def get_result(bmi):
        if bmi < 18.5:
            return BmiMeasurement.UNDERWEIGHT
        elif bmi > 30:
            return BmiMeasurement.OBESE
        elif bmi <= 24.9:
            return BmiMeasurement.NORMAL
        return BmiMeasurement.OVERWEIGHT

    def save(self, *args, **kwargs):
        # type(BmiMeasurement.height)
        self.bmi = BmiMeasurement.get_bmi(self.weight, self.height)
        # bmi = self.get_bmi(BmiMeasurement.weight, BmiMeasurement.height)
        self.result = BmiMeasurement.get_result(self.bmi)
        super().save(*args, **kwargs)

    # @property
    # def bmi(self):
    #     bmi = self.weight / self.height ** 2
    #     return bmi
    #
    # # getter
    # def get_bmi(self):
    #     return self.bmi
    #
    # # setter
    # def set_bmi(self):
    #     return self.bmi

    # @property
    # def bmi(self):
    #     bmi = weight / height ** 2
    #     return bmi
    #
    # @property
    # def result(self):
    #     if bmi < 18.5:
    #         return self.UNDERWEIGHT
    #     elif bmi > 30:
    #         return self.OBESE
    #     elif bmi <= 24.9:
    #         return self.NORMAL
    #     return self.OVERWEIGHT
    #
    # # def save(self, force_insert=False, force_update=False, using=None,
    # #          update_fields=None):
    #
    # def save(self, *args, **kwargs):
    # #     weight = self.weight
    # #     height = self.height
    #     self.bmi = self.bmi
    #     self.result = self.result
    #     return super(BmiMeasurement, self).save(*args, **kwargs)
