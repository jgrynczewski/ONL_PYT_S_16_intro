from django.db import models

# Create your models here.

# Student, a w nim następujące właściwości:
#
# name: string, max. 64 znaki, imię powinno być unikalne
# year_at_university: integer,
# is_active: boolean, standardowa wartość True,
class Student(models.Model):
    name = models.CharField(max_length=64, unique=True)
    year_at_university = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

# Lecture, a w nim następujące właściwości:
#
# name: string, max 64 znaki, imię powinno być unikalne,
# lecturer: string, max. 64 znaki.
class Lecture(models.Model):
    name = models.CharField(max_length=64, unique=True)
    lecturer = models.CharField(max_length=64)
    students = models.ManyToManyField('Student')

# Połącz oba modele taką relacją, aby każdy student mógł brać udział w wielu wykładach, a w każdym wykładzie mogło
# brać udział wielu studentów. Relacja musi być założona bez dodatkowych danych (nie używaj argumentu through)
# oraz ma być zaczepiona w modelu Lecture. Pole powinno mieć nazwę students. Pamiętaj o wykonaniu migracji!

# Co pisaliśmy w shellu:

# Stworzenie dwóch studentów
# In [1]: from exam_app.models import Student
# In [2]: s1 = Student.objects.create(name="John", year_at_university=2)
# In [3]: s2 = Student.objects.create(name="Jane", year_at_university=3)
#
# Stworzenie jednego wykładu
# In [4]: from exam_app.models import Lecture
# In [5]: l1 = Lecture.objects.create(name='math', lecturer='Bill')
#
# List studentów wykładu 1 jest pusta
# In [11]: l1.students.all()
# Out[11]: <QuerySet []>
#
# Dodajemy studentów
# In [13]: l1.students.add(s1)
# In [15]: l1.students.add(s2)
#
# Lista studentów wykładu 1 nie jest pusta
# In [18]: l1.students.all()
# Out[16]: <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>
#
# Przykład przefiltrowania studentów wykładu 1
# In [27]: l1.students.filter(year_at_university=2)
# Out[27]: <QuerySet [<Student: Student object (1)>]>
