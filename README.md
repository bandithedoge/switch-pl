![słodko](https://github.com/bandithedoge/switch-pl/blob/master/ss/lang.jpg)

[more screenshots/więcej screenshotów](https://imgur.com/a/mZQy2X8)

[GBAtemp](https://gbatemp.net/threads/switch-po-polsku-switch-pl-the-first-almost-full-switch-system-menu-polish-fan-translation.530672/)

[(Want that sexy theme?/Chcesz ten seksowny motyw?)](https://gbatemp.net/download/atmosphere-theme.35531/)

# Polski

## switch-pl - Pierwsze (prawie) pełne fanowskie tłumaczenie systemu Nintendo Switch!

Jesteśmy bardzo zadowoleni z wydania tego projektu, nad którym pracowaliśmy prawie tydzień. Przetłumaczyliśmy (w przybliżeniu) 1748 linijek tekstu na polski.

### Użyte oprogramowanie:

* [NXThemes Installer](https://github.com/exelix11/SwitchThemeInjector) do skopiowania plików systemowych
* [hactool](https://github.com/SciresM/hactool) do otworzenia wyżej wspomnianych plików systemowych
* [SARC Tool](https://github.com/aboood40091/SARC-Tool) do rozpakowania plików .szs
* [Uwizard](https://github.com/MrMysterio/Uwizard) do pakowania plików .msbt do .szs
* i oczywiście ~~Kurit'~~ [Kuriimu](https://github.com/IcySon55/Kuriimu) do edycji plików .msbt


### Co nie zostało przetłumaczone

#### Niemożliwe z obecnymi metodami (może modyfikowanie pamięci NAND?):

* eShop (oczywiście)
* Informacje o zdrowiu i bezpieczeństwie, Ważne informacje itd.

#### Niemożliwe w ogóle:

Jedna z rzeczy, których po prostu nie da się przetłumaczyć, to teksty typu "Offline/Played for X minutes/hours/days". Dlaczego? Nintendo zdecydowało się użyć dla nich bardzo niecodziennych tagów. Otwarte w Kuriimu wyglądają tak:

![Nauczcie się robić tagi!](https://i.imgur.com/mJTG5BT.png)

Każda próba edycji tych tekstów powodowała uszkodzenie pliku. To bardzo irytujące. Zanim znaleźliśmy powód, stało się to 6 razy. Dlatego ten tekst pozostał niezmieniony.


### Jak zainstalować

* Pobierz plik .zip dołączony do ostatniego [wyadnia](https://github.com/bandithedoge/switch-pl/releases) i rozpakuj folder "titles" do folderu Twojego CFW (atmosphere/reinx/sxos) na karcie SD. Włącz wybrany CFW ze wsparciem dla LayeredFS (jeżeli używałeś niestandardowych motywów, powinieneś wiedzieć co to).



# English

## switch-pl - The first (almost) full Nintendo Switch system menu fan translation!

We are extremely happy to release the project we've been working on for almost a week. We translated (approximately) 1748 lines of text to Polish.

### Software used:

* [NXThemes Installer](https://github.com/exelix11/SwitchThemeInjector) for dumping the files
* [hactool](https://github.com/SciresM/hactool) for extracting the dumps
* [SARC Tool](https://github.com/aboood40091/SARC-Tool) for extracting .szs files
* [Uwizard](https://github.com/MrMysterio/Uwizard) for packing .msbt files back to .szs
* ...and of course ~~Kurit'~~ [Kuriimu](https://github.com/IcySon55/Kuriimu) for editing .msbt files


### What's not translated

#### Can't be done with current methods (maybe with NAND editing?):

* eShop (obviously)
* Health and Safety Information, Important Information, etc.

#### Can't (and possibly won't) be translated at all:

The one thing that just can't be translated is the text that says "Offline/Played for X minutes/hours/days". Why? Nintendo used some very weird tags for these. When opened in Kuriimu, they look like this:

![Learn to do tags, Ninty](https://i.imgur.com/mJTG5BT.png)

Any attempt to edit this text results in file corruption. It was really annoying. It happened 6 times before we found out the issue. That's why we left it unchanged.


### How to install

* Download the .zip file attached to the latest [release](https://github.com/bandithedoge/switch-pl/releases) and extract the "titles" folder to your CFW's directory (atmosphere/reinx/sxos) on the SD card. Run the selected CFW with LayeredFS support (you should know about it if you've used custom themes).
