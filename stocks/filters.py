import django_filters
from .models import StockPrice

class StockPriceFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = StockPrice
        fields = ['start_date', 'end_date']
