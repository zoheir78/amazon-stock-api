from django.contrib import admin
from .models import StockPrice, Annotation


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ("date", "open", "high", "low", "close", "adj_close", "volume")
    search_fields = ("date",)
    list_filter = ("date",)


admin.site.register(Annotation)
