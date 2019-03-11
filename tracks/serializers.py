from rest_framework import serializers
from .models import Track, Question, Choice


class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = "__all__"
		read_only_fields = ("created_date", "track")


class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = "__all__"
		read_only_fields = ("question", "votes")