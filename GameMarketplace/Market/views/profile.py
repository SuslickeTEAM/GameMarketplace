from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from ..models import *


@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'Market/profile.html', {'user': user})