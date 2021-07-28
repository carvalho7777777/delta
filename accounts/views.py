from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# models:


# forms:
from accounts.forms import UserAdminCreationForm
from django.contrib.auth.forms import UserCreationForm



@login_required()
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:register')
    return render(req, 'register.html', {'form': form})