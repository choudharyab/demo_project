from django.contrib import admin
from  django.contrib import admin
from  .models import User,admin1,Role,Profile,Article,right


# Register your models here.


admin.site.register(User)
admin.site.register(admin1)
admin.site.register(Role)
admin.site.register(Profile)
#admin.site.register(Access)
admin.site.register(Article)
admin.site.register(right)