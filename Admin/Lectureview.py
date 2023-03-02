from django.http import HttpResponse
from django.shortcuts import redirect, render
from Admin.Leacturemodels import Lecture
from Admin.Lectureforms import LectureForm
from Admin.models import Course
        

def Lectureboard(request):
    form = LectureForm()
    Lecture1 = Lecture.objects.all()
    # print(form)
    context = {
        'form': form,
        'Lecture':Lecture1,
    }
    
    return render(request , 'Admin/Lectureboard.html' , context )    
def Lectures(request ):
    if request.method == 'POST':  
        form = LectureForm(request.POST)
        
        if form.is_valid():
            # print('i am ')
            
            # print('i am runing')
            lecture_num =  form.cleaned_data['lecture_num']
        
            if Lecture.objects.filter(lecture_num=lecture_num ).exists():
                user = request.user
                if user.is_superuser:
                    return redirect('Admin:Lectureboard')
                else:
                    return redirect('Teacher:TLectureboard')    
            else:    
                form.save()
                user = request.user
                if user.is_superuser:
                    return redirect('Admin:Lectureboard')
                else:
                    return redirect('Teacher:TLectureboard')
    
    # return render(request , 'Admin/Addlecture.html')    

def Addlecture(request):
    pass


def Lecture_edit(request , id ):
    user = request.user
    
    item = Lecture.objects.get(id = id)
    if request.method == 'POST':
        form = LectureForm(request.POST , instance=item)
        if form.is_valid():
            form.save()
        
            if user.is_superuser:
                return redirect('Admin:Lectureboard')
            else:
                return redirect('Teacher:TLectureboard')    
            
    else:
        form = LectureForm(instance=item)      



        context = {
            'form' : form
        }

        return render(request , 'Admin/Lecture_edit.html' , context  )        


def Leature_delete(request , id ):
    item = Lecture.objects.get(id = id)
    item.delete()
    user = request.user
    if user.is_superuser:
        return redirect('Admin:Lectureboard')
    else:
        return redirect('Teacher:TLectureboard')
         