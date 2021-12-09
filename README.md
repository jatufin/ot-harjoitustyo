# Jaturing

**Python-kielellä toteutettu Turingin kone -simulaattori**

Sovelluksen avulla käyttäjä pystyy luomaan yksinkertaisia Turingin-koneita, ja simuloimaan niiden toimintaa. Sovellus on toteutettu Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

### Projektin tila
* Turingin koneen pääluokat metodeineen ovat valmiit
* Graafinen käyttöliittymä toimii, joskaan ei ole valmis
* Koneen tilan tallennus ja lataus tiedostoon toimivat
* Yksikkötestaus on lähes kattava
* Komentoriviargumenttien käsittelyä ei ole toteutettu
* Koneen graafista esitystä ulkopuolisia kirjastoja käyttäen ei ole toteutettu

### Puuttuva toiminnallisuus
* Tilakartan graafinen esitys
* Komentoriviargumenttien käsittely
* Käyttöliittymä on vielä hiomaton ja muunmuassa palaaminen alkutilaan puuttuu

### Dokumentaatio
[Työaikakirjaus](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Määrittelydokumentti](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
### Asennus ja käyttö

* Riippuvuuksien asennus:
```bash
poetry install
```

* Ohjelman käynnistys
```bash
poetry run invoke start
```

* Testaus
```bash
poetry run invoke test
```

* Testikattavuus
```bash
poetry run invoke coverage-report
```
