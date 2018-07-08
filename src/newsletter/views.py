from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Welcome dog!!'
    if request.user.is_authenticated():
        title = "My title %s" %(request.user)
    print dir(request)
    context = {"template_title": title}
    return render(request, "home.html", context)
