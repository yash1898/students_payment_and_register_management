from django.shortcuts import render
from .models import *
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def view_page(request):
    return render(request,'view_page.html')
    
@login_required(login_url = "/register/login/")
def Register_View(request):
    error=""
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        s = request.POST['std']
        total_fee=request.POST['total_fee']
        fee_recieved=request.POST['fee_recieved']
        

        a=int(total_fee)-int(fee_recieved)
        b=int(fee_recieved)

        if int(total_fee)-int(fee_recieved) == 0:
            fees=True
            partial_fee=False
        
        
        elif  a != 0 and b != 0:
            partial_fee=True
            fees=False
        else:
            fees=False
            partial_fee=False
        try:
            Register.objects.create(first_name=f,last_name=l,std=s,fees=fees,partial_fee=partial_fee,total_fee=total_fee,fee_recieved=fee_recieved)
            error='no'
        except:
            error="yes"
    d={'error':error}
    return render(request,'Register.html',d)

@login_required(login_url = "/register/login/")
def view_students(request):
    students = Register.objects.all()
    f=0
    for i in students:
        f+=1
    d={'students':students,'f':f}
    return render(request,'view_students.html',d)

@login_required(login_url = "/register/login/")
def view_first_students(request):
    students = Register.objects.filter(std='First')
    f=0
    for i in students:
        f+=1
    d={'students':students,'f':f}
    return render(request,'view_first_students.html',d)

@login_required(login_url = "/register/login/")
def view_second_students(request):
    students = Register.objects.filter(std='Second')
    f=0
    for i in students:
        f+=1
    d={'students':students,'f':f}
    return render(request,'view_second_students.html',d)

@login_required(login_url = "/register/login/")
def view_third_students(request):
    students = Register.objects.filter(std='Third')
    f=0
    for i in students:
        f+=1
    d={'students':students,'f':f}
    return render(request,'view_third_students.html',d)

@login_required(login_url = "/register/login/")
def view_forth_students(request):
    students = Register.objects.filter(std='Forth')
    f=0
    for i in students:
        f+=1
    d={'students':students,'f':f}
    return render(request,'view_forth_students.html',d)

@login_required(login_url = "/register/login/")
def edit_students(request, pid):
    error=""
    students = Register.objects.get(id=pid)
    i=students.fee_recieved
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        s = request.POST['std']
        fee_recieved1=request.POST['fee_recieved']
        fee_recieved = i+int(fee_recieved1)

        a=students.total_fee-fee_recieved
        b=fee_recieved

        if students.total_fee-fee_recieved == 0:
            fees=True
            partial_fees=False
        
        elif a != 0 and b != 0:
            partial_fees=True
            fees=False
        else:
            fees=False
            partial_fees=False
        try:
            Register.objects.filter(id=pid).update(first_name=f,last_name=l,std=s,fees=fees,fee_recieved=fee_recieved,partial_fee=partial_fees,date=datetime.now())
            error='no'
        except:
            error="yes"
    remain=students.total_fee-students.fee_recieved
    d={'students':students,'remain':remain,'error':error}
    return render(request,'edit_students.html',d)

@login_required(login_url = "/register/login/")
def delete_students(request,pid):
    error=""
    try:
        students=Register.objects.get(id=pid)
        students.delete()
        error='deleted'
    except:
        error="not_deleted"
    d={'error':error}
    return render(request,'view_students.html',d)

@login_required(login_url = "/register/login/")
def view_detail(request,pid):
    students=Register.objects.get(id=pid)
    remain=students.total_fee-students.fee_recieved
    d={'students':students,'remain':remain}
    return render(request,'view_detail.html',d)

