from django.http import JsonResponse
from django.shortcuts import render


def ads_root(request):
    return JsonResponse({"status": "ok"})
