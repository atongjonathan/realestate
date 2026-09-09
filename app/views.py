from multiprocessing import context
from turtle import color

from django.shortcuts import render


menu_items = [
    {"name": "Home", "url_name": "index"},
    {"name": "About", "url_name": "about"},
    {"name": "Services", "url_name": "services"},
    {"name": "Properties", "url_name": "properties"},
    {"name": "Contact", "url_name": "contact"},
]


# Create your views here.
def index(request):

    context = {
        "menu_items": menu_items,
        "page_title": "Discover Your Dream Home with Us",
        "page_subtitle": "Find the Perfect Property for Your Lifestyle",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/hero-bg.jpg",
        "title": "Home - Popote Listings"
    }
    return render(request, "app/index.html", context)

def about(request):
    context = {
        "menu_items": menu_items,
        "page_title": "Discover Our Story and Expertise",
        "page_subtitle": "Learn more about our company and team",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/about-bg.jpg",
        "title": "About - Popote Listings"
    }
    return render(request, "app/about.html", context)

def services(request):

    context = {
        "menu_items": menu_items,
        "page_title": "Services",
        "page_subtitle": "We offer a wide Range of Services",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/services-bg.jpg",
        "title": "Services - Popote Listings"
    }
    return render(request, "app/services.html", context)

def properties(request):
    context = {
        "menu_items": menu_items,
        "page_title": "Properties",
        "page_subtitle": "Looking to Buy, Sell, Rent, Invest or Manage?",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/properties-bg.jpg",
        "title": "Properties - Popote Listings"
    }
    return render(request, "app/properties.html", context)

def contact(request):

    context = {
        "menu_items": menu_items,
        "page_title": "Contact Us",
        "page_subtitle": "We’re Just a Phone Call or Message Away",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/contact-us-bg.jpg",
        "title": "Contact - Popote Listings"
    }
    return render(request, "app/contact.html", context)
def find_properties(request):
    context = {
        "menu_items": menu_items,
        "page_title": "Find Your Property",
        "page_subtitle": "Search and Filter Through Our Listings",
        "hero_image": "https://websitedemos.net/real-estate-company-04/wp-content/uploads/sites/1484/2023/07/properties-bg.jpg",
        "title": "Find Properties - Popote Listings"
    }
    return render(request, "app/find_properties.html", context)