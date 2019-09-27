from django.shortcuts import render
def confname(request):
    globalname = {
        "logoname": "OU Project"
    }
    return render(request, globalname)
    
