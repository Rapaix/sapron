from .serializers import AgendaListSerializer, AgendaDetailSerializer
from rest_framework import generics, filters
from .models import Agenda


class AgendaListAPIView(generics.ListAPIView):

    queryset = Agenda.objects.all()
    serializer_class = AgendaListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['checkin']

    search_fields = ['hospede', 'id']


class AgendaRetrieveAPIView(generics.RetrieveAPIView):

    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer


class AgendaCreateAPIView(generics.CreateAPIView):

    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer


class AgendaUpdateAPIView(generics.RetrieveUpdateAPIView):

    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer


class AgendaDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Agenda.objects.all()
