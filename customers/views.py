import datetime
import os
import httplib2
import re

from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from django.views.generic import ListView
from django.utils.decorators import method_decorator

from django.template import RequestContext
from django.core.urlresolvers import reverse



from crispy_forms.layout import Field

from apiclient.discovery import build

from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from customers.django_orm import Storage


from grooming import settings
from customers.forms import CustomerForm, CustomerDeleteForm, CustomerPetFormSet, CustomerPetFormSetHelper
from customers.forms import BreedDeleteForm
from customers.forms import ServiceDeleteForm
from customers.forms import PetDeleteForm, PetForm, BreedForm
from customers.models import Customer, Pet, Breed, Service, Call , CredentialsModel, Appointment, AppointmentDetail, User
from customers.forms import AppointmentDeleteForm, ServiceForm
from customers.forms import AppointmentForm, AppointmentServiceFormSet,AppointmentServiceFormSetHelper



CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://localhost:8000/oauth2callback')

# Customer Model views

class CustomerCreate(CreateView):
    model=Customer
    form_class=CustomerForm
    customerpet_form = CustomerPetFormSet()
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('customer_list')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CustomerCreate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        phone = request.GET.get('phone','')
        callername = request.GET.get('name','')
        nameparts = callername.split()
        try:
            numparts=len(nameparts)
        except IndexError:
            numparts=0
        firstname=""
        lastname=""
        if numparts>1:
            firstname=nameparts[numparts-1].title()
            nameparts.pop()
            lastname=" ".join(nameparts).title()


        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.helper['home_phone'].wrap(Field,value='{}'.format(phone))
        form.helper['last_name'].wrap(Field,value='{}'.format(lastname))
        form.helper['first_name'].wrap(Field,value='{}'.format(firstname))
        customerpet_form = CustomerPetFormSet()
        helper = CustomerPetFormSetHelper()
        return self.render_to_response(
            self.get_context_data(form=form,helper=helper,
                                  customerpet_form=customerpet_form,
            ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        customerpet_form = CustomerPetFormSet(self.request.POST)
        helper = CustomerPetFormSetHelper()
        if form.is_valid() and customerpet_form.is_valid():
            return self.form_valid(form, customerpet_form)
        else:
            return self.form_invalid(form, customerpet_form, helper)

    def form_valid(self, form, customerpet_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        customerpet_form.instance = self.object
        customerpet_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, customerpet_form, helper):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, helper=helper,
                                  customerpet_form=customerpet_form,
                                  ))

class CustomerUpdate(UpdateView):
    model=Customer
    form_class=CustomerForm
    template_name_suffix = '_detail_form'
    success_url = reverse_lazy('customer_list')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CustomerUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = Customer.objects.get(pk=kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        customerpet_form = CustomerPetFormSet(instance=self.object)
        helper = CustomerPetFormSetHelper()

        return self.render_to_response(
            self.get_context_data(form=form,helper=helper,
                                  customerpet_form=customerpet_form,
            ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = Customer.objects.get(pk=kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        customerpet_form = CustomerPetFormSet(self.request.POST,instance=self.object)
        helper = CustomerPetFormSetHelper()
        if (form.is_valid() and customerpet_form.is_valid()):
            return self.form_valid(form, customerpet_form)
        else:
            return self.form_invalid(form, customerpet_form, helper)

    def form_valid(self, form, customerpet_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        customerpet_form.instance = self.object
        customerpet_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, customerpet_form, helper):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, helper=helper,
                                  customerpet_form=customerpet_form,
                                  ))

class CustomerDelete(DeleteView):
    model=Customer
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super(CustomerDelete, self).get_context_data(**kwargs)
        context.update({
            'form': CustomerDeleteForm(),
        })
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CustomerDelete, self).dispatch(*args, **kwargs)

class CustomerListView(ListView):
    model=Customer
    paginate_by = 10
    context_object_name = "customer_list"

    def get_context_data(self, **kwargs):
        context = super(CustomerListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        return context

    def get_queryset(self):
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            self.query_string = self.request.GET['q']
            entry_query = get_query(self.query_string, ['last_name','first_name', 'home_phone','work_phone'])
            objects=Customer.objects.filter(entry_query).order_by('last_name','first_name')
        else:
            self.query_string=None
            objects=Customer.objects.all()
        return objects

    def get(self, request, *args, **kwargs):
        if 'submit' in request.GET:
            return HttpResponseRedirect('/customer/create')
        return super(CustomerListView,self).get(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CustomerListView, self).dispatch(*args, **kwargs)


# Pet Model views


class PetDelete(DeleteView):
    model=Pet
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('pet_list')

    def get_context_data(self, **kwargs):
        context = super(PetDelete, self).get_context_data(**kwargs)
        context.update({
            'form': PetDeleteForm(),
        })
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PetDelete, self).dispatch(*args, **kwargs)

class PetUpdate(UpdateView):
    model=Pet
    form_class=PetForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pet_list')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PetUpdate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PetUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('freetime',
                                    kwargs={'pk': self.get_object().id})

        return context

