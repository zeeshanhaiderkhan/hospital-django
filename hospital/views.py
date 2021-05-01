from django.shortcuts import render, HttpResponse, redirect,reverse
from . import forms,models
from hospital.models import Patient 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User , auth
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required 
from .forms import CreatUserForm,PatientUserForm
from hospital.models import Report
from django.contrib.auth.models import Group
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
#Create your views here.
from .forms import CreatUserForm
def index(request):
    return render(request, 'temp/home.html')


def adminbase(request):
    return render(request, 'temp/admin_base.html')

def admin_dashboard(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    reports=models.Report.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()
    
    reportcount=models.Report.objects.all().filter(status=True).count
    pendingreportcount=models.Report.objects.all().filter(status=False).count()

    mydict={
    'doctors':doctors,
    'patients':patients,
    'reports':reports,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'reportcount':reportcount,
    'pendingreportcount':pendingreportcount,
    }
    return render(request,'temp/admin_dashboard.html',context=mydict)


def doctor_signup(request):
    if request.user.is_authenticated:
        return redirect('doctorclick')
    else:
        form =CreatUserForm()
        context = {'form':form}
        if request.method=='POST':
            form = CreatUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                print('User Created')
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='doctor')
                user.groups.add(group)
                

                messages.success(request, 'The account has been created for ' + username)
                return redirect('doctor_login')
            else:
                print(form.errors)
                print('issue')
                return render(request,'temp/doctorsignup.html', context)
        return render(request,'temp/doctorsignup.html',context)
    
     
def doctor_login(request):
    # if request.user.is_authenticated:
    #     return redirect('doctorbase')
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    else:
        if request.method =='POST':
            username =  request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(request , username = username, password=password)
            if user is not None:
                login(request,user)
                # return redirect('doctorbase')
                return HttpResponseRedirect('afterlogin')
        else:
            messages.info(request,'Username or password is incorrect')

        context= {}
        return render(request, 'temp/doctorlogin.html',context)


def patient_signup(request):
    if request.user.is_authenticated:
        return redirect('doctorclick')
    else:
        form = CreatUserForm()
        context={'form':form}
        if request.method=='POST':
            form = CreatUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                print('User Created')
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='patient')
                user.groups.add(group)
                messages.success(request, 'The account has been created for ' + username)
                return redirect('doctor_login')
            else:
                print(form.errors)
                print('issue')
                return render(request,'temp/patientsignup.html', context)
    return render(request, 'temp/patientsignup.html',context)

def patient_login(request):
    # if request.user.is_authenticated:
    #     return redirect('patientbase')
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    else:
        if request.method =='POST':
            username =  request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username = username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('afterlogin')
                
                # return redirect('patientbase')
        else:
            messages.info(request,'Username or password is incorrect')

        context= {}
        return render(request, 'temp/patientlogin.html')


@login_required(login_url='patient_login') 
def patient(request):
    return render(request, 'temp/patient_profile.html')

    

def patientclick(request):
    return render(request, 'temp/patientclick.html')

@login_required(login_url='patient_login')
def patientbase(request):
    return render(request, 'temp/patientbase.html')



def doctorclick(request):
    return render(request, 'temp/doctorclick.html')



@login_required(login_url='doctor_login') 
def doctorbase(request):
    return render(request, 'temp/doctorbase.html')


@login_required(login_url='doctor_login') 
def doctordashboard(request):
    #for three cards
    doctor=models.Doctor.objects.get(user_id=request.user.id)
    patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=doctor.pk).count()
    mydict={
    'patientcount':patientcount,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request, 'temp/doctor_main.html',context=mydict)



def doctor_patient(request):
    mydict={
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'temp/doctor_patient.html',context=mydict)

import json
def doctor_view_patient(request):
    sample_instance = Patient.objects.get(id=3)
    dr_id= sample_instance.assignedDoctorId
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    patients=models.Patient.objects.all().filter(status=True,assignedDoctorId=doctor.pk)
    report = Report.objects.all().filter(doctorId=doctor)
   
    return render(request,'temp/doctor_view_patient.html',{'doctor':doctor, 'patients':patients})


def doctor_view_reports(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id)
    report = Report.objects.all().filter(doctorId=doctor)
    return render(request,'temp/doctor_view_reports.html',{'doctor':doctor, 'report':report})

def doctor_view_patient_report(request):
    doctor = request.user.id
    patient = request.GET['id']
    
    report = Report.objects.all().filter(doctorId__user_id=doctor).filter(patientId__id=patient)
    
    return render(request,'temp/doctor_view_patient_report.html',{'doctor':doctor, 'report':report})


def doctor_notifications(request):
    return render(request,'temp/doctor_Notifications.html')


def LogOut(request):
    logout(request)
    return redirect('/')


#-----------for checking user is doctor , patient or admin(by sumit)
def is_admin(user):
    return user.groups.filter(name='admin').exists()
def is_doctor(user):
    return user.groups.filter(name='doctor').exists()
def is_patient(user):
    return user.groups.filter(name='patient').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('/doctorbase')
        else:
            return HttpResponse('Waiting for approvel')
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('/patientbase')
        else:
             return HttpResponse('Waiting for approvel')



    ##patient

def patient_dashboard(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    return render(request,'temp/patientdashboard.html',{'patient':patient})


def patient_report(request):
    reports=models.Report.objects.filter(patientId__user__id=request.user.id).count()
    
    return render(request,'temp/patient_report.html',{'reports':reports})


def patient_view_reports(request):
    reports=Report.objects.filter(patientId__user__id=request.user.id)
   
    all_report = {'reports':reports}
    return render(request,'temp/patient_view_reports.html',all_report)

def patient_upload_report(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    doctor=models.Doctor.objects.get(id=patient.assignedDoctorId)
  
    if request.method == "POST":
        patientId=patient
        doctorId=doctor
        Name = request.POST.get('testname', '')
        Date= request.POST.get('testdate', '')
        desc = request.POST.get('desc', '')
        try:

            report_file = request.FILES['report']
        except:
            report_file = None
            
        report = Report(patientId=patientId, doctorId=doctorId, testName=Name, testDate=Date, description=desc, report_file=report_file)
        report.save()
        messages.success(request,'Report has been uploaded')
    return render(request,'temp/patient_upload_report.html')