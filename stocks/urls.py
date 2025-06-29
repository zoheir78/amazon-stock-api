from django.urls import path
from . import views  # frontend
from . import api  # API views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    # Stocks
    path("api/stocks/", api.StockPriceListView.as_view(), name="stock-list"),
    path(
        "api/stocks/<int:pk>/", api.StockPriceDetailView.as_view(), name="stock-detail"
    ),
    # Annotations
    path("api/annotations/", api.AnnotationListView.as_view(), name="annotation-list"),
    path(
        "api/annotations/add/",
        api.AnnotationCreateView.as_view(),
        name="annotation-create",
    ),
    path(
        "api/annotations/<int:pk>/delete/",
        api.AnnotationDeleteView.as_view(),
        name="annotation-api-delete",
    ),
    path(
        "annotation/<int:annotation_id>/delete/",
        views.delete_annotation,
        name="annotation-delete",
    ),
    path(
        "api/annotations/<int:pk>/update/",
        api.AnnotationUpdateView.as_view(),
        name="annotation-update",
    ),
]
