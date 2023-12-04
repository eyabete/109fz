# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Purchase  # Import the model representing user purchases

@login_required
def user_purchases(request):
    # Retrieve user purchases from the database
    purchases = Purchase.objects.filter(user=request.user)

    context = {
        'purchases': purchases
    }

    return render(request, 'user_purchases.html', context)
