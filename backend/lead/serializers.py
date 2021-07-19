from rest_framework import serializers
from .models import ImageGallery, Lead
from team.serializer import UserSerializer

class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = ['id', 'image']

class LeadSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageGallerySerializer(source='imagegallery_set', many=True, read_only=True)
    assigned_to = UserSerializer(read_only=True)
    
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        )
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'images',
            'logo',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )
    def create(self, validated_data):
        # upload only the "files[i]" files not logo or anything else
        images_data = self.context.get('view').request.FILES
        files_length = self.context.get('view').request.data['files_length']
        print(files_length)
        files = []
        for file in images_data.items():
            for i in range(int(files_length)):
                if file[0] == 'files['+str(i)+']':
                    files.append(file)
        # print(files)
        lead = Lead.objects.create(**validated_data)
        for image_data in files:
            image = image_data[1]
            print(image)
            ImageGallery.objects.create(lead=lead, image=image)
        return lead