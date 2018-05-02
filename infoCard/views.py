from django.shortcuts import render

def info_list(request):
    return render(request, 'infoCard/info_list.html', {})
