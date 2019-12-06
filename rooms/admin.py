from django.contrib import admin
from . import models


@admin.register(
    models.RoomType, models.Amenity, models.Facility, models.HouseRule
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Space", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last detail", {"fields": ("host",)}),
    )

    filter_horizontal = ("amenities", "facilities", "house_rules")

    # what are the criteria for deciding whether display or filter ?
    # the answer to question is context!
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # (^, startwith) / (=, iexact)
    search_fields = ("=city", "^host__username")

    ordering = ("name", "price")

    # this ftn is in admin, not model.
    # so this is not registered in db.
    def count_amenities(self, obj):
        print(obj)  # return objects connected to registered model
        return obj.amenities.count()

    # this rename column in list_display
    count_amenities.short_description = "junsik"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