@login_required(login_url = "/register/login/")
def payment(request):
    message=""
    zero=0
    remain=0
    remain1=0
    remain2=0
    remain3=0
    remain4=0
    students = Register.objects.all()
    f=Register.objects.aggregate(Sum('fee_recieved'))
    t=Register.objects.aggregate(Sum('total_fee'))
    t1=Register.objects.filter(std='First').aggregate(Sum('total_fee'))
    t2=Register.objects.filter(std='Second').aggregate(Sum('total_fee'))
    t3=Register.objects.filter(std='Third').aggregate(Sum('total_fee'))
    t4=Register.objects.filter(std='Forth').aggregate(Sum('total_fee'))
    f1=Register.objects.filter(std='First').aggregate(Sum('fee_recieved'))
    f2=Register.objects.filter(std='Second').aggregate(Sum('fee_recieved'))
    f3=Register.objects.filter(std='Third').aggregate(Sum('fee_recieved'))
    f4=Register.objects.filter(std='Forth').aggregate(Sum('fee_recieved'))
    p=Register.objects.filter(fees=True).count()
    up=Register.objects.filter(fee_recieved=0).count()
    p1=Register.objects.filter(fees=True,std='First').count()
    up1=Register.objects.filter(fee_recieved=0,std='First').count()
    p2=Register.objects.filter(fees=True,std='Second').count()
    up2=Register.objects.filter(fee_recieved=0,std='Second').count()
    p3=Register.objects.filter(fees=True,std='Third').count()
    up3=Register.objects.filter(fee_recieved=0,std='Third').count()
    p4=Register.objects.filter(fees=True,std='Forth').count()
    up4=Register.objects.filter(fee_recieved=0,std='Forth').count()
    students1=Register.objects.filter(std='First')
    students2=Register.objects.filter(std='Second')
    students3=Register.objects.filter(std='Third')
    students4=Register.objects.filter(std='Forth')
    
    count=0
    for i in students:
        if(i.total_fee != i.fee_recieved and i.fee_recieved != 0):
            count+=1

    count1=0
    for i in students1:
        if(i.total_fee != i.fee_recieved and i.fee_recieved != 0):
            count1+=1

    count2=0
    for i in students2:
        if(i.total_fee != i.fee_recieved and i.fee_recieved != 0):
            count2+=1

    count3=0
    for i in students3:
        if(i.total_fee != i.fee_recieved and i.fee_recieved != 0):
            count3+=1

    count4=0
    for i in students4:
        if(i.total_fee != i.fee_recieved and i.fee_recieved != 0):
            count4+=1

    try:
        remain=t['total_fee__sum']-f['fee_recieved__sum']
        zero=0
    except:
        message='None'

    try:
        remain1=t1['total_fee__sum']-f1['fee_recieved__sum']
        zero=0
    except:
        message='None'

    try:
        remain2=t2['total_fee__sum']-f2['fee_recieved__sum']
        zero=0
    except:
        message='None'
    
    try:
        remain3=t3['total_fee__sum']-f3['fee_recieved__sum']
        zero=0
    except:
        message='None'

    try:
        remain4=t4['total_fee__sum']-f4['fee_recieved__sum']
        zero=0
    except:
        message='None'

    d={'f':f,'f1':f1,'f2':f2,'f3':f3,'f4':f4,'t':t,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'remain':remain,'remain1':remain1,'remain2':remain2,'remain3':remain3,'remain4':remain4,'message':message,'p':p,'up':up,'count':count,'p1':p1,'up1':up1,'p2':p2,'up2':up2,'up3':up3,'p3':p3,'p4':p4,'up4':up4,'count1':count1,'count2':count2,'count3':count3,'count4':count4}
    return render(request,'payment.html',d)

@login_required(login_url = "/register/login/")
def paid_fees(request):
    paid_students=Register.objects.filter(fees=True)
    d={'paid_students':paid_students}
    return render(request,'paid_fees.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_zero(request):
    paid_studentsz=Register.objects.filter(fee_recieved=0)
    d={'paid_studentsz':paid_studentsz}
    return render(request,'paid_fees_zero.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_partial(request):
    paid_studentsp=Register.objects.filter(partial_fee=True)
    d={'paid_studentsp':paid_studentsp}
    return render(request,'paid_fees_partial.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_first(request):
    paid_students_first=Register.objects.filter(fees=True,std='First')
    d={'paid_students_first':paid_students_first}
    return render(request,'paid_fees_first.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_first_partial(request):
    paid_students_first_partial=Register.objects.filter(partial_fee=True,std='First')
    d={'paid_students_first_partial':paid_students_first_partial}
    return render(request,'paid_fees_first_partial.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_firstz(request):
    paid_students_firstz=Register.objects.filter(fee_recieved=0,std='First')
    d={'paid_students_firstz':paid_students_firstz}
    return render(request,'paid_fees_firstz.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_second(request):
    paid_students_second=Register.objects.filter(fees=True,std='Second')
    d={'paid_students_second':paid_students_second}
    return render(request,'paid_fees_second.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_second_partial(request):
    paid_students_second_partial=Register.objects.filter(partial_fee=True,std='Second')
    d={'paid_students_second_partial':paid_students_second_partial}
    return render(request,'paid_fees_second_partial.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_secondz(request):
    paid_students_secondz=Register.objects.filter(fee_recieved=0,std='Second')
    d={'paid_students_secondz':paid_students_secondz}
    return render(request,'paid_fees_secondz.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_third(request):
    paid_students_third=Register.objects.filter(fees=True,std='Third')
    d={'paid_students_third':paid_students_third}
    return render(request,'paid_fees_third.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_third_partial(request):
    paid_students_third_partial=Register.objects.filter(partial_fee=True,std='Third')
    d={'paid_students_third_partial':paid_students_third_partial}
    return render(request,'paid_fees_third_partial.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_thirdz(request):
    paid_students_thirdz=Register.objects.filter(fee_recieved=0,std='Third')
    d={'paid_students_thirdz':paid_students_thirdz}
    return render(request,'paid_fees_thirdz.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_forth(request):
    paid_students_forth=Register.objects.filter(fees=True,std='Forth')
    d={'paid_students_forth':paid_students_forth}
    return render(request,'paid_fees_forth.html',d)

@login_required(login_url = "/register/login/")
def paid_fees_forth_partial(request):
    paid_students_forth_partial=Register.objects.filter(partial_fee=True,std='Forth')
    d={'paid_students_forth_partial':paid_students_forth_partial}
    return render(request,'paid_fees_forth_partial.html',d)


@login_required(login_url = "/register/login/")
def paid_fees_forthz(request):
    paid_students_forthz=Register.objects.filter(fee_recieved=0,std='Forth')
    d={'paid_students_forthz':paid_students_forthz}
    return render(request,'paid_fees_forthz.html',d)

"""
def paid_fees(request):
    paid_students=Register.objects.filter(fees=True)
    d={'paid_students':paid_students}
    return render(request,'paid_fees.html',d)

def paid_fees(request):
    paid_students=Register.objects.filter(fees=True)
    d={'paid_students':paid_students}
    return render(request,'paid_fees.html',d)
"""