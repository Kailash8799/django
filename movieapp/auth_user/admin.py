from django.contrib import admin
from .models import User,Contact

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','user_name','user_email']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['message_id','m_u_name','m_email','u_message']
