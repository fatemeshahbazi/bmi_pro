from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BmiMeasurement

from accounts.serializers import UserRegisterSerializer


class BmiSerializer(serializers.ModelSerializer):
    UNDERWEIGHT = 'underweight'
    NORMAL = 'normal'
    OVERWEIGHT = 'overweight'
    OBESE = 'obese'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(BmiSerializer, self).__init__(*args, **kwargs)

    user = UserRegisterSerializer(read_only=True)
    previous_status = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BmiMeasurement
        fields = ('user', 'height', 'weight', 'bmi', 'previous_status', 'result')
        extra_kwargs = {
            'bmi': {'read_only': True},
            'result': {'read_only': True}
        }

    def create(self, validated_data):
        height = self.validated_data.get('height')
        weight = self.validated_data.get('weight')
        bmi = self.get_bmi(weight=weight, height=height)
        result = self.result(bmi=bmi)
        user = self.request.user

        instance = BmiMeasurement(
            height=height,
            weight=weight,
            bmi=bmi,
            result=result
        )
        if user.is_authenticated:
            instance.user = user

        instance.save()
        return instance

    def validate_weight(self, value):
        if value > 0:
            weight = float(value)
            return weight
        raise ValidationError('weight is not valid')

    def validate_height(self, value):
        if value > 0:
            height = float(value)
            return height
        raise ValidationError('height is not valid')

    def get_result(self, obj):
        if obj.bmi < 18.5:
            return self.UNDERWEIGHT
        elif obj.bmi > 30:
            return self.OBESE
        elif obj.bmi <= 24.9:
            return self.NORMAL
        return self.OVERWEIGHT

    def result(self, bmi):
        if bmi < 18.5:
            return self.UNDERWEIGHT
        elif bmi > 30:
            return self.OBESE
        elif bmi <= 24.9:
            return self.NORMAL
        return self.OVERWEIGHT

    def get_bmi(self, weight, height):
        bmi = weight / height ** 2
        return bmi

    def get_previous_status(self, obj):
        if float(obj.bmi) >= 30:
            return f'You need to loose {self.get_delta_weight(round(float(obj.bmi) - 30, 2), obj.height)} kgs'
        elif float(obj.bmi) <= 18.5:
            return f'You are underweight'
        elif float(obj.bmi) >= 24.9:
            return f'You need to lose {self.get_delta_weight(round(float(obj.bmi) - 24.9, 2), obj.height)} kgs'
        return f'You need to lose {self.get_delta_weight(round(float(obj.bmi) - 18.5, 2), obj.height)} kgs'

    @staticmethod
    def get_delta_weight(delta_bmi, height):
        return round(delta_bmi * height ** 2, 2)
