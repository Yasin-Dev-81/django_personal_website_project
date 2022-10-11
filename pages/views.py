from django.shortcuts import render, redirect
from django.urls import reverse

from .models import AboutUs, WorkExperience, Education, MyProject
from .forms import ContactForm


def home_view(request):
    request_method = request.method
    if request_method == 'POST':
        new_contact_form = ContactForm(request.POST)
        if new_contact_form.is_valid():
            new_contact = new_contact_form.save(commit=False)
            print('---user:', request.user)
            new_contact.author = request.user
            new_contact.save()
            return redirect(reverse('home_url'))
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()
    return render(
        request=request,
        template_name='pages/home.html',
        context={
            'about_us': AboutUs.objects.order_by('?').first(),
            'work_experience': enuming(WorkExperience.objects.all()),
            'education': enuming(Education.objects.all()),
            'projects': MyProject.objects.all(),
            'contact_form': contact_form,
        }
    )


def enuming(input):
    return_list = []
    right = True
    for i in input:
        return_list.append((right, i, ))
        right = not right
    else:
        return return_list
