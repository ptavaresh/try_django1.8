from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

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
    return render(request, "base.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data.iteritems():
        #     print key
        #print form.cleaned_data.get(key)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youremail@gmail.com']
        #some_html_message = "html code"
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
    context = {
        'form': form,
    }

    return render(request, "forms.html", context)