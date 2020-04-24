from accounts.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		user = authenticate(**data)
		if user:
			return user
		raise serializers.ValidationError('Incorrect Credentials')


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'username', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(
			name=validated_data["name"],
			username=validated_data["username"],
			email=validated_data["email"],
			password=validated_data["password"]
		)
		return user


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'username')