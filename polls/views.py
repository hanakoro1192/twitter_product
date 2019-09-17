from django.shortcuts import render

# Create your views here.
def polls(request):

    return render(request, 'polls/polls.html')

