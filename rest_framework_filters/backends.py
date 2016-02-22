
import rest_framework.filters
from .filterset import FilterSet


class DjangoFilterBackend(rest_framework.filters.DjangoFilterBackend):
    default_filter_set = FilterSet

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            subset_class = filter_class.get_subset(request.query_params)
            return subset_class(request.query_params, queryset=queryset).qs

        return queryset
