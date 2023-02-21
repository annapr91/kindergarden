from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, BadHeaderError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView
from django.conf.global_settings import LANGUAGES
from .forms import ContactUSERForm, RegistrationKind, USERREG, RegisUserForm
from .models import *
from django.conf import settings


# Create your views here.
def home(request):
    us=User.objects.all()
    for el in us:
        print(type(el.address))
    return render(request, 'home.html', {'us': us})

def price(request):
    chil=Children.objects.all()
    return render(request, 'price.html',{'chil':chil})

# class ContactForm(FormView):
#     form_class = ContactUSERForm
#     template_name = 'contact.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

def contact_view(request):
    form = ContactUSERForm()

    if request.method =='POST':
        form = ContactUSERForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            html = render_to_string('contctformemail.html', {
                     'name': name,
                     'from_email': from_email,
                     'message': message,
                 })
            send_mail(f'{name}-{from_email}',
                      message,settings.EMAIL_HOST_USER, [settings.RECIPIENTS_EMAIL], fail_silently=False,html_message=html)
            form.save()

            return redirect('success')
        # else:
        #     return HttpResponse('Неверный запрос.')
    return render(request, "contact.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

# def view_people(request):
#     form= RegistrationKind()
#     chil=Children.objects.all()
#     rodit=Perents.objects.all()
#     context={
#         'children': chil,
#         'perents': rodit,
#         'form':form,
#     }
#     return render(request, 'people.html',context=context)

# class RedKindrChil(FormView):
#     form_class = RegistrationKind
#     template_name = ''
def RegKidSad(request):
    perents = Perents.objects.all()


    if request.method == 'POST':
        form = USERREG(request.POST)
        if form.is_valid():
            form.save()
        return redirect("kids")
    return render(request, 'people.html',{'perents':perents})

class Kidbuil(ListView):
    model = Kindergarden
    template_name = 'kid_building.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

# def RegKidSad(request):
#     if request.method == 'GET':
#         perents= Perents.objects.all()
#         return render(request, 'people.html')
#     elif request.method == 'POST':
#         perent = Perents()
#         perent.name = request.POST.get("name")
#         perent.id_number = request.POST.get("id_number")
#         perent.phone_number = request.POST.get("phone_number")
#         perent.save()
#         # print(perent.id)
#     return redirect("kids")

# class RegKidSad(FormView):
#     form_class = USERREG
#     template_name = 'people.html'
#     success_url = reverse_lazy('kids')
#
#     def reg(request,form):
#         if request.method == 'POST':
#             perent = Perents()
#             perent.name = request.Post.get("name")
#             perent.id_number = request.Post.get("id_number")
#             perent.phone_number = request.Post.get("phone_number")
#             perent.save()
#         return super().reg(form)
# class RegKidSad(FormView):
#     form_class = USERREG
#     template_name = 'people.html'
#     success_url = reverse_lazy('kids')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
class RegisterUser(CreateView):
    form_class = RegisUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
    #     return redirect('/')




def kidkas(request):
     rodid=Perents.objects.latest('id')
#     # person = Perents.objects.filter(id=id)
     if request.method == 'GET':
         return render(request, 'kids.html')
     if request.method == 'POST':
         child = Children()
         user=Perents()
         print(user)
         child.name = request.POST.get("name")
         child.id_number = request.POST.get("id_number")
         child.surname = request.POST.get("surname")
         last_zapis = Perents.objects.latest('id')
         child.roditeli_id = last_zapis.id
         child.save()
     return redirect("home")

# class REGISKIDS(FormView):
#     form_class = RegistrationKind
#     template_name = 'kids.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)