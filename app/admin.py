from django.contrib import admin
from .models import User, Listing


admin.site.site_header = "Popote Listings Administration"
admin.site.site_title = "Popote Listings Admin"
admin.site.index_title = "Welcome to Popote Listings Administration"
admin.site.register(User)
admin.site.register(Listing)