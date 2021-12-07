# Jaturing

**Python-kielellä toteutettu Turingin kone -simulaattori**

Sovelluksen avulla käyttäjä pystyy luomaan yksinkertaisia Turingin-koneita, ja simuloimaan niiden toimintaa. Sovellus on toteutettu Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

### Projektin tila
* Turingin koneen pääluokat metodeineen ovat valmiit
* Yksikkötestaus on lähes kattava
* Käyttöliittymä on perusosiltaan valmis
* Arkkitehtuurikuvausta ei ole vielä tehty

### Puuttuva toiminnallisuus
* Palaaminen alkutilaan
* Tiedostoon tallennus ja luku
* Tilakartan graafinen esitys
* Käyttöliittymä on vielä hiomaton

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
