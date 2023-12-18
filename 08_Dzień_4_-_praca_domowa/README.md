## Zadanie 1
Nadaj wszystkim URL-om etykietki (trzeci argument w definicji URL-a). Pamiętaj, że etykiety powinny być unikalne. 
(Jeśli masz wątpliwości jak to zrobić, zajrzyj tutaj: 
[https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls](https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls))


## Zadanie 2
Przerób widoki tak, aby w linkach odwoływały się do etykietek. 

Jeśli masz wątpliwości jak to zrobić, zajrzyj tutaj: 
[https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls](https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls)


## Zadanie 3
Przerób widoki `/persons/` oraz `/movies/` tak, aby spełniały następujące warunki:
* przy nazwisku każdej osoby oraz przy tytule każdego filmu powinny znajdować się przyciski pozwalające na usunięcie 
osoby i filmu
* przyciski powinny przekierowywać pod adresy: `/del-person/{id}/` dla osoby oraz `/del-movie/{id}/` dla filmu.
* po poprawnym usunięciu osoby oraz filmu, na ekranie powinien pojawić się komunikat `Usunięto osobę!` 
lub `Usunięto film!`


## Zadanie 4
Upewnij się, że serwis filmowy jest spójny graficznie. Na każdej stronie powinno znajdować się menu pozwalające 
na łatwe nawigowanie po całym serwisie (odnośniki do listy osób, listy filmów, formularza wyszukiwania)


## Zadanie 5 (*).
Jeśli kod **HTML** umieściłeś w zmiennych w widokach, przenieś go do zewnętrznych plików HTML.
Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.
