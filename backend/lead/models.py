from team.models import Team
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

def upload_to(instance, filename):
    try:
        title = instance.lead.company
    except:
        title = instance.company
    slug = slugify(title)
    return 'posts/{filename}'.format(filename = slug + '_' + filename)
    

class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'
    CHOICES_STATUS = {
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'lost'),
        (WON, 'won')
    }

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CHOICES_PRIORITY = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    )

    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=upload_to, default="image/placeholder.jpeg")
    confidence = models.IntegerField(null=True, blank=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=100, choices=CHOICES_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assignedleads', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)

    def __str__(self):
        return self.company


class ImageGallery(models.Model):
    lead = models.ForeignKey(Lead, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to,
                              verbose_name='Image')

    def __str__(self):
        return self.lead.company
