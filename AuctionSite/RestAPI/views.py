from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def Login(request):
    if request.user.is_authenticated:
        return render(request, 'loggedin.html')
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'index.html', {'error': 'Invalid Username/Password or account not activated, Please confirm your email ID.'})
        # TO CHECK VENDOR OR BIDDER INSIDE VIEW
        # for group in request.user.groups.all:
        #     if group.name == 'bidder':
        #         return render(request, 'bidderwelcome.html')
        #     elif group.name =='vendor':
        #         return render(request, 'vendorwelcome.html')
        return render(request, 'loggedin.html')
    else:
        return redirect('index')

