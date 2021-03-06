from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import OrderForm
from django.conf import settings
from django.utils import timezone
import datetime
#import stripe


# Create your views here.

#stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method=="POST":
        print(request.POST)
        print(request.POST.get('e-mail'))
        print(request.POST.get('full_name'))
        print(request.POST.get('amount'))
        form = OrderForm(request.POST)
        
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.e-mail,
                    card = form.cleaned_data['stripe_id'],
                )
                
                form.save()
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid!")
            
            print(messages)
                
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
    
    
def pay(request):
    return render(request, 'checkout.html')
    

def predict(request):
    return render(request, 'predict.html')
    


    
    