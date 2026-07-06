from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at questions {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
