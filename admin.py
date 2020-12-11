from django.contrib import admin
from DBRapp.models import * #import DBRuser as well as Book class

admin.site.register(DBRuser)
admin.site.register(Book)
