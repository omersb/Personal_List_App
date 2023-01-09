from rest_framework import serializers
from .models import Department, Personal
from django.utils.timezone import now


class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count')

    def get_personal_count(self, obj):
        # deparmentlardaki personelleri saydırdık
        return Personal.objects.filter(department=obj.id).count()


class PersonalSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    create_user = serializers.StringRelatedField()

    class Meta:
        model = Personal
        fields = "__all__"

    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days


class DepartmentPersonalSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    departments = PersonalSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count', 'departments')

    def get_personal_count(self, obj):
        # deparmentlardaki personelleri saydırdık
        return Personal.objects.filter(department=obj.id).count()