class PetListView(ListView):
    model=Pet
    paginate_by = 10
    context_object_name = "pet_list"

    def get_context_data(self, **kwargs):
        context = super(PetListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        return context

    def get_queryset(self):
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            self.query_string = self.request.GET['q']
            entry_query = get_query(self.query_string, ['name','breed__breed','owner__last_name','owner__first_name'])
            objects=Pet.objects.filter(entry_query).order_by('name')
        else:
            self.query_string=None
            objects=Pet.objects.all()
        return objects

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PetListView, self).dispatch(*args, **kwargs)

# Utility Views
@login_required(login_url='/login/')
def time_view(request):
    return render_to_response("time.html")

def logout_view(request):
    return logout_then_login(request, login_url='/login/')

def login_view(request,next="/",what=""):
    return render(request, 'login.html')

def auth_view(request):
    username = request.POST.get('Username',"")
    password = request.POST.get('Password',"")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        #return HttpResponse("%s logged in"%user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Bad!!! Go away...")

@login_required(login_url='/login/')
def home_view(request):
    now=datetime.datetime.now().isoformat()+"+05:00"
    today=datetime.date.today().isoformat()+' 00:00:00.0-05:00'
    tomorrow=datetime.date.today()+datetime.timedelta(days=1)
    tomorrow=tomorrow.isoformat()+' 00:00:00.0-05:00'
    now.replace("T"," ")
    appts =(Appointment.objects.filter(when__gt=today,when__lt=tomorrow))
    lastentered=(Appointment.objects.order_by("-pk"))[:5]
    calls =(Call.objects.order_by('id').reverse())[:5]
    for call in calls:
        if call.customer_id==-1:
            try:
                cust=Customer.objects.get(home_phone=call.phone_number)
            except:
                cust=None
            if cust:
                call.customer=cust

    return render_to_response("home.html",{'calls': calls, 'appts':appts, 'last':lastentered},context_instance=RequestContext(request))

def google_connect():
    import pickle
    import base64
    user=User.objects.get(id=1)
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    cred = storage.get()
    if cred is not None:
        credential=pickle.loads(base64.b64decode(cred))
    else:
        credential=None
    if credential is None or credential.invalid == True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                       user)
        authorize_url = FLOW.step1_get_authorize_url()
        HttpResponseRedirect(authorize_url)
    else:
        http = credential.authorize(httplib2.Http())
        service = build("calendar", "v3", http=http)
        return service

@login_required
def auth_return(request):
      if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'].encode(),
                                     request.user):
            return  HttpResponseBadRequest()
      credential = FLOW.step2_exchange(request.REQUEST)
      storage = Storage(CredentialsModel, 'id', request.user, 'credential')
      storage.put(credential)

      return HttpResponseRedirect("/customers")

