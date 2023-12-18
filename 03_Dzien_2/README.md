## Zadanie 1 – rozwiązywane z wykładowcą

Zajrzyj do katalogu `project`. Znajdziesz tam projekt o nazwie **coderslab**.
* Sprawdź plik **settings.py**, czy wszystko jest skonfigurowane poprawnie.
* Utwórz wirtualne środowisko.
* Zainstaluj potrzebne biblioteki. (Możesz skorzystać z pliku **requirements.txt**: `pip install -r requirements.txt`)
* Załóż bazę danych o odpowiedniej nazwie.
* Wykonaj migrację i uruchom projekt.


## Zadanie 2 – rozwiązywane z wykładowcą

Zajrzyj do aplikacji **exercises_app** w projekcie **coderslab**. Znajdziesz tam model `Band`, który zawiera informację 
o zespołach rockowych. Znajdziesz tam zdefiniowane dwa pola: `name` – nazwę zespołu i `year` – rok założenia zespołu.

Dodaj tam pola:
* `still_active`: czy zespół jest jeszcze aktywny. Pole powinno przyjmować typ boolean, domyślna wartość `True`.
* `genre`: pole typu integer, które powinno przyjmować wartości:
  * -1: not defined,
  * 0: rock,
  * 1: metal,
  * 2: pop,
  * 3: hip-hop,
  * 4: electronic,
  * 5: reggae,
  * 6: other.

Pole powinno domyślnie przyjąć wartość -1.

Hint: Skorzystaj z parametru **choices**. Więcej znajdziesz w sekcji **Snippets**.

Pamiętaj, aby wszystkie modele definiować w pliku **models.py**!


## Zadanie 3

Utwórz model `Category`, który będzie przechowywał listę wszystkich kategorii w CMS-ie. Model powinien mieć pola:
* `name`: string, max 64 znaki,
* `description`: nielimitowanej długości string. Może przyjmować wartość `null`.


>CMS (Content Management System) - system zarządzania treścią.
>https://pl.wikipedia.org/wiki/System_zarz%C4%85dzania_tre%C5%9Bci%C4%85


## Zadanie 4

a. Utwórz model `Article`, który będzie przechowywał dane nt. artykułów w CMS-ie. Model powinien mieć następujące pola:

* `title`: string, max. 128 znaków,
* `author`: string, max. 64 znaki, może przyjmować wartość `null`,
* `content`: nielimitowanej długości string,
* `date_added`: pole typu datetime, wartość ma być automatyczniee dodawana podczas pierwszego zapisu 
(podpowiedź: `auto_now_add=True`).

b. Model `Article` potrzebuje jeszcze kilku pól:

* statusu, który będzie przyjmował następujące wartości:
    * w trakcie pisania,
    * czeka na akceptację redaktora,
    * opublikowany
    (podpowiedź: atrybut **choices**),
* daty początku emisji (pole może przyjmować wartość null),
* daty końca emisji (pole może przyjmować wartość null).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.


## Zadanie 5

Utwórz model `Album`, który będzie przechowywał następujące wartości:
* tytuł albumu,
* rok wydania,
* ocenę (w skali 0-5 gwiazdek) (podpowiedź: **choices**).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.


## Zadanie 1 &ndash; wykonywane razem z wykładowcą

W aplikacji **exercises_app**, w modelu `Band` znajduje się kilkanaście zespołów. 

* Wyciągnij dane wszystkich zespołów.
* Posortuj je alfabetycznie.
* Dodaj dane zespołu Rage Against The Machine, rok założenia 1991.

Zadania roziąż w konsoli interaktywnej (`python manage.py shell`)

Hint: Jak doinstalujesz **ipython** (`pip install ipython`) shell będzie kolorował składnię, 
oraz podpowiadał komendy przy użyciu przycisku **tab**

##### Wszystkie zadania wykonuj używając Django ORM.

#### Zadanie 2

* Znajdź wszystkie zespoły, które nie mają zdefinowanego roku założenia. Wypisz w konsoli ich nazwy 
i identyfikator nadany przez bazę danych.
* Znajdź informacje o zespołach, które nie mają w naszej bazie podanego roku założenia. 
Uzupełnij informacje (może być losowo) i zapisz je w bazie danych.

##### Skorzystaj z powłoki interaktywnej **django** (`python manage.py shell`)

Hint: Możesz napisać funkcję, którą następnie zaimportujesz i wywołasz w powłoce django.
Zwykły skrypt nie zadziała, ponieważ nie będzie miał skonfigurowanej bazy danych oraz aplikacji django.

