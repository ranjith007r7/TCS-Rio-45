from django.shortcuts import render
from app26.models import Student
from app26.form import StudentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from app26.forms import SignUpForm

def home(request):
	student=Student.objects.all()
	return render(request,"apps/25.html",{'s':student})

def forms(request):
	form = StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)

	
	return render(request,"apps/form.html",{'form':form})

def final(request):
	return render(request,'apps/final.html')
def delete(request,id):
	s=Student.objects.get(id=id)
	s.delete()
	return redirect('/index')
def update(request,id):
	student=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect('/index')
	return render(request,'apps/update.html',{'s':student})
def index(request):
	return render(request,'apps/index.html')
@login_required
def open(request):
	return render(request,'apps/open.html')
@login_required
def service(request):
	return render(request,'apps/service.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def contact(request):
	return render(request,'apps/contact.html')
def logout(request):
	return render(request,'registration/logout.html')
def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'registration/signup.html',{'form':form})
	

