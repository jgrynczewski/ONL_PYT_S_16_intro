from django.shortcuts import render, HttpResponse, get_object_or_404

from exam_app.models import Lecture


def lecture_details(request, lecture_id):
    # # filter
    # lecture = Lecture.objects.filter(id=lecture_id)
    # if not lecture:
    #     return HttpResponse("Wykład o podanym id nie istnieje", status=404)
    # l1 = lecture[0]  # lub lecture.first()

    # # get
    # try:
    #     l1 = Lecture.objects.get(id=lecture_id)
    # except:
    #     return HttpResponse("Wykład o podanym id nie istnieje", status=404)

    # funkcja get_object_or_404
    l1 = get_object_or_404(Lecture, id=lecture_id)

    students = l1.students.all()
    response = "<ul>"
    for student in students:
        response += f"<li>{student.name}</li>"
    response += "</ul>"

    return HttpResponse(response)
