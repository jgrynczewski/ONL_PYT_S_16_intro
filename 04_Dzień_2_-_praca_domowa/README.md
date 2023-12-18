## Zadanie 1

Wyobraź sobie serwis filmowy w stylu FilmWeb albo IMDB. 
Będziemy zbierać informacje o filmach i ludziach pracujących w filmie. W tym celu zdefiniuj następujace obiekty:

* `Person` a w nim następujące pola:
    * `first_name` string o max długości 32 znaki,
    * `last_name` string o max długości 32 znaki.
    
* `Genre` a w nim następujące pola:
    * `name` string o max długości 32 znaki,
    
* `Movie` czyli opis filmu, a w nim następujące pola:
    * `title`: string o max długości 128 znaków,
    * `director`: klucz obcy do modelu `Person`,
    * `screenplay`: klucz obcy do modelu `Person`.
    * `starring`: relacja wiele-do-wielu z modelem `Person`. Relacja powinna mieć dodatkowe pole `role` 
    (string 128 znaków, może być null), 
    czyli rola jaką gra aktor w filmie, tabela przechodnia powinna mieć nazwę `PersonMovie`, 
    * `year`: integer, rok produkcji filmu,
    * `rating`: float, ocena filmu: liczba od 1.0 do 10.0.
    * `genre` relacja wiele-do-wielu z modelem `Genre`.
Wypełnij modele danymi: zdefiniuj kilka osób: reżyserów, scenarzystów, aktorów. Dodaj kilka filmów.


**Podpowiedż:**

Prawdopodobnie będziesz musiał dodać własność `related_name` do pól `director` i `screenplay`. 
W innym przypadku, jeśli będziemy chcieli wypisać wszystkie filmy danej osoby, django nie będzie wiedziało, 
czy chodzi nam o filmy, w którym dana osoba jest reżyserem, czy scenarzystą. 

Więcej: [https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name)


## Zadanie 2

* Napisz widok, który udostępnisz pod adresem `/movies/`. Wypisze on listę tytułów filmowych posortowanych 
od najnowszego do najstarszego oraz rok produkcji, nazwisko reżysera i ocena. Tytuł filmu powinien być linkiem do URL-a 
`/movie-details/{id}/` gdzie id to identyfikator filmu.


## Zadanie 3

Napisz widok, który udostępnisz pod adresem `/movie-details/{id}/` gdzie id to identyfikator filmu.
 Widok pobierze dane o filmie z bazy (używając modelu) i wyświetli na stronie wszystkie posiadane informacje o filmie.


## Zadanie 4

* Dodaj widoki: 
    * `/persons/` - lista osób: przy nazwisku każdej osoby powinien być link do edycji. 
    Parametr powinien być przekazywany w URL-u. Na dole listy osób powinien być link "dodaj osobę".
    * `/edit-person/{id}/` - edycja osoby: po wejściu na link do edycji wyświetla się formularz edycji osoby. 
    Można zmienić dane i zapisać.
    * `/add-person/` - dodawanie osoby: po wejściu w link "dodaj osobę", powinien wyświetlić się pusty formularz, 
    w którym można dodać nową osobę i zapisać. Po prawidłowym dodaniu osoby powinniśmy zostać przeniesieni 
    pod adres `/persons`.
 

## Zadanie 5

* Zmodyfikuj widok `/movies/`
    * obok tytułu filmu dodaj link do edytowania filmu, parametr powinien być przekazany w URL-u. 
    Po kliknięciu w ten link program powinen wyciągnąć dane o tym filmie z bazy, a następnie pokazać formularz edycji 
    filmu wypełniony danymi wybranego filmu. Film można zapisać do bazy. 
    Strona edycji powinna być udostępniona pod adresem `/edit_movie/{id}/`
    * na dole listy filmów dodaj link "Dodaj film". Po kliknięciu w ten link powinien pokazać się pusty formularz 
    dodawania filmu. Film można zapisać do bazy. Strona edycji powinna być udostępniona pod adresem `/add-movie/`. 
    Po prawidłowym dodaniu filmu do bazy powinno nastąpić przekierowanie pod adres `/movies/`,
