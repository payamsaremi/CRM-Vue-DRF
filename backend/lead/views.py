from team.models import Team
from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.
from .models import Lead, ImageGallery
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
        queryset = Lead.objects.all()
        serializer_class = LeadSerializer
        parser_classes = [FormParser, MultiPartParser]
        
        def perform_create(self, serializer):
            team = Team.objects.filter(members__in=[self.request.user]).first()
            serializer.save( team=team, created_by = self.request.user)

        def get_queryset(self):
            team = Team.objects.filter(members__in=[self.request.user]).first()
            # return self.queryset.filter(created_by = self.request.user)
            return self.queryset.filter(team=team)
