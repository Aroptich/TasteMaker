from rest_framework.serializers import ModelSerializer

from autors.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ('login',
                  'password',
                  'email',)

    def create(self, validated_data):
        password = validated_data.pop("password")
        autor = Autor(**validated_data)
        autor.set_password(password)
        autor.save()
        return autor