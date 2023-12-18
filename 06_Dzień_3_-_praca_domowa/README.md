## Zadanie 1
Przerób widok `/movies/` tak, aby:
* na górze strony znajdowały się trzy przyciski do sortowania listy filmów wg. ich oceny 
(rosnąco, malejąco lub domyślnie), po naciśnięciu przycisku strona powinna się odświeżyć, 
pokazać posortowaną listę filmów oraz zapisać do sesji pod kluczem `sorted` wartość: 
   * `1` jeżeli wybrana została opcja malejąca (od najwyższej do najniższej oceny), 
   * `2` jeżeli wybrana została opcja rosnąca (od najniższej do najwyższej oceny),
   * `0` jeżeli została wybrana opcja domyślna (sortowanie domyślne wg roku produkcji, tak jak w zadaniu 2.),

* po ponownym wejściu na stronę lista była posortowana zgodnie z ostatnim wyborem


## Zadanie 2
Napisz widok `/search-movie/`, pod którym:

* widoczny będzie formularz, dzięki któremu można będzie wyszukiwać filmy, 
w formularzu powinny znajdować się następujące pola (użyj odpowiednich wartości dla atrybutu `name`):
   * `title` nazwa filmu - `name="title"`, 
   * `first_name` imię osoby - `name="first_name"`,
   * `last_name` nazwisko osoby - `name="last_name"`,
   * `year`rok - od `name="year_from"` do - `name="year_to"`,
   * `genre` gatunek - `name="genre"`, 
   * `rating` ocena - od `name="rating_from"` do - `name="rating_to"`.

* dodatkowe wymagania:
   * powinno być możliwe wyszukiwanie od-do wg roku produkcji, 
   * powinno być możliwe wyszukiwanie od-do wg oceny filmu,
   * powinno być możliwe wpisanie po przecinku kilku gatunków w polu `genre` i wyszukanie wszystkich filmów, 
   które są przypisane do tych gatunków,
   * po wpisaniu imienia lub nazwiska w polu `person` mają być wyszukane wszystkie filmy, 
   w których szukana osoba pełni jakąś rolę (jest reżyserem, scenarzystą, aktorem),
   * puste pole w wysłanym formularzu powinno oznaczać "wszystkie dane", 
   tzn. wysłanie całkowicie pustego formularza powinno wyszukać wszystkie dostępne w bazie filmy; 
   wpisanie w polu `last_name` wartości `Smith`i zostawienie pozostałych þól pustych powinno wyszukać wszystkie filmy, 
   w których jakąkolwiek rolę pełnią osoby o nazwisku `Smith`.

Wyniki wyszukiwania powinny pojawiać się na tej samej stronie tzn. `/search-movie/`.