def calendar(request):
    return HttpResponseRedirect("calendar.google.com")

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search_customers keywords within a model by testing the given search_customers fields.

    '''
    query = None # Query to search_customers for every search_customers term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search_customers for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

# Breed Model views

class BreedDelete(DeleteView):
    model=Breed
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('breed_list')

    def get_context_data(self, **kwargs):
        context = super(BreedDelete, self).get_context_data(**kwargs)
        context.update({
            'form': BreedDeleteForm(),
        })
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BreedDelete, self).dispatch(*args, **kwargs)

class BreedListView(ListView):
    model=Breed
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(BreedListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        return context

    def get_queryset(self):
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            self.query_string = self.request.GET['q']
            entry_query = get_query(self.query_string, ['breed','size','description'])
            objects=Breed.objects.filter(entry_query).order_by('breed')
        else:
            self.query_string=None
            objects=Breed.objects.all()
        return objects

    def get(self, request, *args, **kwargs):
        if 'submit' in request.GET:
            return HttpResponseRedirect('/breed/create')
        return super(BreedListView,self).get(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BreedListView, self).dispatch(*args, **kwargs)

class BreedUpdateView(UpdateView):
    model=Breed
    template_name = 'customers/breed_update.html'
    form_class = BreedForm
    success_url = '/breeds'

    def get_context_data(self, **kwargs):
        context = super(BreedUpdateView,self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context['helper']=form.helper
        return context

    def post(self, request, *args, **kwargs):
        self.object = Breed.objects.get(pk=kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            if request.POST.get('picture-clear',False):
                self.object.picture=None
            elif request.POST.get('picture',False):
                self.object.picture=request.POST['picture']
            self.object.save()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BreedUpdateView, self).dispatch(*args, **kwargs)

class BreedCreateView(CreateView):
    model=Breed
    template_name = 'customers/breed_create.html'
    form_class = BreedForm
    success_url = '/breeds'

    def get_context_data(self, **kwargs):
        context = super(BreedCreateView,self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BreedCreateView, self).dispatch(*args, **kwargs)

# Service Model views

class ServiceDelete(DeleteView):
    model=Service
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('service_list')

    def get_context_data(self, **kwargs):
        context = super(ServiceDelete, self).get_context_data(**kwargs)
        context.update({
            'form': ServiceDeleteForm(),
        })
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiceDelete, self).dispatch(*args, **kwargs)

class ServiceListView(ListView):
    model=Service
    paginate_by = 10
    context_object_name = "service_list"

    def get_context_data(self, **kwargs):
        context = super(ServiceListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        return context

    def get_queryset(self):
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            self.query_string = self.request.GET['q']
            entry_query = get_query(self.query_string, ['service','size','price','description'])
            objects=Service.objects.filter(entry_query).order_by('service','-price')
        else:
            self.query_string=None
            objects=Service.objects.all()
        return objects

    def get(self, request, *args, **kwargs):
        if 'submit' in request.GET:
            return HttpResponseRedirect('/service/create')
        return super(ServiceListView,self).get(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiceListView, self).dispatch(*args, **kwargs)
    
class ServiceUpdateView(UpdateView):
    model=Service
    template_name = 'customers/service_update.html'
    form_class = ServiceForm
    success_url = '/services'

    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView,self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiceUpdateView, self).dispatch(*args, **kwargs)
    
class ServiceCreateView(CreateView):
    model=Service
    template_name = 'customers/service_create_form.html'
    form_class = ServiceForm
    success_url = '/services'

    def get_context_data(self, **kwargs):
        context = super(ServiceCreateView,self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiceCreateView, self).dispatch(*args, **kwargs)

# Appointment Model views

class AppointmentUpdate(UpdateView):
    model=Appointment
    form_class=AppointmentForm
    template_name_suffix = '_service_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = Appointment.objects.get(pk=kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        appointmentservice_form = AppointmentServiceFormSet(instance=self.object)
        helper = AppointmentServiceFormSetHelper()
        pet=Pet.objects.get(pk=self.object.pet_id)

        self.success_url = '/appointments/?when=Future&pet={}'.format(self.object.pet_id)
        return self.render_to_response(
            self.get_context_data(form=form,helper=helper,
                                  formset=appointmentservice_form,pet=pet
            ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = Appointment.objects.get(pk=kwargs['pk'])
        pet=Pet.objects.get(pk=self.object.pet_id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        appointmentservice_form = AppointmentServiceFormSet(self.request.POST,instance=self.object)
        helper = AppointmentServiceFormSetHelper()
        self.success_url = '/appointments/?when=Future&pet={}'.format(self.object.pet_id)
        if form.is_valid() and appointmentservice_form.is_valid():
            todo=""
            total=0
            for f in appointmentservice_form:
                doit=False
                svc=None
                price = 0.0
                for fld in f:
                    if fld.name=="price":
                        price=fld.data
                    if fld.name=="service":
                        svc=Service.objects.get(pk=fld.data)
                    if fld.name=="do_it" and fld.data:
                        doit=True

                if doit:
                    dash=", "
                    if len(todo)<1:
                        dash=""
                    todo+=dash+svc.service
                    total+=float(price)
            self.object.todo = todo
            self.object.total = total
            google=google_connect()
            event=google.events().get(calendarId='primary',eventId=self.object.gcalid).execute()
            event['summary']+=" : "+todo
            google.events().update(calendarId='primary',eventId=event['id'],body=event).execute()
            return self.form_valid(form, appointmentservice_form)
        else:
            return self.form_invalid(form, appointmentservice_form, helper, pet)

    def form_valid(self, form, appointmentservice_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        appointmentservice_form.instance = self.object
        appointmentservice_form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, appointmentservice_form, helper, pet):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, helper=helper,
                                  formset=appointmentservice_form,pet=pet
                                  ))

class AppointmentDelete(DeleteView):
    model=Appointment
    template_name_suffix = '_confirm_delete'

    def get_context_data(self, **kwargs):
        context = super(AppointmentDelete, self).get_context_data(**kwargs)
        context.update({
            'form': AppointmentDeleteForm(),
        })
        return context

    def get_success_url(self):
        self.google=google_connect()
        self.google.events().delete(calendarId='primary',eventId=self.object.gcalid).execute()
        return '/appointments/?when=Future&pet={}'.format(self.object.pet_id)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentDelete, self).dispatch(*args, **kwargs)

class AppointmentListView(ListView):
    model=Appointment
    template_name='customers/appointment_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(AppointmentListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        context["pet_id"]=self.pet_id
        context["pet_name"]=self.pet_name
        return context

    def get_queryset(self):
        now=datetime.datetime.now()
        self.pet_id=None
        self.pet_name=None
        if ('pet' in self.request.GET) and self.request.GET['pet'].strip():
            self.pet_id=self.request.GET['pet']
        if ('when' in self.request.GET) and self.request.GET['when'].strip():
            self.query_string = self.request.GET['when']
            if self.query_string == 'Future':
                if self.pet_id:
                    objects=Appointment.objects.filter(when__gt=now,pet=self.pet_id).order_by('when')
                    self.pet_name=Pet.objects.get(pk=self.pet_id)
                else:
                    objects=Appointment.objects.filter(when__gt=now).order_by('when')
            elif self.query_string == 'Past':
                if self.pet_id:
                    objects=Appointment.objects.filter(when__lte=now,pet=self.pet_id).order_by('-when')
                    self.pet_name=Pet.objects.get(pk=self.pet_id)
                else:
                    objects=Appointment.objects.filter(when__lte=now).order_by('-when')
        else:
            self.query_string=None
            objects=Appointment.objects.all()
        return objects

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentListView, self).dispatch(*args, **kwargs)

@login_required(login_url='/login/')
def make_appointment(request, petid, date, time):
    google=google_connect()
    pet=Pet.objects.get(pk=petid)
    petname=pet.name
    owner = pet.owner.name
    phone = pet.owner.home_phone
    breed = pet.breed
    size = pet.breed.size
    success_url="\appointment\pet\{}".format(petid)
    text="{} : {} : {} : {} : {} at {} on {}".format(petname, breed,size,owner,phone,time,date)
    appt = google.events().quickAdd(calendarId='primary',text=text)
    response = appt.execute()
    gcalid=response['id']
    dt=datetime.datetime.strptime("{} {}".format(date,time),"%Y-%m-%d %I:%M%p")
    when = dt.strftime("%Y-%m-%dT%H:%M:%S")
    appt=Appointment(pet=pet,when=when,gcalid=gcalid)
    appt.save()
    object = Appointment.objects.get(gcalid=gcalid)
    anyservices = Service.objects.filter(size='ANY')
    breedservices = Service.objects.filter(size=breed.size)
    services={}
    for svc in breedservices:
        services[svc.service]=svc
    for svc in anyservices:
        if svc.service not in services:
            services[svc.service]=svc
    for svc in services:
        s = services[svc]
        aptservice = AppointmentDetail(appointment=object, service=s, price=s.price)
        aptservice.save()
    return HttpResponseRedirect("/appointment/{}".format(appt.id))

@login_required(login_url='/login/')
def freetime(request,petid,weeks=0,next=None):

    if next is not None:
        weeks = int(weeks)+1
    google=google_connect()
    pet = Pet.objects.get(pk=petid)
    fromdays=7*int(weeks)
    moredays = 0
    if weeks==0 or weeks=='0':
        moredays = 7
    todays = 7+7*int(weeks)+moredays
    fromtime=datetime.date.today()+datetime.timedelta(days=fromdays)
    timeMin=fromtime.isoformat()+'T00:00:00.0-05:00'
    totime=datetime.datetime.now()+datetime.timedelta(days=todays)
    timeMax=totime.isoformat()+'-05:00'

    activities = google.events().list(calendarId='primary',singleEvents=True,timeMin=timeMin,timeMax=timeMax,timeZone='EST')
    activitylist = activities.execute()
    appointments=[]
    for item in activitylist['items']:
        starttime=datetime.datetime.strptime(item['start']['dateTime'][:-6], "%Y-%m-%dT%H:%M:%S").strftime("%A, %B %d, %Y %I:%M%p")
        startforsort=datetime.datetime.strptime(item['start']['dateTime'][:-6], "%Y-%m-%dT%H:%M:%S")
        endtime=datetime.datetime.strptime(item['end']['dateTime'][:-6], "%Y-%m-%dT%H:%M:%S")#.strftime("%A, %B %d, %Y %I:%M%p")
        try:
            summary = item['summary']
        except KeyError:
            summary = 'No description'
        try:
            colorid = item['colorId']
        except KeyError:
            colorid = None
        if colorid is None:
            appointments.append((startforsort, endtime,starttime,  summary))
    bigdogs={}
    day=None
    for apt in appointments:
        aptday = apt[0].date()
        summary=apt[3]
        if aptday != day:
            day=aptday
            bigdogs[day]={}
            bigdogs[day]["am"]=0
            bigdogs[day]["pm"]=0
        if " XL" in summary or " LG" in summary:
            if endtime.strftime("%H")<='12':
                bigdogs[day]["am"]+=1
            else:
                bigdogs[day]["pm"]+=1


    requestbody={"timeMin": timeMin,
                 "timeMax": timeMax,
                 "timeZone": "EST",
                 "items":[{"id": settings.CALENDAR_ID }]}
    busyrequest = google.freebusy().query(body=requestbody)
    busy=busyrequest.execute()
    b1 = busy["calendars"]
    b2 = b1[settings.CALENDAR_ID]
    b3 = b2['busy']

    beginday=datetime.time(8,0)
    endday=datetime.time(17,0)
    opentimes={}
    busytime={}
    for endstart in b3:
        enddt=datetime.datetime.strptime(endstart['end'][:-6], "%Y-%m-%dT%H:%M:%S")
        startdt=datetime.datetime.strptime(endstart['start'][:-6], "%Y-%m-%dT%H:%M:%S")
        date = enddt.date()#.strftime("%A, %B %d, %Y")
        dow=date.strftime("%a")
        if not ((dow=='Sat' or dow=='Sun') and pet.breed.size=='XL'):
            busytime.setdefault(date,[]).append([startdt.time(),enddt.time()])
    for date in sorted(busytime):
        hour = beginday.hour
        while hour < endday.hour:
            slot = datetime.time(hour,0)
            slotfree=True
            for busy in busytime[date]:
                ampm = "am"
                if hour>11:
                    ampm="pm"
                if pet.breed.size in ("XL","LG") and bigdogs.get(date,{}).get(ampm,0)>1:
                    slotfree=False
                    break
                if busy[0]<=slot<busy[1]:
                    slotfree = False
                    break
            if slotfree:
                opentimes.setdefault(date, []).append(slot.strftime("%I:%M%p"))
            hour +=1
    most=0
    header=[]

    for day in sorted(opentimes):
        header.append(day)
    maxslots=0
    for day in header:
       if len(opentimes[day])>maxslots:
           maxslots=len(opentimes[day])
    rows=[]
    for row in range(maxslots):
        rows.append([])
        for day in header:
            try:
                slot = (day.strftime("%Y-%m-%d"),opentimes.get(day)[row])
            except IndexError:
                slot=''
            rows[row].append(slot)
    wdheader=[]
    for day in header:
        wdheader.append(day.strftime("%A, %B %d, %Y"))

    return render_to_response('customers/free_time.html', {'dates': wdheader, 'opentimes': rows, 'petname': pet.name, 'petid':pet.id, 'weeks':weeks})

# Calls Model Views

class CallListView(ListView):
    model=Call
    paginate_by = 10
    context_object_name = "call_list"

    def get_context_data(self, **kwargs):
        context = super(CallListView,self).get_context_data(**kwargs)
        context["query_string"]=self.query_string
        return context

    def get_queryset(self):
        calls=Call.objects.filter(customer_id=-1)
        for call in calls:
            try:
                cust = Customer.objects.get(home_phone=call.phone_number)
            except:
                cust = None
            if cust is not None:
                call.customer=cust
                call.save()

        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            self.query_string = self.request.GET['q']
            entry_query = get_query(self.query_string, ['customer__last_name','customer__first_name','phone_number','caller_id_name','rang_at'])
            objects=Call.objects.filter(entry_query).order_by('-rang_at')
        else:
            self.query_string=None
            objects=Call.objects.all().order_by('-rang_at')
        return objects

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CallListView, self).dispatch(*args, **kwargs)


