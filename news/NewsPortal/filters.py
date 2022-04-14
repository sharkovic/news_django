from django_filters import FilterSet, DateTimeFilter, DateTimeFromToRangeFilter
from .models import models
from .models import Post
from django import forms


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class SearchFilter(FilterSet):
    date_range = DateTimeFromToRangeFilter(widget=forms.SelectDateWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'title_post': ['icontains'],
            'area_post': ['icontains'],
            'date_of_creation': ['gt'],
        }

        # filter_overrides = {
        #     models.DateTimeField: {
        #         'filter_class': DateTimeFromToRangeFilter,
        #         'extra': lambda f: {
        #             'widget': forms.SelectDateWidget,
        #         },
        #     }
        # }
