from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from publications.models import Publication
from publications.forms import PublicationForm

from utils import custom_paginator


def publications(request):
    form = PublicationForm()
    # num = custom_paginator(paginator.num_pages)
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Publication.objects.create(title=data.get("title"),
                                       body=data.get("body"),
                                       image=data.get("image"),
                                       author=request.user)
    publications = Publication.objects.all()
    paginator = Paginator(publications, 10)
    page = request.GET.get('page')

    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)
    return render(request, "publications.html", {"publications": publications,
                                                 "form": form})
