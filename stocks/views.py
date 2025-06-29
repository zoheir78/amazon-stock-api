from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import StockPrice, Annotation
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .forms import (
    DateFilterForm,
    AnnotationForm,
)  # Optional if use a form for annotation


def landing_page(request):
    stocks = StockPrice.objects.all().order_by("date")

    # Filtering between two dates
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    high_volume = request.GET.get("high_volume")

    # Apply filters to the queryset
    if start_date:
        stocks = stocks.filter(date__gte=start_date)
    if end_date:
        stocks = stocks.filter(date__lte=end_date)
    if high_volume:
        stocks = stocks.filter(volume__gt=10_000_000)

    # Paginate the results (25 per page)
    paginator = Paginator(stocks, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Determine if we're editing an annotation
    edit_annotation_id = request.GET.get("edit")
    annotation_instance = None
    if edit_annotation_id:
        annotation_instance = Annotation.objects.get(pk=edit_annotation_id)

    # Handle POST (create or update)
    if request.method == "POST":
        if "update_id" in request.POST:
            annotation_instance = Annotation.objects.get(
                pk=request.POST.get("update_id")
            )
            form = AnnotationForm(request.POST, instance=annotation_instance)
        else:
            form = AnnotationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("landing")

    else:
        form = AnnotationForm(instance=annotation_instance)

    if start_date and end_date:
        annotations = Annotation.objects.filter(date__range=[start_date, end_date])
    else:
        annotations = Annotation.objects.all()

    # Paginate annotations separately
    annotation_paginator = Paginator(annotations, 5)  # 5 annotations per page
    annotation_page_number = request.GET.get("annotation_page")
    annotation_page_obj = annotation_paginator.get_page(annotation_page_number)

    context = {
        "page_obj": page_obj,  # stocks
        "annotation_page_obj": annotation_page_obj,  # paginated annotations
        "start_date": start_date,
        "end_date": end_date,
        "high_volume": high_volume,
        "form": form,
        "annotations": annotation_page_obj,  # only use paginated annotations in the template
        "editing": annotation_instance,
    }

    return render(request, "stocks/landing.html", context)


@require_POST
def delete_annotation(request, annotation_id):
    annotation = get_object_or_404(Annotation, id=annotation_id)
    annotation.delete()
    return redirect("landing")
