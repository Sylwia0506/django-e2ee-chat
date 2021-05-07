from rest_framework import serializers
from .models import Profile, Invite


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'invite')


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invite
        fields = ('invite',)


class RegisterSerializer(serializers.Serializer):
    invite = serializers.CharField()
    public_key = serializers.CharField()
    hcaptcha = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class LoginSerializer(serializers.Serializer):
    id = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
