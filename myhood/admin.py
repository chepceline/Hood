from django.contrib import admin
from .models import Neighborhood,Gender, Profile,Post, PostType

admin.site.register(Profile)
admin.site.register(Gender)
admin.site.register(Post)
admin.site.register(Neighborhood)
#admin.site.register(Business)
admin.site.register(PostType)
