# Jaturing

**Python-kielellä toteutettu Turingin kone -simulaattori**

Sovelluksen avulla käyttäjä pystyy luomaan yksinkertaisia Turingin-koneita, ja simuloimaan niiden toimintaa. Sovellus on toteutettu Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

### Projektin tila
* Turingin koneen pääluokat ovat valmiit ja toimivat
* Graafinen käyttöliittymä toimii
* Koneen tilan tallennus ja lataus tiedostoon toimivat
* Tiloja ja niiden välisiä siirtymiä esittävä graafi on upotettu ulkopuolista kirjastoa käyttäen käyttöliittymään
* Yksikkötestaus on lähes kattava

### Puuttuva toiminnallisuus
* Komentoriviargumenttien käsittelyä ei ole toteutettu
* Käyttöliittymä on vielä hiomaton, eikä graafi ole täysin tyydyttävä

### Dokumentaatio
[Käyttöohje](https://github.com/jatufin/ot-harjoitustyo/blob/master/dokumentaatio/kaytto-ohje.md)

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
