from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import projects, new
# from .models import YourModel
from django.conf import settings
from django.http import FileResponse
import os
### for email ###
import smtplib
from email.message import EmailMessage


def home(request):
  if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message1 = request.POST.get('message')
        email = request.POST.get('email')
        message=f"""
Dear scholar Team,

I hope this email finds you well. Kindly find the details of the submission below:

Message: {message1}
Name: {name}
Phone: {phone}
Email:{email}"""
        # recipient = 'sonira.shokoyan123@gmail.com'
        recipient = 'rahmatullah.kanjo123@gmail.com'

        # Create the email message
        email = EmailMessage()
        email['Subject'] = name
        email['From'] = settings.EMAIL_HOST_USER
        email['To'] = recipient
        email.set_content(message)

        # Send the email using SMTP
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(email)

        return redirect('/success/')
  project=new.objects.all()
  data2={
     'project':project
  }
  return render(request,'index.html',data2)





def success(request):
    return render(request,'success.html')






def scholarship(request):
  mymembers = projects.objects.all().values()
  template = loader.get_template('scholarship.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

##### for simple template rendering ####
# def scholarship(request):
#     projects=projects.objects.all()
#     data={
#       'projects':projects
#     }
    
#     return render(request,'scholarship.html', data)




##### recieve from models.py send to template.html ####
# def scholarsip(request):
#     projects=projects.objects.all()
#     data={
#       'projects':projects
#     }
#     return render(request,"scholarship.html",data)
# ##### for email feature ####
# def Yourdef(request):
#     if request.method == 'POST':
#         # Get the form data
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         email = request.POST.get('email')
#         message_email=f' Name:{name},\n Email: {email},\n Message:{message}'
#         recipient = ' type the email reciever account gmail'

#         # Create the email message
#         email = EmailMessage()
#         email['Subject'] = name
#         email['From'] = settings.EMAIL_HOST_USER
#         email['To'] = recipient
#         email.set_content(message_email)

#         # Send the email using SMTP
#         with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
#             smtp.starttls()
#             smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#             smtp.send_message(email)

#         return render(request, 'success.html')
    
#     return render(request,'index.html')




# ####### for downloading feature #####
# def download_file(request):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')
#     return FileResponse(open(file_path, 'rb'), as_attachment=True)