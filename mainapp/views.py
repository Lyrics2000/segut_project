from django.shortcuts import redirect, render
from django.http import Http404
from datetime import datetime
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import Booking
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
from .models import (
    SLiderPanel,
    AboutUs,
    AboutUsValues,
    OurServices,
    BusStop,
    TravelSChedule,
    ContactUs
)

def index(request):
    slider =  SLiderPanel.objects.all()
    latest_abt =  AboutUs.objects.last()
    about_us_values =  AboutUsValues.objects.all()
    our_services =  OurServices.objects.all()
    context = {
        'slider':  slider,
        'about_us' :  latest_abt,
        'about_us_values' :  about_us_values,
        'our_services' :  our_services
    }
    return render(request,'index.html',context)


def car_book(request):
    all_bus_stop =  BusStop.objects.all()
    travel_schedule =  TravelSChedule.objects.all()

    context = {
        'all_bus_stop' :  all_bus_stop,
        'travel_schedule' :  travel_schedule
    }
    return render(request,'gallery.html',context)


def detailed_page(request):
    if request.method == "POST":
        try:
            inDate = request.POST.get("departure_date")
            # d = datetime.strptime(inDate, "%m,%d,%Y,%H:%M")
            # print(d)
            travel_filtered = TravelSChedule.objects.get(starting_point=request.POST.get("form"),destination=request.POST.get("to"),type=request.POST.get("vehicle_type"))
            context = {
                'travel_filtered' :  travel_filtered
            }
            return render(request,'detailed_page.html',context)
        except TravelSChedule.DoesNotExist:
            return render(request,'page_not_found.html')
    return render(request,'detailed_page.html')


@login_required(login_url="account:sign_in")
def booking(request):
    if request.method == "POST":
        all_on = []
        one =  request.POST.get('01')
        two =  request.POST.get('02')
        three =  request.POST.get('03')
        four = request.POST.get('04')
        five =  request.POST.get('05')
        six =  request.POST.get('06')
        seven =  request.POST.get('07')
        eight =  request.POST.get('08')
        nine =  request.POST.get('09')
        ten =  request.POST.get('10')
        eleven =  request.POST.get('11')
        twelve =  request.POST.get('12')
        thirteen =  request.POST.get('13')
        fourteen =  request.POST.get('14')
        travel_id =  request.POST.get('travel_id')
        travel_obj =  TravelSChedule.objects.get(id =  travel_id)
        if  one == 'on':
            all_on.append('01')
        if two == 'on':
            all_on.append('02')
        if three == 'on':
            all_on.append('03')
        if four == 'on':
            all_on.append('04')

        if five == 'on':
            all_on.append('05')

        if six == 'on':
            all_on.append('06')
        
        if seven == 'on':
            all_on.append('07')

        if eight == 'on':
            all_on.append('08')

        if nine ==  'one':
            all_on.append('09')
        if ten == 'on':
            all_on.append('10')
        if eleven == 'on':
            all_on.append('11')

        if twelve == 'on' :
            all_on.append('12')
        if thirteen == 'on':
            all_on.append('13')

        if fourteen ==  'on':
            all_on.append('14')

        user_id = request.user.id
        user_obj =  User.objects.get(id= user_id)
        booking = Booking.objects.create(
            user_id =  user_obj,
            schedule_id =  travel_obj,
            number_of_seats =  len(all_on),
            seat_ids =  str(all_on),
            fare_amount = travel_obj.fare_amount,
            total_amount = len(all_on) * travel_obj.fare_amount


        )
        request.session['booking_id'] = booking.id

        return redirect('mainapp:mpesa_pay')

     
    return render(request,'booking.html')



@login_required(login_url="account:sign_in")
def mpesa_pay(request):
    booking =  request.session.get('booking_id')
    booking_obj = Booking.objects.get(id = booking)

    context = {
        'booking' :  booking_obj
    }
    return render(request,'booking_summary.html',context)


def about_us(request):
    latest_abt =  AboutUs.objects.last()
    context = {
        'about_us' :  latest_abt
    }
    return render(request,'about_us.html',context)


def contact_us(request):
    if request.method == "POST":
        ContactUs.objects.create(
            name = request.POST.get("name"),
            email =  request.POST.get("email"),
            phone =  request.POST.get("phone"),
            subject =  request.POST.get("subject"),
            message =  request.POST.get("message") 

        )
        # email_subject = 'Contact Us'
        # user =  request.user
        # current_site = get_current_site(request)
        # message = render_to_string('contact_us_booking.html', {
        # 'user': user,
        # 'domain': current_site.domain,
        # })
        # to_email = user.email
        # email = EmailMessage(email_subject, message, to=[to_email])
        # email.send()

        return redirect("/")
    
    return render(request,'contact_us.html')



