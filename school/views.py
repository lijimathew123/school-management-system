from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student, Login, Note, Assignment, TimeTable, Attendance

import os


# Create your views here.


def index(request):
    return render(request, "index.html")


def gallery(request):
    try:
        return render(request, "gallery.html")
    except:
        return  HttpResponse('Something went wrong!!!')



def teacher_student_reg(request):
    try:
        if request.method == 'POST':
            obj = Student()
            obj.FirstName = request.POST['fname']
            obj.LastName = request.POST['lname']

            a = request.FILES.get('img', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.jpg' or file_extension == '.jpeg':
                obj.Photo = a

            else:
                return HttpResponse(
                    "Upload a valid image. The file you uploaded was either not an image or a corrupted image.")

            obj.Date_of_Birth = request.POST['dob']
            obj.Gender = request.POST['gender']
            obj.Address = request.POST['address']
            obj.State = request.POST['state']
            obj.Country = request.POST['country']
            obj.Email = request.POST['email']
            obj.Guardian_Name = request.POST['gname']
            obj.PhoneNumber1 = request.POST['phone1']
            obj.PhoneNumber2 = request.POST['phone2']
            obj.Class = request.POST['std']
            obj.Academic_Year = request.POST['academicyear']
            obj.Area_of_Interest = request.POST['interest']

            try:
                user_exists = Login.objects.get(UserName=request.POST['username'])
                return HttpResponse("username already taken")

            except Login.DoesNotExist:
                obj.UserName = request.POST['username']

            try:
                user_exists = Login.objects.get(Password=request.POST['password'])
                return HttpResponse("password already taken")

            except Login.DoesNotExist:
                obj.Password = request.POST['password']
            obj.Status = 'pending'

            obj.save()

            ob = Login()
            ob.Type = 'student'
            ob.UserName = request.POST['username']
            ob.Password = request.POST['password']

            ob.save()
        return render(request, "teacher_student_register.html")
    except:
        return HttpResponse('Something went wrong!!! Please check all the data you filled.')


def tregister(request):
    return render(request, "ad_login.html")


def tlogin(request):
    return render(request, "teacher_login.html")


def student_reg(request):
    return render(request, "student_reg.html")


def teacher_reg(request):
    return render(request, "teacher_reg.html")


def student_log(request):
    return render(request, "student_log.html")


def forget_pass(request):
    return render(request, "forgot_password.html")


def forget_pass_edit(request):
    try:
        if request.method == 'POST':
            m = Login.objects.get(UserName=request.POST['username'])
            a = request.POST.get('npassword')
            b = request.POST.get('cpassword')
            if a == b:
                m.Password = request.POST.get('npassword')
                m.save()

                if m.Type == 'teacher':
                    nt = Teacher.objects.get(UserName=request.POST['username'])
                    nt.Password = m.Password
                    nt.save()

                    return render(request, "teacher_login.html")
                else:
                    ns = Student.objects.get(UserName=request.POST['username'])
                    ns.Password = m.Password
                    ns.save()
                    return render(request, "student_log.html")
            else:
                return HttpResponse('not matching')
        else:
            return HttpResponse('Password not matching')
    except:
        return HttpResponse('Something went wrong')


def ad_home(request):
    try:
        if request.method == 'POST':
            obj = Teacher()
            obj.FirstName = request.POST['fname']
            obj.LastName = request.POST['lname']

            a = request.FILES.get('img', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.jpg' or file_extension == '.jpeg':
                obj.Photo = a

            else:
                return HttpResponse(
                    "Upload a valid image. The file you uploaded was either not an image or a corrupted image.")

            obj.Photo = request.FILES['img']
            obj.Date_of_Birth = request.POST['age']
            obj.Gender = request.POST['gender']
            obj.Address = request.POST['address']
            obj.State = request.POST['state']
            obj.Country = request.POST['country']
            obj.Email = request.POST['email']
            obj.PhoneNumber = request.POST['phone']
            obj.Qualification = request.POST['qal']
            obj.Date_of_joining = request.POST['join']
            obj.Subject = request.POST['sub']
            obj.Class_in_charge = request.POST['class1']

            try:
                user_exists = Login.objects.get(UserName=request.POST['username'])
                return HttpResponse("username already taken")

            except Login.DoesNotExist:
                obj.UserName = request.POST['username']

            try:
                user_exists = Login.objects.get(Password=request.POST['password'])
                return HttpResponse("password already taken")

            except Login.DoesNotExist:
                obj.Password = request.POST['password']

            obj.save()

            ob = Login()
            ob.Type = 'teacher'
            ob.UserName = request.POST['username']
            ob.Password = request.POST['password']

            ob.save()

            tcr = Teacher.objects.all()
            return render(request, "ad_home.html", {'tc': tcr})
    except:
        return HttpResponse('Something went wrong!!')


def teacher_home(request):
    try:
        m = Login.objects.get(UserName=request.POST['username'])
        if m.Password == request.POST['password']:
            tr = Teacher.objects.get(UserName=request.POST['username'], Password=request.POST['password'])
            s = Student.objects.all().filter(Class=tr.Class_in_charge)
            request.session['name'] = m.UserName
            return render(request, "teacher_home.html", {'d': tr, 'st': s})
        else:
            return HttpResponse('Invalid username or password')
    except:
        return HttpResponse('Something went wrong!!! Please check your username or password')


def student_home(request):
    try:
        m = Login.objects.get(UserName=request.POST.get('username'))
        if m.Password == request.POST['password']:
            Usn = request.POST['username']
            Pwd = request.POST['password']
            stt = Student.objects.get(UserName=Usn, Password=Pwd)
            if stt.Status == 'accepted':
                request.session['name'] = m.UserName
                return render(request, "student_home.html", {'d': stt})
            else:
                return HttpResponse('You are not accepted')
        else:
            return HttpResponse('Invalid username or password')
    except:
        return HttpResponse('Something went wrong!!! Please check your username or password')


def log(request):
    try:
        m = Login.objects.get(UserName=request.POST['username'])
        if m.Password == request.POST['password']:
            tc = Teacher.objects.all()
            request.session['name'] = m.UserName
            return render(request, "ad_home.html", {'tc': tc})
        else:
            return HttpResponse('Invalid username or password')
    except:
        return HttpResponse('Something went wrong!!! Some Technical issue found!')


def note_upload(request):
    try:
        if request.method == 'POST':
            nt = Note()
            nt.Class = request.POST.get('class9', False)
            nt.Chapter = request.POST.get('chapter', False)
            nt.Subject = request.POST.get('subject9', False)

            a = request.FILES.get('note', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.pdf':
                nt.Note = a

            else:
                return HttpResponse("Upload a valid file. The file you uploaded was either not an pdf.")

            nt.save()
        return HttpResponse('Successfully uploaded')
    except:
        return HttpResponse('Something went wrong!!!')


def attendance_upload(request):
    try:
        if request.method == 'POST':
            at = Attendance()
            at.Class = request.POST.get('class3', False)
            at.Month = request.POST.get('month', False)

            a = request.FILES.get('attendance', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.pdf':
                at.Attendance = a

            else:
                return HttpResponse(
                    "Upload a valid file. The file you uploaded was either not an pdf.")

            at.save()
        return HttpResponse('Successfully uploaded')
    except:
        return HttpResponse('Something went wrong!!!')


def assignment_upload(request):
    try:
        if request.method == 'POST':
            ag = Assignment()
            ag.Class = request.POST.get('class2', False)
            ag.Subject = request.POST.get('subject2', False)

            a = request.FILES.get('assignment', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.pdf':
                ag.Assignment = a

            else:
                return HttpResponse(
                    "Upload a valid file. The file you uploaded was either not an pdf.")

            ag.save()
        return HttpResponse('Successfully uploaded')
    except:
        return HttpResponse('Something went wrong!!!')


def timetable_upload(request):
    try:
        if request.method == 'POST':
            tm = TimeTable()
            tm.Class = request.POST.get('class4', False)

            a = request.FILES.get('timetable', False)
            filename, file_extension = os.path.splitext((str(a)))

            if file_extension == '.pdf':
                tm.TimeTable = a

            else:
                return HttpResponse(
                    "Upload a valid file. The file you uploaded was either not an pdf.")

            tm.save()
        return HttpResponse('Successfully uploaded')
    except:
        return HttpResponse('Something went wrong!!!')


def accept(request, idd):
    try:
        stdnt = Student.objects.get(id=idd)
        stdnt.Status = 'accepted'
        stdnt.save()
        return HttpResponse('Accepted')
    except:
        return HttpResponse('Somthing went wrong!!')


def reject(request, icc):
    try:
        sd = Student.objects.get(id=icc)
        lg = Login.objects.get(UserName=sd.UserName, Password=sd.Password)
        lg.delete()

        sd.delete()
        return HttpResponse("Rejected!!")
    except:
        return HttpResponse('Something went wrong!!!')


def delete(request,id):
    try:
        th = Teacher.objects.get(id=id)
        lg = Login.objects.get(UserName=th.UserName, Password=th.Password)
        lg.delete()
        th.delete()
        thr = Teacher.objects.all()
        return render(request, 'ad_home.html', {'tc': thr})
    except:
        return HttpResponse('Something went wrong!!!')


def logout(request):
    return render(request, 'index.html')


def works(request):
    if request.method == 'POST':
        notes = Note.objects.all().filter(Class=request.POST['class6'], Subject=request.POST['subject6'])
        assignments = Assignment.objects.all().filter(Class=request.POST['class6'], Subject=request.POST['subject6'])
        att = Attendance.objects.all().filter(Class=request.POST['class6'])
        timetable = TimeTable.objects.all().filter(Class=request.POST['class6'])

        return render(request, 'works.html',
                      {'notes': notes, 'assignments': assignments, 'att': att, 'timetable': timetable})


def updation(request):

        if request.method == 'POST':
            sut = Student.objects.filter(UserName=request.POST.get('username',), Password=request.POST.get('password')).update(FirstName = request.POST["fname"],
            LastName = request.POST['lname'],
            Gender = request.POST["gender"],
            Address = request.POST["address"],
            State = request.POST["state"],
            Country = request.POST["country"],
            Email = request.POST["email"],
            Guardian_Name=request.POST["gname"],
            PhoneNumber1 = request.POST["phone1"],
            PhoneNumber2 = request.POST['phone2'],
            Area_of_Interest = request.POST["interest"],
            Academic_Year = request.POST['academicyear'],
            Class = request.POST["std"])
            return HttpResponse('Changed')





def updation1(request):

        if request.method == 'POST':
            tch = Teacher.objects.filter(UserName=request.POST.get('username', False),Password=request.POST.get('password', False)).update(FirstName = request.POST["fname"],
            LastName = request.POST['lname'],
            Gender = request.POST["gender"],
            Address = request.POST["address"],
            State = request.POST["state"],
            Country = request.POST["country"],
            Email = request.POST["email"],
            PhoneNumber = request.POST["phone"],
            Qualification = request.POST["qal"],
            Subject = request.POST['sub'],
            Class_in_charge = request.POST["class1"])
            return HttpResponse('Changed')

