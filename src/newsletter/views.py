from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome dog!!'
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title = "My title %s" %(request.user)
    # print dir(request)
    # if request.method == "POST":
    #     print request.POST
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid(): #validator in views
        instance = form.save(commit=False) #commit = false is to no auto commit the info in the db
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"

        if not instance.full_name == None:
            instance.full_name = "Caramelius"
        instance.save()
        context = {
            "title": "Thank you!!!"
        }
    return render(request, "home.html", context)
