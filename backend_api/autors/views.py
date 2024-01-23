from rest_framework import generics


from autors.serializers import AutorSerializer


class AutorCreatView(generics.CreateAPIView):

    serializer_class = AutorSerializer
