from django.contrib import admin
from django.contrib.auth.models import User
from .models import Address, LawyerProfile, LawyerImage, LawyerDocument , ClientProfile , User , TimeSlot

# Register your models here.
admin.site.register(Address),
admin.site.register(LawyerProfile),
admin.site.register(LawyerDocument),
admin.site.register(LawyerImage),
admin.site.register(ClientProfile),

admin.site.register(TimeSlot),

