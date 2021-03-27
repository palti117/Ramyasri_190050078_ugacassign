from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import *
import json

#to feed data into database
'''f=open("static/users.json")
usrs = json.load(f)
usrs_stu = usrs["students"]'''

def Name(l):
	return l["name"]

def Department(l):
	return l["dept"]

def RollNo(l):
	return int(l["roll"])

def hostel(l):
	return int(l["hstl"])

def home(request):
	if request.method=="POST":
		doc = request.FILES
		print(doc)
		'''myfile=doc['myfile']
		f=open(myfile)
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		print(fs.url(filename))
		usrs = json.load(f)
		print(usrs)'''
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

		stus.sort(key=RollNo)
		context={'users':stus}
		messages.info(request,"Sorted by RollNo")
		return render(request,'userdata/userdata.html',context)

	'''if request.method=="POST":
		sorttype = request.POST.get("cat")
		print(sorttype)
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
		if sorttype=="Name":
			stus.sort(key=Name)
		elif sorttype=="Department":
			stus.sort(key=Department)
		elif sorttype=="RollNo":
			stus.sort(key=RollNo)
		elif sorttype=="hostel":
			stus.sort(key=hostel)
		messages.info(request,"Sorted by "+sorttype)
		context={'users':students}
		return render(request,'userdata/userdata.html',context)
'''
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

	stus.sort(key=RollNo)
	context={'users':stus}
	messages.info(request,"Sorted by RollNo")
	return render(request,'userdata/userdata.html',context)

def addstu(request):
	if request.method=="POST":
		name=request.POST.get("name")
		roll = request.POST.get("RollNo")
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]
		
		flag = False
		for i in roll_nos:
			if i==roll:
				flag = True

		if flag==False:			
			student(name=name,roll=roll,dept=dept,hstl=host).save()
			messages.info(request,"Added "+name+" successfully")
			return render(request,'userdata/addstu.html')
		else:
			messages.info(request,"User with roll no. "+roll+" already in database")
			return render(request,'userdata/addstu.html')

	return render(request,'userdata/addstu.html')

def remstu(request):
	if request.method=="POST":
		roll = request.POST.get("RollNo")
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]
		
		flag = False
		for i in roll_nos:
			if i==roll:
				flag = True
				student.objects.filter(roll=roll).delete()
				break

		if flag:		
			messages.info(request,"Removed "+roll+" successfully")
			return render(request,'userdata/remstu.html')
		else:
			messages.info(request,"No such user of Roll no.  "+roll+" in database")
			return render(request,'userdata/remstu.html')
			
	return render(request,'userdata/remstu.html')


def editstu(request):	
	if request.method=="POST":
		roll = request.POST.get("RollNo")
		#about to edit details
		name=request.POST.get("name")		
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")
		students = student.objects.all()
		roll_nos = [stu.roll for stu in students]
		data1 = {
			"name":name,
			"roll":int(roll),
			"dept":dept,
			"hstl":int(host)
		}
		flag = False
		for i in roll_nos:
			if i==roll:
				student.objects.filter(roll=roll).update(name=name,hstl=host,dept=dept)
				flag = True
				break

		if flag:
			messages.info(request,"Edited details of  "+roll+" successfully")
			return render(request,'userdata/editstu.html')
		else:
			messages.info(request,"No such student with Roll No.: "+roll)
			return render(request,'userdata/editstu.html')
			
	
	return render(request,'userdata/editstu.html')
