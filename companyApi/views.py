from django .http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page requested")
    subjects=[
        'OS',
        'COS',
        'dbms'
    ]
    return JsonResponse(subjects, safe = False)