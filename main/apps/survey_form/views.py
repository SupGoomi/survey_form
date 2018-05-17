from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'attempt' in request.session:
        request.session['attempt']=0
    return render(request, 'survey_form/index.html')
def process(request):
    if request.method != "POST":
        return redirect('/')
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['attempt'] += 1
    return redirect('/result')    
def result(request):
    return render(request, 'survey_form/result.html')