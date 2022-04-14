from django_filters import FilterSet, DateFilter, DateTimeFilter
# from django_filters.widgets import RangeWidget, CSVWidget

from .models import models
from .models import Post
from django import forms
import datetime

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class SearchFilter(FilterSet):
    date_of_creation = DateTimeFilter(
        lookup_expr='gt',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Post
        fields = {
            'area_post': ['icontains'],
            'author__name': ['exact'],


        }
