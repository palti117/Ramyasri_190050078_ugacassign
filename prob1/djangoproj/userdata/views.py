from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import json

def Name(l):
	return l["Name"]

def Department(l):
	return l["Department"]

def RollNo(l):
	return l["RollNo"]

def hostel(l):
	return l["hostel"]

def home(request):
	if request.method=="POST":
		sorttype = request.POST.get("cat")
		print(sorttype)
		file=open("static/users.json")
		data = json.load(file)
		students = data["students"]
		if sorttype=="Name":
			students.sort(key=Name)
		elif sorttype=="Department":
			students.sort(key=Department)
		elif sorttype=="RollNo":
			students.sort(key=RollNo)
		elif sorttype=="hostel":
			students.sort(key=hostel)
		messages.info(request,"Sorted by "+sorttype)
		context={'users':students}
		return render(request,'userdata/userdata.html',context)
	file=open("static/users.json")
	data = json.load(file)
	students = data["students"]
	students.sort(key=RollNo)
	context={'users':students}
	messages.info(request,"Sorted by RollNo")
	return render(request,'userdata/userdata.html',context)

def addstu(request):
	if request.method=="POST":
		name=request.POST.get("name")
		roll = request.POST.get("RollNo")
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")
		file=open("static/users.json")
		data = json.load(file)
		data1 = {
			"Name":name,
			"RollNo":int(roll),
			"Department":dept,
			"hostel":int(host)
		}
		flag = False
		for i in range(len(data["students"])):
			if data["students"][i]["RollNo"]==int(roll):
				flag = True

		if flag==False:
			data["students"].append(data1)
			with open("static/users.json",'w') as file2:
				json.dump(data,file2,indent=4)
				messages.info(request,"Added "+name+" successfully")
				return render(request,'userdata/addstu.html')
		else:
			messages.info(request,"User with roll no. "+roll+" already added")
			return render(request,'userdata/addstu.html')

	return render(request,'userdata/addstu.html')

def remstu(request):
	if request.method=="POST":
		name=request.POST.get("name")
		roll = request.POST.get("RollNo")
		host = request.POST.get("hostel")
		dept = request.POST.get("Department")
		file=open("static/users.json")
		data = json.load(file)
		
		flag = False
		for i in range(len(data["students"])):
			if data["students"][i]["RollNo"]==int(roll):
				flag = True
				data["students"].remove(data["students"][i])
				break

		if flag:		
			with open("static/users.json",'w') as file2:
				json.dump(data,file2,indent=4)
				messages.info(request,"Removed "+name+" successfully")
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
		file=open("static/users.json")
		data = json.load(file)
		data1 = {
			"Name":name,
			"RollNo":int(roll),
			"Department":dept,
			"hostel":int(host)
		}
		flag = False
		for i in range(len(data["students"])):
			if data["students"][i]["RollNo"]==int(roll):
				data["students"][i]=data1
				flag = True

		if flag:
			with open("static/users.json",'w') as file2:
				json.dump(data,file2,indent=4)
				messages.info(request,"Edited details of  "+roll+" successfully")
				return render(request,'userdata/editstu.html')
		else:
			messages.info(request,"No such student with Roll No.: "+roll)
			return render(request,'userdata/editstu.html')
			
	
	return render(request,'userdata/editstu.html')
