from django import forms
from django.forms import Form, ValidationError

from django.forms.models import inlineformset_factory, modelformset_factory, BaseModelFormSet, BaseInlineFormSet, BaseFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, StrictButton, Accordion, AccordionGroup, InlineRadios,PrependedAppendedText
from crispy_forms.layout import Layout, Submit, HTML, Div, Fieldset, Row, Field, Button,Hidden
from django.db import models

from customers.models import Customer, Breed, Pet, Service, Call, Appointment, AppointmentDetail


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('last_name','first_name','home_phone', 'work_phone', 'email', 'veterinarian', 'notes')
        widgets = {
          'notes': forms.Textarea(attrs={'rows':1, 'cols':60}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.layout=Layout(
            HTML('<br>'),
            Field('first_name'),Field('last_name'),
            Field('home_phone'),Field('work_phone'),Field('email'),
            Field('veterinarian'),Field('notes'),
            HTML('<br><br>'))

CustomerPetFormSet = inlineformset_factory(Customer,Pet,
        fields=("name","sex","breed",'birthday','vaccinated','notes','noisy','bites','shy','soils_cage','arthritic','epileptic','overweight'),
        widgets = {
            'notes': forms.Textarea(attrs={'rows':1, 'cols':95}),
            'sex':forms.RadioSelect(),
            'birthday':forms.DateInput(),
            'vaccinated':forms.CheckboxInput(),
            'noisy':forms.CheckboxInput(),
            'bites':forms.CheckboxInput(),
            'shy':forms.CheckboxInput(),
            'soils_cage':forms.CheckboxInput(),
            'arthritic':forms.CheckboxInput(),
            'epileptic':forms.CheckboxInput(),
            'overweight':forms.CheckboxInput(),
            },
        extra=1)

class CustomerPetFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CustomerPetFormSetHelper, self).__init__(*args, **kwargs)
        self.form_class = 'form-inline'
        self.form_method = 'post'
        #self.form_delete = 'pet_delete'
        self.form_list = 'appointment_pet_list'
        self.form_freetime = 'freetime'
        self.template='customers/customer_pet_form.html'
        self.layout = Layout(Div(
            'name','sex','breed','birthday',
            'notes',Div('vaccinated','noisy','bites','shy','soils_cage','arthritic','epileptic','overweight'),css_class="well")
        )
        self.render_required_fields = True

class CustomerDeleteForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('last_name','first_name','home_phone', 'work_phone', 'email', 'veterinarian', 'notes')

    def __init__(self, *args, **kwargs):
        super(CustomerDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(deletebutton,cancelbutton)
        )

class BreedDeleteForm(forms.ModelForm):
    class Meta:
        model = Breed
        exclude = ('breed','size','description')

    def __init__(self, *args, **kwargs):
        super(BreedDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(HTML('{% include "customers/button_delete.html" %}'),HTML('{% include "customers/button_cancel.html" %}')))

class BreedForm(forms.ModelForm):
    class Meta:
        model=Breed
        fields=('breed','size','description','picture')
        widgets = {
            'description': forms.Textarea(attrs={'rows':1, 'cols':80})}

    def __init__(self, *args, **kwargs):
        super(BreedForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(Div('picture'),Div('breed','size','description'))


class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields=('service','price','size','description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':1, 'cols':60})}
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
class ServiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('service','description','size','price')

    def __init__(self, *args, **kwargs):
        super(ServiceDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_tag = False
        self.helper.layout.append(
            FormActions(HTML('{% include "customers/button_delete.html" %}'),HTML('{% include "customers/button_cancel.html" %}')))

class PetDeleteForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('owner','name','breed','sex','vaccinated','noisy','bites','shy','soils_cage',
        'arthritic','epileptic','overweight','notes','birthday'
                                                     '')
    def __init__(self, *args, **kwargs):
        super(PetDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(deletebutton,cancelbutton))

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields=("id","name","sex","breed",'vaccinated','notes','noisy','bites','shy','soils_cage','arthritic','epileptic','overweight',"owner")

        widgets = {
            'notes': forms.Textarea(attrs={'rows':1, 'cols':60}),
            'sex':forms.RadioSelect(),
            'vaccinated':forms.CheckboxInput(),
            'noisy':forms.CheckboxInput(),
            'bites':forms.CheckboxInput(),
            'shy':forms.CheckboxInput(),
            'soils_cage':forms.CheckboxInput(),
            'arthritic':forms.CheckboxInput(),
            'epileptic':forms.CheckboxInput(),
            'overweight':forms.CheckboxInput(),
            }

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Fieldset('Pet','owner', 'name','breed','sex','vaccinated'),
            HTML('<br>'),
            Fieldset('Temperament','noisy','bites','shy','soils_cage'),
            HTML('<br>'),
            Fieldset('Health Issues','arthritic','epileptic','overweight'),
            HTML('<br>'),
            Fieldset('Pet Notes','notes'),
            HTML('<br>'))

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('when','notes')
        widgets = {
          'notes': forms.Textarea(attrs={'rows':1, 'cols':60}),
                  }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'

        self.helper.layout = Layout(
            Field('notes'),
            HTML("<br><br>"),
            Field('when',type="hidden"))

class BaseServiceInlineformset(BaseInlineFormSet):
    def get_queryset(self):
        '''
        Copied this method from Django code and modified the ordering statement
        '''
        if not hasattr(self, '_queryset'):
            if self.queryset is not None:
                qs = self.queryset
            else:
                qs = self.model._default_manager.get_query_set()

            # If the queryset isn't already ordered we need to add an
            # artificial ordering here to make sure that all formsets
            # constructed from this queryset have the same form order.
            if not qs.ordered:
    # MY MOD IS HERE:
    #            qs = qs.order_by(self.model._meta.pk.name)
                qs = qs.order_by('service','-price')
    #/MOD

            # Removed queryset limiting here. As per discussion re: #13023
            # on django-dev, max_num should not prevent existing
            # related objects/inlines from being displayed.
            self._queryset = qs
        return self._queryset

AppointmentServiceFormSet=inlineformset_factory(Appointment, AppointmentDetail, formset=BaseServiceInlineformset,
        fields=('do_it','service','price'),
        widgets={'do_it':forms.CheckboxInput()},
        can_delete=False,
                   extra=0)

class AppointmentServiceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AppointmentServiceFormSetHelper, self).__init__(*args, **kwargs)
        self.template='bootstrap3/uni_formset.html'
        self.form_class = 'form-inline'
        self.form_method = 'post'
        self.layout = Layout('do_it','service','price')
        self.render_required_fields = True

class AppointmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ('when','notes','pet','gcalid','todo','total')
    def __init__(self, *args, **kwargs):
        super(AppointmentDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(
            FormActions(HTML('{% include "customers/button_delete.html" %}'),HTML('{% include "customers/button_cancel.html" %}')))

