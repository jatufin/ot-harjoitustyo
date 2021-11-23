# Jaturing

**Python-kielellä toteutettu Turingin kone -simulaattori**

Sovelluksen avulla käyttäjä pystyy luomaan yksinkertaisia Turingin-koneita, ja simuloimaan niiden toimintaa. Sovellus on toteutettu Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotuotanto harjoitustyönä.

### Projektin tila
* Turingin koneen pääluokat metodeineen ovat lähes valmiit
* Nauhaa esittävän Tape-luokan osalta on yksikkötestien rakentaminen aloitettu
* Käyttöliittymää ja tiedostotoimintoja ei ole vielä aloitettu
* Arkkitehtuurikuvausta ei ole vielä tehty

### Dokumentaatio
[Työaikakirjaus](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Määrittelydokumentti](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)


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
