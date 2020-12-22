from django.contrib import admin

from .models import (
    CustomUser,
    Thread,
    Comment
)

admin.site.register(CustomUser)
admin.site.register(Thread)
admin.site.register(Comment)
