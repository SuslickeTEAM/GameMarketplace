from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


from ..models import *


@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user)
    if not Profile.objects.filter(user=user).exists():
        Profile.objects.create(user=user)
    profile = get_object_or_404(Profile, user_id=user.id)
    
    history = PurchaseHistory.objects.prefetch_related('product').filter(user=user).order_by('-created_at')[:7]
    return render(request, 'Market/profile.html', {'user': user, 'profile': profile, 'history':history, 'body_class': 'profile-bg'})


@login_required
def get_data(request, history_id):
    history = PurchaseHistory.objects.get(pk=history_id).details.all()
    user = []
    for histor_data in history:
        data = {
            'login': f'{histor_data.login}',
            'password': f'{histor_data.password}'
        }
        user.append(data)
    # json_data = json.dumps(user, ensure_ascii=False, sort_keys=True, separators=(',', ': '), default=str)
    # print(json_data)
    return JsonResponse(user, safe=False)