from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "index.html")
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form":form})