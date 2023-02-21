import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Children, Perents, ContactForm, User


class ContactUSERForm(forms.ModelForm):
    name = forms.CharField(max_length=20,label=_(u'Name'))
    email = forms.EmailField(label=_(u'email'))
    subject = forms.CharField(max_length=255,label=_(u'subject'))
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000,label=_(u'message'))

    class Meta:
        model = ContactForm
        fields = ('name', 'email','message')

class USERREG(forms.ModelForm):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))
    # phone_number = forms.CharField(max_length=30,
    #                        widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))
    # roditeli = forms.CharField(max_length=30,
    #                        widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))
    # det_sads = forms.CharField(max_length=30,
    #                        widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))


    class Meta:
        model = Perents
        fields = ('name', 'id_number')



class RegistrationKind(forms.ModelForm):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))
    # roditeli = forms.CharField(max_length=30,
    #                        widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))
    det_sads = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control wow fadeInUp', 'placeholder': 'Name'}))


    class Meta:
        model = Children
        fields = ('name', 'surname', 'det_sads','id_number','roditeli')



class RegisUserForm(UserCreationForm):
    error_messages = {
        'address_mismatch': _('Адрес состоит из - улица,дом/кварира.'),
        'phone_mismatch' : _('Проверьте ,должно содержать 8 цифр.')
    }
    first_name = forms.CharField(label=_('Имя'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label=_('Фамилия'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label=_('Почта'), widget=forms.EmailInput(attrs={'class': 'form-input','placeholder': 'Почта'}))
    username = forms.CharField(label=_('Логин'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=_('Повтор пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    phone = forms.IntegerField(localize=False,label=_('Телефон'), widget=forms.NumberInput(attrs={'class': 'form-input','placeholder': _('телефон') }))
    address=forms.CharField(label=_('Адрес'), widget=forms.TextInput(attrs={'class': 'form-input','placeholder': _('улица,дом/квартира') }))

    def clean_address(self):
        data = self.cleaned_data['address']
        c = re.match(r'^[а-яА-яa-zA-Z]+,\d+/\d+$', data)
        print(c)
        if not c:
            raise ValidationError(
                         self.error_messages['address_mismatch'],
                         code='address_mismatch',
                     )
        # for el in number:
        #     if str(el) in street:
        #         raise ValidationError(
        #             self.error_messages['address_mismatch'],
        #             code = 'address_mismatch',
        #         )

        # for st in alphabet:
        #     if  hous_app.split('/'):
        #         hous, app = hous_app.split('/')
        #
        #         if st in hous:
        #             raise ValidationError('House should contain only number')
        #         if st  in app:
        #             raise ValidationError('Appartment should contain only number')

        return data

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone))!=8:
            raise ValidationError(
                self.error_messages['phone_mismatch'],
                code='phone_mismatch',
            )

        return phone


    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2','phone','address')