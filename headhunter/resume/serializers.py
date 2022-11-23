from rest_framework import serializers

from resume.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'company_name', 'position', 'start_work', 'end_work', 'resume')

