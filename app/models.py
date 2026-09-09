from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ("apartment", "Apartment"),
        ("villa", "Villa"),
        ("townhouse", "Townhouse"),
        ("luxury", "Luxury"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    # core attributes
    bedrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    bathrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    size_sqm = models.PositiveIntegerField(null=True, blank=True, help_text="Size / plinth area in sqm")

    # type and availability
    property_type = models.CharField(max_length=32, choices=PROPERTY_TYPE_CHOICES, default="apartment")
    is_ready_unit = models.BooleanField(default=False)
    is_offplan = models.BooleanField(default=False)
    available_for_sale = models.BooleanField(default=True)
    available_for_rent = models.BooleanField(default=False)

    # pricing
    price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    deposit = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    instalment_period_months = models.PositiveIntegerField(null=True, blank=True, help_text="Instalment period in months")
    estimated_roi_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # metadata
    units = models.PositiveIntegerField(null=True, blank=True, help_text="Number of units (if part of a development)")
    towers = models.PositiveIntegerField(null=True, blank=True, help_text="Number of towers (if part of a development)")
    amenities = models.TextField(blank=True, help_text="Comma or newline separated amenities")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.location or 'Unknown'}"

    def main_image(self):
        img = self.images.first()
        return img.image.url if img and img.image else None


# class ListingImage(models.Model):
#     listing = models.ForeignKey(Listing, related_name="images", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="listings/%Y/%m/%d/", blank=True, null=True)
#     caption = models.CharField(max_length=255, blank=True)
#     order = models.PositiveSmallIntegerField(default=0)

#     class Meta:
#         ordering = ["order"]

#     def __str__(self):
#         return self.caption or f"Image for {self.listing_id}"