**Dla chętnych**: Możesz napisać własną komendę, która będzie uruchamiana z poziomu **manage.py**

[https://docs.djangoproject.com/en/dev/howto/custom-management-commands/](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)


## Zadanie 3

* Uzupełnij gatunki zespołów oraz informację, czy są nadal aktywne. 

##### Skorzystaj z powłoki interaktywnej **django** (`python manage.py shell`)

Hint: Możesz napisać funkcję, którą następnie zaimportujesz i wywołasz w powłoce django.
Zwykły skrypt nie zadziała, ponieważ nie będzie miał skonfigurowanej bazy danych oraz aplikacji django.

**Dla chętnych**: Możesz napisać własną komendę, która będzie uruchamiana z poziomu **manage.py**

[https://docs.djangoproject.com/en/dev/howto/custom-management-commands/](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)


## Zadanie 4

Znajdź i wypisz na konsoli wszystkie zespoły, które:

* Mają w nazwie "The",
* założone zostały w latach 1980-tych i są wciąż aktywne,
* założone zostały w latach 1970-tych oraz mają w nazwie "The",
* założone zostały w latach 1980-tych, oraz są już nieaktywne. 


## Zadanie 5.

* Do modelu `Category` z poprzedniej części, dodaj kilka wybranych kategorii,
* Dodaj kilka artykułów do modelu `Article`.

Nie dodawaj tytułu ani zawartości losowo, skorzystaj z [Random text generator](http://randomtextgenerator.com/).


## Zadanie 6

Napisz widok, który udostępnisz pod adresem `/articles`, w którym pokażesz listę artykułów. 
Na liście powinien pojawić się tytuł, autor (jeśli jest) i data dodania artykułu do bazy. 
Wybierz tylko artykuły ze statusem "opublikowany".

W tym celu w widoku wyciągnij wszystkie opublikowane artykuły z bazy danych, i przekaż je przy użyciu metody `format`, 
do stringa z kodem **html**, który wyświetli odpowiednio dane.

**Dla chętnych**:
Zamiast pisać kod **html** w zmiennej w widoku, możesz użyć zewnętrznego pliku **html** (tak zwanego szablonu). 
Więcej na ten temat znajdziesz w jednej z prezentacji z tego modułu, lub w oficjalnej dokumentacji:
[https://docs.djangoproject.com/en/4.0/ref/templates/](https://docs.djangoproject.com/en/4.0/ref/templates/)

## Zadanie 1 &ndash; wykonywane razem z wykładowcą
* W jednym z poprzednich zadań, utworzyliśmy model `Album`. Teraz dodaj odpowiednią relację z modelem `Band`, 
tak by jeden zespół mógł mieć wiele albumów.

* Dodaj kilka albumów do kilku zespołów (nie szukaj ich w internecie, możesz coś wymyślić). 

* Wypisz w konsoli wszystkie albumy dowolnego zespołu.

##### Wszystkie zadania wykonuj używając Django ORM.


## Zadanie 2

Dodaj do modeli kolejny: `Song`. Powinien mieć następujące pola:
* `title`: string, max długość 128 znaków,
* `duration`: czas (TimeField), może przyjmować null,
* dodaj relację wiele-do-jednego tak, aby jeden album mógł mieć wiele piosenek.

Uzupełnij dane, tworząc albumy grup i uzupełniając je piosenkami (nie przejmuj się, czy piosenki są prawdziwe, 
po prostu je dodaj).


## Zadanie 3

Wyciągnij z bazy danych (i wypisz na konsoli), używając modeli:

* wszystkie albumy dowolnego zespołu,
* wszystkie piosenki z każdego albumu.


## Zadanie 4

* Połącz modele `Article` i `Category` tak, aby jeden artykuł mógł mieć wiele kategorii, a każda kategoria mogła być
przypisana do wielu artykułów.
* Dodaj kilka kategorii do każdego artykułu.

Podpowiedź: Relaję wiele do wielu możesz zaczepić w dowolnym modelu:
* Możesz dodać pole categories w modelu Article
* Możesz dodać pole articles w modelu Category


## Zadanie 5

* Wybierz kategorię. Następnie wybierz (i wypisz na konsoli) wszystkie artykuły należące do tej kategorii.
* Wybierz dwie kategorie. Następnie wybierz i wypisz na konsoli wszystkie artykuły należące 
*jednocześnie* do obu kategorii.


## Zadanie 6
* Napisz model `Person`, który będzie miał następującą właściwość:
    * `name`,
* Napisz model `Position`, który będzie miał następujące właściwości:
    * `position_name`,
    * `salary`,
* Połącz oba modele relacją tak, aby jedna osoba mogła być przypisana dokładnie do jednego stanowiska, 
a każde stanowisko miało tylko jednego pracownika. Zadbaj o to, by wraz z usunięciem stanowiska, 
usuwana była też przyporządkowana do niego osoba.
Hint:
Masz dwa sposoby:
- albo dodajesz pole `person` w modelu `Position`
- albo dodajesz pole `position` w modelu `Person`

* Dodaj kilka osób i stanowisk.


## Zadanie 7

Napisz widok i udostępnij go pod adresem `/show-band/{id}/`, gdzie **id** to identyfikator zespołu. 
Widok powinien wyświetlić informacje o zespole muzycznym: jego nazwę, 
gatunek i rok założenia oraz informację, czy wciąż jest aktywny. 

W tym celu w widoku musisz pobrać parametrem z URL-a id zespołu, wyciągnąć przy użyciu modelu dane zespołu 
i przekazać je  za pomocą instrukcji `format` do stringa z kodem HTML. 

Zwróć uwagę, że jeśli w zadaniu 1 dodałeś klucz obcy Band - Album, to w modelu `Band` masz pole, które przechowuje 
listę albumów danego zespołu. Pokaż albumy w szablonie. 

**Hint:** użyj następującego wyrażenia regularnego, do zdefiniowania URL-a: 
```
^/show-band/(?P<id>\d+)/$
```

Możesz też użyć instrukcji **path** podając ścieżkę w prostszy sposób:
```
/show-band/<int:id>/
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz 
w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.


## Zadanie 8 (*)
1. Zapoznaj się z aplikacją **football** i sprawdź, czy jest zarejestrowana w projekcie.
2. Zapoznaj się ze strukturą bazy danych, znajdującą się w pliku **models.py**.
3. Wykonaj migrację, aby dodać odpowiednie tabele do bazy danych.
4. W katalogu `management` znajduje się komenda ładująca przykładowe dane do bazy. 
Możesz zapoznać się z zawartością tego katalogu. Uruchom komendę `python manage.py insert_football_data`.
5. Utwórz widok `league_table`, który:
    * wyciągnie z bazy danych ligową tabelę posortowaną wg liczby zdobytych punktów,
    * utworzy HTML, w którym znajdą się następujące dane:
        * pozycja w tabeli,
        * nazwa klubu,
        * liczba punktów,
    * zwróci wynik do przeglądarki.
6. utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `league_table` pod URL-em `/table/`.

**Podpowiedź:**

Aby zobaczyć informacje o dostępnych komendach wpisz:
```
python manage.py help
```
Aby załadować dane uruchom komendę:
```
python manage.py insert_football_data
```
Więcej o własnych komendach django możesz doczytać tutaj:
[https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/)


## Zadanie 9 (*).
1. Wybierz swój ulubiony klub piłkarski z tabeli (np. Naprzód Brwinów).
2. Utwórz widok `games_played`, który:
    * wyciągnie z tabeli wszystkie mecze, które rozegrał klub (zarówno te w domu, jak i na wyjeździe),
    * utworzy HTML, w którym znajdą się następujące dane:
        * nazwa klubu gospodarza,
        * nazwa klubu gościa,
        * wynik (np. 2:0),
    * zwróci wynik do przeglądarki.
3. Utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `games_played` pod URL-em `/games/`.

### Podpowiedzi do zadań 8 i 9

* Do operacji na bazach danych użyj modeli.

* Możesz zapoznać się z materiałami pod poniższymi linkami. Dowiesz się, jak poradzić sobie z tworzeniem modeli 
do istniejących już baz danych:
    * [https://docs.djangoproject.com/en/4.0/ref/django-admin/#inspectdb](https://docs.djangoproject.com/en/4.0/ref/django-admin/#inspectdb)
    * [https://docs.djangoproject.com/en/3.0/howto/legacy-databases/](https://docs.djangoproject.com/en/3.0/howto/legacy-databases/)

* Aby przećwiczyć import danych powyższym sposobem, możesz wykorzystać plik `football.sql`. 
Efekt powinien być podobny, jak przy uruchomieniu migracji i użyciu komendy `insert_football_data`.
Możesz w tym celu utworzyć nowy projekt django i spróbować zaimportować bazę z istniejącego pliku. 
