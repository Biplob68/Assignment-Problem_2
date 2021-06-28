from django.contrib import admin


from mysite.models import Contact
from mysite.models import Login
from mysite.models import Reg

# Register your models here.
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Reg)