from django.shortcuts import render,redirect
from CrudMysqlys.forms import StudentForm
from CrudMysqlys import Student

def emp(request):
	if request.method == "POST":
		form = StudentForm (request.POST) # here "form" is one varible
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = StudentForm()
	return render(request,"index.html",{'form':form})

def show(request):
	students= Student.objects.all() # it's select query,select all data store in employees varible
	return render(request,"show.html",{'students': students})

def edit(request,id):
	student = Student.objects.get(id=id)
	return render(request,"edit.html",{'student':student})

def update(request,id):
	student = Student.objects.get(id=id)
	form = StudentForm(request.POST, instance=student)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,"edit.html",{'student':student})

def delete(request,id):
	student = Student.objects.get(id=id)
	student.delete()
	return redirect("/show")

def home(request):
	return render(request,"home.html")
