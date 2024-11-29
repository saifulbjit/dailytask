from rest_framework import serializers
from jobs.models import Job, Category, Application


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['description', 'added_by']

    def get_category_name(self, obj):
        return obj.category.name

class JobDetailSerializer(JobSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'



