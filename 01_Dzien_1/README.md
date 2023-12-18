## Zadanie 1 &ndash; tworzenie projektu.

Stwórz forka repozytorium. Sklonuj repozytorium na swój komputer. Następnie utwórz folder **projekt_1** 
- folder powinen się znajdować w katalogu **1_Zadania/Dzien_1**.  
Następnie w terminalu wejdź do folderu i wykonaj następujące kroki:

1. utwórz wirtualne środowisko w podkatalogu env (pamiętaj o tym, żeby środowisko utworzyć dla Pythona w wersji 3)
2. uruchom virtualenv,
3. używając narzędzia PIP, zainstaluj bibliotekę Django,
4. używając narzędzia **django-admin**, utwórz projekt
5. uruchom serwer deweloperski i sprawdź, czy działa (http://127.0.0.1:8000/).


## Zadanie 2 &ndash; konfigurowanie projektu.

1. używając narzędzia **manage.py** utwórz nową aplikację **django_1** ,
2. dodaj aplikację **exercises_app** do pliku **settings.py**,
3. Zainstaluj sterownik PostgreSQL:
    * używając narzędzia PIP zainstaluj pakiet `psycopg2-binary`.
4. skonfiguruj Django do pracy z bazą danych PostgreSQL:
    * załóż bazę danych, którą dołączysz do projektu, nazwij ją **exercises**,
    * w pliku **settings.py** znajdź wpis `DATABASES` i zmień go tak aby współpracował z Twoją bazą danych:

```python
DATABASES = {
    'default': {
        'NAME': '<tu wstaw nazwę bazy danych>',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': '<tu wstaw nazwę użytkownika bazy danych>',
        'PASSWORD': '<tu wstaW hasło bazy danych>',
        'HOST': '127.0.0.1'
    }
}
```

5. wykonaj pierwszą migrację.
6. uruchom serwer deweloperski i sprawdź, czy działa.

Czy i jak zmieniła się strona główna projektu?


## Zadanie 3 – pierwsza strona

Wzorując się na przykładzie z prezentacji napisz stronę która pokaże napis `Hello World`. Strona powinna być przypisana do adresu `/hello/`. Pamiętaj o tym żeby metoda która będzie wykonywana zwracała obiekt typu `HttpResponse`.

Hint: możesz użyć poniższego wyrażenia regularnego żeby przypisać funkcję do odpowiedniego adresu:

```
r'^hello/$'
```

Mozesz też użyć metody `path`, wtedy nie będziesz musiał korzystać z wyrażeń regularnych.


## Zadanie 4 – druga strona

Wzorując się na przykładzie z prezentacji napisz stronę która pokaże losową liczbę z zakresu od 0 do 100. 
Strona powinna być przypisana do adresu `/random/`. 
Strona powinna wyświetlać napis `Wylosowano liczbę: <wylosowana liczba>` oczywiście wstawiając wylosowaną liczbę 
w odpowiednie miejsce. Pamiętaj o tym żeby metoda która będzie wykonywana zwracała obiekt typu `HttpResponse`.

Hint: możesz użyć poniższego wyrażenia regularnego żeby przypisać funkcję do odpowiedniego adresu:

```
r'^random/$'
```
Mozesz też użyć metody `path`, wtedy nie będziesz musiał korzystać z wyrażeń regularnych.


## Zadanie 1 – wykonywane z wykładowcą
Napisz widok który będzie przypisany do adresu `/random/<max number>/` gdzie `max number` powinno być liczbą 
(na razie nie przejmuj się walidacją - po prostu przyjmij zmienną). 
Strona ta powinna pokazywać losową liczbę z zakresu od 0 do liczby podanej przez użytkownika. 
Strona powinna wyświetlać napis `Użytkownik podał wartość <max number>. Wylosowano liczbę: <wylosowana liczba>` 
oczywiście wstawiając odpowiednie zmienne w odpowiednie miejsca.

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^random/(?P<max_number>(\d)+)/$'
```
Mozesz też użyć metody `path`, wtedy nie będziesz musiał korzystać z wyrażeń regularnych.
```
'random/<int:max_number>/'
```


## Zadanie 2
Napisz widok który będzie przypisany do adresu `/random/<min number>/<max number>/` gdzie `min number` i `max number`
powinny być liczbami (na razie nie przejmuj się walidacją - po prostu przyjmij zmienną).
Strona ta powinna pokazywać losową liczbę z zakresu podanego przez użytkownika.
Strona powinna wyświetlać napis
`Użytkownik podał wartości <min number> i <max number>. Wylosowano liczbę: <wylosowana liczba>` 
oczywiście wstawiając odpowiednie zmienne w odpowiednie miejsca.  
Zauważ jak w zależności od różnej ilości parametrów wykonywane są widoki z zadań 1, 2 lub 3 (z poprzedniego działu).

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^random/(?P<min_number>(\d)+)/(?P<max_number>(\d)+)/$'
```

Mozesz też użyć metody `path`, wtedy nie będziesz musiał korzystać z wyrażeń regularnych.
```
'random/<int:min_number>/<int:max_number>/'
```


## Zadanie 3.
Napisz widok który będzie przypisany do adresu `/hello/<name>/` gdzie `name` powinno być ciągiem znaków
(na razie nie przejmuj się walidacją - po prostu przyjmij zmienną).
Strona ta powinna pokazywać napis `Witaj <name>` oczywiście wstawiając odpowiednią zmienną w odpowiednie miejsce.

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^hello/(?P<name>([A-Za-z])+)/$
```

Mozesz też użyć metody `path`, wtedy nie będziesz musiał korzystać z wyrażeń regularnych.
```
'hello/<str:name>/'

```
