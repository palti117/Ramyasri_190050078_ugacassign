from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings

from .models import *
import json

#sorting functions
def Name(l):#sort by name irrespective of upper or lower case 
	return str(l["name"]).upper()

def Department(l):#sort by department irrespective of upper or lower case 
	return str(l["dept"]).upper()

def RollNo(l):#sort by rollnumber 
	return int(l["roll"])

def hostel(l):#sort by hostel
	return int(l["hstl"])
#end of sorting functions



def home(request):#home page where table of students can be seen

	#to feed data from json file to db for once
	f=open("static/users.json")
	usrs = json.load(f)#loads json into dict
	students = student.objects.all() # get all students from db
	if(len(usrs)!=0):
		for s in usrs["students"]:
			n = s["Name"]
			r = str(s["RollNo"])
			h = str(s["hostel"])
			d = s["Department"]
			if not student.objects.filter(roll=r).exists():
				#add studnet to db if not already existed
				student(name=n,roll=r,dept=d,hstl=h).save()

		usrs={
		"students":
			[]
		}
		with open("static/users.json",'w') as file2:
			json.dump(usrs,file2,indent=4)
	#end of feeding data using json file for once


	# for selecting sorting type of table data
	if request.method=="POST":
		students = student.objects.all()
		sorttype = request.POST.get("cat")
		stus=[]
		for s in students:
			d1={
			"name":s,
			"roll":s.ro(),
			"dept":s.de(),
			"hstl":s.ho()
			}
			stus.append(d1)
		#sorting acc to sort type
		if sorttype=="Name":
			stus.sort(key=Name)
		elif sorttype=="Department":
			stus.sort(key=Department)
		elif sorttype=="RollNo":
			stus.sort(key=RollNo)
		elif sorttype=="hostel":
			stus.sort(key=hostel)
		#sending context to display on webpage
		context={'users':stus}
		messages.info(request,"Sorted by "+sorttype)
		return render(request,'userdata/userdata.html',context)


	#when page loaded
	students = student.objects.all()
	stus=[]
	for s in students:
		d1={
		"name":s,
		"roll":s.ro(),
		"dept":s.de(),
		"hstl":s.ho()
		}
		stus.append(d1)
	#sort by Rollno by default	
	stus.sort(key=RollNo)
	context={'users':stus}
	messages.info(request,"Sorted by RollNo")
	return render(request,'userdata/userdata.html',context)


#add student to db, if not already there
def addstu(request):
	if request.method=="POST":

		#get student details
		name=request.POST.get("name")
		roll = request.POST.get("RollNo")
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")

		#db students
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]
		
		#flag for knowing if being added student is already in db, if true, then already in db
		flag = False
		for i in roll_nos:
			if i==roll:
				flag = True

		if flag==False:			
			#adding student to db
			student(name=name,roll=roll,dept=dept,hstl=host).save()
			messages.info(request,"Added "+name+" successfully")
			return render(request,'userdata/addstu.html')
		else:
			#already in db
			messages.info(request,"User with roll no. "+roll+" already in database")
			return render(request,'userdata/addstu.html')

	return render(request,'userdata/addstu.html')

#remove student to db, if there
def remstu(request):

	if request.method=="POST":
		#get student roll no.
		roll = request.POST.get("RollNo")

		#get all students from db
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]
		
		#flag for knowing if student is in db, if true, then present
		flag = False
		for i in roll_nos:
			if i==roll:
				flag = True
				student.objects.filter(roll=roll).delete()
				break

		if flag:		
			#student there in db, and will be removed
			messages.info(request,"Removed "+roll+" successfully")
			return render(request,'userdata/remstu.html')
		else:
			#student not in db
			messages.info(request,"No such user of Roll no.  "+roll+" in database")
			return render(request,'userdata/remstu.html')
			
	return render(request,'userdata/remstu.html')


#edit student details in db, if there
def editstu(request):	
	if request.method=="POST":
		#get rollnumber
		roll = request.POST.get("RollNo")
		#about to edit details
		name=request.POST.get("name")		
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")

		#students in db
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]

		data1 = {
			"name":name,
			"roll":int(roll),
			"dept":dept,
			"hstl":int(host)
		}

		#setting flag for knowing if student is in db, if true, then present in db
		flag = False
		for i in roll_nos:
			if i==roll:
				student.objects.filter(roll=roll).update(name=name,hstl=host,dept=dept)
				flag = True
				break

		if flag:
			#student in db, details will be edited
			messages.info(request,"Edited details of  "+roll+" successfully")
			return render(request,'userdata/editstu.html')
		else:
			#not in db
			messages.info(request,"No such student with Roll No.: "+roll)
			return render(request,'userdata/editstu.html')
			
	
	return render(request,'userdata/editstu.html')


###END OF views.py###
