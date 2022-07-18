from django.shortcuts import render, redirect
from .forms import NewOrderForm, FeedbackForm
from .models import OrderDB, FeedbackDB
from datetime import datetime
from account.models import User
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

distance = 0


def BillGeneration(request):
    global distance
    source = int(request.GET.get('so'))
    destination = int(request.GET.get('de'))
    weight = int(request.GET.get('weight'))
    distance = 4  # use google api get distance between source and destination
    bill = (20+(distance*10)+(weight*4))

    return JsonResponse({'newval': bill}, status=200)


def NewOrder(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewOrderForm(request.POST)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.user = request.user
                newform.pick_name = request.user.first_name
                newform.distance = distance
                newform.save()
                return redirect('myorders')
            return render(request, 'order_form.html', {'form': form})
        else:
            form = NewOrderForm()
            return render(request, 'order_form.html', {'form': form})
    else:
        return redirect('login')


def MyOrders(request):
    if request.user.is_authenticated:
        orders = OrderDB.objects.filter(
            user=request.user).order_by('order_time').reverse()
        return render(request, 'myorders.html', {'orders': orders})
    else:
        return redirect('login')


def SendToOrder(request):
    form = NewOrderForm(request.GET)
    return render(request, "order_form.html", {'form': form})


def CancelOrder(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = OrderDB.objects.filter(order_id=oid)
            obj.update(status='cancelled', cancelled_time=datetime.now())
            return redirect('myorders')
        else:
            return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def AvailableOrders(request):
    if request.user.is_authenticated:
        if request.user.is_agent:
            obj = OrderDB.objects.filter(
                status='pending').order_by('order_time').reverse()
            return render(request, 'available_order.html', {'orders': obj})
        else:
            return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})
    else:
        return redirect('login')


def Accept(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_agent:
                obj = OrderDB.objects.filter(order_id=oid)
                obj.update(status='accepted',
                           accepted_time=datetime.now(), agent=request.user)
                return redirect('acceptedorder')
            else:
                return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})
        return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def Picked(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_agent:
                obj = OrderDB.objects.filter(order_id=oid)
                obj.update(status='picked', picked_time=datetime.now(),pamyment_time=datetime.now())
                return redirect('acceptedorder')
            else:
                return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})
        return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def AcceptedOrders(request):
    if request.user.is_authenticated:
        if request.user.is_agent:
            obj = OrderDB.objects.filter(
                agent=request.user).order_by('order_time').reverse()
            return render(request, 'accepted_order.html', {'orders': obj})
        else:
            return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})
    else:
        return redirect('login')


def Delivered(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_agent:
                obj = OrderDB.objects.filter(order_id=oid)
                obj.update(status='completed', completed_time=datetime.now(
                ))
                return redirect('acceptedorder')
            else:
                return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})
        else:
            return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def OrderDetail(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = OrderDB.objects.get(order_id=oid)
            if obj.agent_id:
                aid = obj.agent_id
                agent = User.objects.get(id=aid)
                return render(request, 'view_order_details.html', {'order': obj, 'agent': agent})
            else:
                return render(request, 'view_order_details.html', {'order': obj})
        else:
            return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def Feedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            oid = request.POST['order_id']
            feedback = request.POST['feedback']
            if FeedbackDB.objects.filter(order_id=oid).exists():
                obj = FeedbackDB.objects.filter(order_id=oid)
                obj.update(feedback=feedback)
                return redirect('myorders')
            if form.is_valid():
                newobj = form.save(commit=False)
                newobj.datetime = datetime.now()
                newobj.save()
                return redirect('myorders')
        else:
            return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')


def FeedbackTake(request, oid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if FeedbackDB.objects.filter(order_id=oid).exists():
                fb = FeedbackDB.objects.get(order_id=oid)
                form = FeedbackForm(
                    initial={'order_id': oid, 'feedback': fb.feedback})
                return render(request, 'feedback.html', {'form': form})
            else:
                form = FeedbackForm(initial={'order_id': oid})
                return render(request, 'feedback.html', {'form': form})
        else:
            return render(request, "error.html", {'error': '404 Page Not found'})
    else:
        return redirect('login')
