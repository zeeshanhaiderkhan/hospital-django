from django.shortcuts import render, HttpResponse,request
from hospital.models import Patient ,Doctor,Report
from django.db.models.signals import post_save,pre_save

def save_report(sender,instance,**kwargs):
    sample_instance = Patient.objects.get(id=1)
    dr_id= sample_instance.assignedDoctorId
    patient=models.Patient.objects.get(user_id=request.user.id)
    doctor=models.Doctor.objects.get(id=dr_id)
    notifications=print("New report has been submitted")
    mydict={
    'doctor':doctor,
    'patient':patient,
    'notifications':notifications
    }
    return render(request,'temp/doctor_Notifications.html',context=mydict)

post_save.connect(save_report,sender=Report)