from django.db import models

class projects(models.Model):
  link = models.CharField(max_length=255)
  image_property = models.FileField(upload_to='img',max_length=255,null=True,blank=True,default=None)
  # catagory = models.CharField(max_length=255,null=True,blank=True)
  organization=models.CharField(max_length=255,null=True,blank=True)
  description = models.CharField(max_length=255,null=True,blank=True)
  name=models.CharField(max_length=255,null=True,blank=True)
  language_requirement=models.CharField(max_length=255,null=True,blank=True)
  last_date=models.DateField(max_length=255,null=True,blank=True)



class new(models.Model):
 
  name = models.CharField(max_length=255,null=True,blank=True)
  name_of_organization = models.CharField(max_length=255,null=True,blank=True)

  number_opportunity=models.IntegerField(null=True,blank=True)
  Gender = models.CharField(max_length=255,null=True,blank=True)
  

  Degree=models.CharField(max_length=255,null=True,blank=True)
  opportunity_type=models.CharField(max_length=255,null=True,blank=True)

  scholarship_type=models.CharField(max_length=255,null=True,blank=True)
  province_state=models.CharField(max_length=255,null=True,blank=True)

  language_requirement=models.CharField(max_length=255,null=True,blank=True)
  field_study=models.CharField(max_length=255,null=True,blank=True)

  Duration=models.CharField(max_length=255,null=True,blank=True)
  Language_Instruction=models.CharField(max_length=255,null=True,blank=True)
  last_date=models.DateField(max_length=255,null=True,blank=True)
  link = models.CharField(max_length=255)

  
  description = models.CharField(max_length=255,null=True,blank=True)
  eligibility_criteria = models.CharField(max_length=255,null=True,blank=True)
  requirement_documents = models.CharField(max_length=255,null=True,blank=True)

  
  
  
  
  
  
  
  
 
  





# class projects_2(models.Model):
 
#   name=models.CharField(max_length=255,null=True,blank=True)
#   icon_name=models.CharField(max_length=100, blank=True)
  
#   organization=models.CharField(max_length=255,null=True,blank=True)
#   icon_organization=models.CharField(max_length=100, blank=True)

#   language_requirement=models.CharField(max_length=255,null=True,blank=True)
#   icon_language=models.CharField(max_length=100, blank=True)

#   Gender = models.CharField(max_length=255,null=True,blank=True)
#   icon_gender=models.CharField(max_length=100, blank=True)

#   requirement_documents = models.CharField(max_length=255,null=True,blank=True)
#   icon_documents=models.CharField(max_length=100, blank=True)

#   last_date=models.DateField(max_length=255,null=True,blank=True)
#   icon_lastDate=models.CharField(max_length=100, blank=True)

#   number_opportunity=models.IntegerField(null=True,blank=True)
#   icon_id=models.CharField(max_length=100, blank=True)

#   link = models.CharField(max_length=255)
#   description = models.CharField(max_length=255,null=True,blank=True)
#   eligibility_criteria = models.CharField(max_length=255,null=True,blank=True)

# alliswell
# Email address: sonira.shokoyan531@gmail.com
# password alliswell

  def __str__(self):
    return f"{self.name}"
  