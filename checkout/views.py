from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
import datetime
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        
        if order_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = 1,
                    currency = "GBP",
                    description = request.user.email,
                    card = form.cleaned_data['stripe_id'],
                )
                
                form.save()
                #redirect('/checkout_success')
            except stripe.error.CardError:
                form.add_error("Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid!")
                
    else:
        form = OrderForm()
            
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['publishable'] = settings.STRIPE_PUBLISHABLE
    args['months'] = range(1, 12)
    args['years'] = range(2018, 2036)
    args['soon'] = datetime.date.today() + datetime.timedelta(days=30)
    
    return render(request, "checkout.html", args)
    
    