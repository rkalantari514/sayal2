from rest_framework import serializers

from contents.models import Projects


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        # fields = ['url', 'username', 'email', 'is_staff']
        # fields = '__all__'
        fields = [
            "active",
            "name",
            "subject",
            "about_project",
            "p_picture",
            "timep",
            "kinde",
            "statusp",
            "zirbana",
            "area",
            "price",
            "locationp",
            "employer",
            "engineer",
        ]
