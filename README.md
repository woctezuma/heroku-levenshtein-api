# Heroku Levenshtein API

Deploy an API built with Flask on Heroku, in order to match game names with Levenshtein distance.

## Data

Data consists of app ids and names from the Steam store (~30k games) downloaded [on January 9, 2021][data-snapshot].

## Usage

To create the database of game names in lower case:

```bash
python app/file_utils.py
```

To run locally:

```bash
python run.py
```

To deploy:

```bash
heroku login
heroku create
git push heroku main
```

## Web App

The web app can be accessed at this URL:

> https://arcane-springs-42307.herokuapp.com/

To ask for results about "Cyberpunk 2077", and constrain the response to 10 matches:

> [https://arcane-springs-42307.herokuapp.com/find/?name=\"Cyberpunk 2077\"&n=10][api-example]

## CORS and rate-limits

If you want to make your web app accessible from a Single-Page Application,
e.g. written in Svelte, then you will want to specify CORS and rate-limits.

See the `cors` branch of my repository for more information.

## References

- [`heroku-flask-api`][flask-clip-api]
- [`heroku-levenshtein-api`][flask-levenshtein-api]

<!-- Definitions -->

[data-snapshot]: <https://github.com/woctezuma/steam-store-snapshots>

[flask-clip-api]: <https://github.com/woctezuma/heroku-flask-api>

[flask-levenshtein-api]: <https://github.com/woctezuma/heroku-levenshtein-api>

[api-example]: <https://arcane-springs-42307.herokuapp.com/find/?name="Cyberpunk 2077"&n=10>
