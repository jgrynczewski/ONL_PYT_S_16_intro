## Zadanie 1
W zadaniu stwórz trzy widoki, które mają mieć następującą funkcjonalność:
* Pierwszy widok ma być przypisany pod adres `/set-session/` ma nastawiać informacje w sesji pod kluczem ```counter``` 
na **0**.
* Drugi widok ma być przypisany pod adres `/show-session/`  wyświetlać zawartość sesji pod kluczem ```counter``` 
i zwiększać ją o **1**. Jeżeli nie ma takich danych w sesji, to strona powinna wyświetlić odpowiednie informacje.
* Trzeci widok ma być przypisany pod adres `/delete-session/`  kasować dane z sesji 
(tylko te trzymane pod kluczem ```counter```).


## Zadanie 2
Napisz widok przypisany pod adres `/login/`. Widok ten powinien:
* W przypadku w którym wejdziemy na niego metodą GET wyświetlić formularz do logowania:  
```html
<form action="" method="POST">
    <label>
        Imię:
        <input type="text" name="name">
    </label>
    <input type="submit">
</form>
``` 
* W przypadku przesłania danych POST do sesji pod kluczem `loggedUser` wpisz przesłane imię.
* W przypadku w którym wejdziemy na niego metodą GET, a sesji są informacji pod kluczem `loggedUser` wyświetl komunikat 
`Witaj <imię>` - ta część polecenia wymaga modyfikacji kodu napisanego w pierwszym punkcie.

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd 
i nie przepuści użytkownika dalej. Aby temu zapobiec 
(tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz 
w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.


## Zadanie 3
Napisz widok pod adresem `/add-to-session/` który wyświetli następujący formularz:  
```html
<form action="#" method="POST">
    <label>
        Klucz:
        <input type="text" name="key">
    </label>
    <label>
        Wartość:
        <input type="text" name="value">
    </label>
    <input type="submit">
</form>
  ``` 
W przypadku wejścia na tą stronę metodą POST widok powinien dodawać do sesji przesłaną wartość (pod odpowiedni klucz).  
Następnie napisz widok pod adresem `/show-all-session/` który wyświetli w formie tabeli wszystkie dane znajdujące się
w sesji (zarówno klucz jak i wartość). 

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd 
i nie przepuści użytkownika dalej. Aby temu zapobiec (tylko na potrzeby ćwiczenia, 
CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu.
Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.


## Zadanie 4 (*)

* zmodyfikuj widok `add_game` tak, aby zapamiętać w sesji, który zespół był ostatnio edytowany (jako gospodarz),
* podczas ponownego wejścia na stronę odczytać zmienną sesyjną i ustawić listę HTML na pozycji odpowiadającej 
ostatnio edytowanemu klubowi (`<option ... selected>`)


## Zadanie 1
W tym zadaniu stwórz trzy strony:
* Pierwszy widok, przypisany do adresu `/set-cookie/`, ma nastawiać ciasteczko o nazwie ```User``` na Twoje imię.
* Drugi widok, przypisany do adresu `/show-cookie/`, ma wyświetlać zawartość ciasteczka ```User```. 
Jeżeli nie ma takiego ciasteczka, to powinna wyświetlić odpowiednie informacje.
* Trzeci widok, przypisany do adresu `/delete-cookie/`, powinien kasować ciasteczko o nazwie ```User```. 


## Zadanie 2
Napisz widok pod adresem `/add-to-cookie/` który wyświetli następujący formularz:  
```html
<form action="#" method="POST">
    <label>
        Klucz:
        <input type="text" name="key">
    </label>
    <label>
        Wartość:
        <input type="text" name="value">
    </label>
    <input type="submit" name="convertionType">
</form>
  ``` 
W przypadku wejścia na tą stronę metodą POST widok powinien dodawać do ciasteczek przesłaną wartość 
(pod odpowiedni nazwę).  
Następnie napisz widok pod adresem `/show-all-cookies/` który wyświetli w formie tabeli wszystkie dane znajdujące się 
w ciasteczkach do których masz dostep (zarówno nazwę ciasteczka jak i wartość). 

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, 
zgłosi błąd i nie przepuści użytkownika dalej. Aby temu zapobiec 
(tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. 
Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.


## Zadanie 3(*)

Stwórz widok `set_as_favourite` (udostępnij go pod odpowiednim  URL-em), który przyjmie paramter ID metodą GET, po czym:
* sprawdzi, czy ID jest poprawną liczbą, jeśli nie -- wyświetli informację o błędzie,
* sprawdzi, czy identyfikator istnieje w bazie danych (czy istnieje klub o takim ID). Jeśli nie -- wyświetli błąd 404,
* jeśli id jest poprawny, ustaw ciasteczko, ważne przez rok, w którym zapiszesz informację, który klub jest ulubionym 
klubem użytkownika.


## Zadanie 4(*)

Zmodyfikuj widok `league_table` tak, aby:
* ulubiony klub wyświetlał się na czerwono (odczytaj wartość ciasteczka),
* przy każdym klubie był link "zaznacz jako ulubiony", z wygenerowanym odpowiednim ID, 
prowadzący do widoku `/set-as-favourite/`.


## Zadanie 1

Napisz widok bazujący na klasie, który po wejściu metodą `GET` wyświetli formularz przyjmujący imię i nazwisko. 
Formularz ten ma przekierowywać na ten sam adres metodą `POST`.
Jeżeli strona została uruchomiona przez zapytanie POST, to ponad formularzem ma się wyświetlić napis 
`Witaj, <podane imię> <podane nazwisko>`. 
Możesz przerobić widok z zadania 1 z działu **POST formularze**
 

## Zadanie 2

Analogicznie do poprzedniego zadania, przerób zadanie 2 
z działu **POST formularze** tak, aby korzystało z **klasy** widoku.


## Zadanie 3

Przypomnij sobie zadanie 2 z działu **Modele**.
Napisz widok z użyciem klasy. Po wejściu metodą `GET` użytkownik powinien zobaczyć formularz z danymi na temat zespołu:
* name - nazwa zespołu
* year - rok założenia
* still_active - czy dalej aktywny
* genre - gatunek (pole typu select)

Po kliknięciu **Submit** dane powinny zostać przekazane na ten sam widok metodą `POST`.
Po wejściu metodą **POST** przechwyć dane z formularza i dodaj nowy zespół do bazy danych. Następnie wyświetl
użytkownikowi komunikat:

`Zespół <name> został pomyślnie zapisany w bazie danych!`,

gdzie `<name>` to nazwa zespołu, który został dodany do bazy.


## Zadanie 4 (*)

Popraw widoki w aplikacji football, tak aby bazowały na klasach. Pamiętaj o odpowiednich zmianach w pliku **urls.py**.



## Zadanie 1
Zmień routing dla zadań 1-3 z działu "Widoki" w następujący sposób:
* W zadaniu 1 zmienna `max number` musi być liczbą i posiadać od 2 do 4 cyfr,
* W zadaniu 2 zmienna `max number` musi być liczbą i posiadać dokładnie 4 cyfry, a zmienna `min number` 
musi mieć dokładnie 2 cyfry,
* W zadaniu 3 zmienna `name` musi składać się z tylko liter i zaczynać z dużej litery. 
 

## Zadanie 2

Popraw istniejące widoki, w których parametry przekazywane są przez GET w taki sposób, żeby były podawane w URL-ach.


## Zadanie 3 (*).

* Napisz widok `show_team_statistics`, który pokaże:
    * nazwę klubu,
    * sumę goli zdobytych,
    * sumę goli straconych,
    * liczbę meczów u siebie,
    * liczbę meczów na wyjeździe.
* zdefiniuj URL (w pliku **urls.py**), który będzie miał następujący schemat:
```/stats/<team-id>/```, gdzie **team_id**, to identyfikator klubu,

#### Pamiętaj, że odbieranie danych zapisanych w tak zdefiniowanym URL-u odbywa się inaczej niż do tej pory!
