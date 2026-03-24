from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseForbidden


@login_required
def dashboard(request):

    if not request.gym:
        return HttpResponseForbidden()

    if not request.role:
        return HttpResponseForbidden()

    return render(request, "core/dashboard.html")