from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from . models import companies

# Create your views here.

def tutorial(request):
    return render(request, 'tutorial.html')

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            context["error"] = "Invalid credentials"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

def user_register(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                context["exists"] = "Username already taken"
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return HttpResponseRedirect(reverse('user_login'))

        else:
            context["nomatch"] = "Passwords do not match"
    return render(request, 'register.html', context)

@login_required(login_url="/login/")
def dashboard(request):
    comps = companies.objects.filter(user=request.user)

    context = {}
    context["user"] = request.user
    context["comp_list"] = comps
    return render(request, 'dashboard.html', context)

@login_required(login_url="/login/")
def add_company(request):
    context = {}
    if request.method == "GET":
        return render(request, 'input.html')
    if request.method == "POST":
        user = request.user
        rp = request.POST
        stock_name = rp['stock_name']
        industry = rp['industry']
        cmp = rp['cmp']
        date = rp['date']
        eps1 = rp['eps1']
        eps2 = rp['eps2']
        eps3 = rp['eps3']
        eps4 = rp['eps4']
        eps5 = rp['eps5']
        eps6 = rp['eps6']
        eps7 = rp['eps7']
        eps8 = rp['eps8']
        eps9 = rp['eps9']

        cpe = rp['cpe']
        ipe = rp['ipe']
        pe1 = rp['pe1']
        pe2 = rp['pe2']
        pe3 = rp['pe3']
        pe4 = rp['pe4']
        pe5 = rp['pe5']
        pe6 = rp['pe6']
        pe7 = rp['pe7']
        pe8 = rp['pe8']
        pe9 = rp['pe9']
        bv = rp['bv']
        der = rp['der']
        fcf = rp['fcf']
        sales = rp['sales']
        market_cap = rp['market_cap']
        input_data = companies.objects.create(
            user=user, stock_name=stock_name, industry=industry, cmp=cmp, date=date, eps1=eps1, eps2=eps2, eps3=eps3,
            eps4=eps4, eps5=eps5, eps6=eps6, eps7=eps7, eps8=eps8, eps9=eps9, cpe=cpe, ipe=ipe, pe1=pe1,
            pe2=pe2, pe3=pe3, pe4=pe4, pe5=pe5, pe6=pe6, pe7=pe7, pe8=pe8, pe9=pe9, bv=bv, der=der, fcf=fcf, sales=sales,
            market_cap=market_cap
        )
        input_data.save()
        return HttpResponseRedirect(reverse('dashboard'))
    #else:
     #   return render(request, 'input.html')


@login_required(login_url="/login/")
def details(request, id=None):
    context = {}
    comp_list = companies.objects.get(id=id)
    context["list"] = comp_list
    growth_rate = (((context["list"].eps1/context["list"].eps9)**0.12)-1)*100
    context["f_eps"] = growth_rate
    av = (context["list"].pe1 + context["list"].pe2 +context["list"].pe3 + context["list"].pe4 + context["list"].pe5 +
    context["list"].pe6 + context["list"].pe7 + context["list"].pe8 + context["list"].pe9)/ 9
    context["average_pe"] = av
    pegr = (((context["list"].pe1/context["list"].pe9)**0.12)-1)*100
    context["pegr"] = pegr
    bpe = av + pegr
    context["bpe"] = bpe
    iv = av * context["list"].eps1
    context["iv"] = iv
    mov = bpe * context["list"].eps1
    context["mov"] = mov
    peg = context["list"].pe1/growth_rate
    context["peg"] = peg
    pbr = context["list"].cmp/context["list"].bv
    context["pbr"] = pbr
    roe = (context["list"].eps1/context["list"].bv)*100
    context["roe"] = roe
    psr = context["list"].market_cap/context["list"].sales
    context["psr"] = psr
    ccgp = context["list"].cmp/iv
    pro_eps = (((1+0.15)**1)*context["list"].eps1)
    context["pro_eps"] = pro_eps
    ipe = pro_eps * av
    pp = ipe * pro_eps
    opcg = pp - context["list"].cmp
    print(opcg)
    cagr = (((((context["list"].cmp + opcg) / context["list"].cmp)**1)-1))
    context["cagr"] = cagr
    return render(request, 'detail.html', context)