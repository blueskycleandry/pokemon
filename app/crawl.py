"""Search for and save Pokemons and their Properties"""
from flask import jsonify, request, url_for, abort
from app import db
from app.models import Pokemon, Property
from sqlalchemy import and_, func
from sqlalchemy.orm import aliased
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAXIMUM_EXTRACT = 100


def bulk_save(Table, data):
    """Bulk save data to Table"""
    rows = []
    for record in data:
        row = Table(**record)
        rows.append(row)
    db.session.add_all(rows)
    db.session.commit()


def traverse(dic, path=None):
    """Extract path from nested dicts.

    Copied from https://tinyurl.com/bddf8rww, amended for list
    """
    if not path:
        path = []
    if isinstance(dic, dict):
        for x in dic.keys():
            local_path = path[:]
            local_path.append(x)
            for b in traverse(dic[x], local_path):
                yield b
    elif isinstance(dic, list):
        n = 0
        for d in dic:
            n += 1
            for x in d.keys():
                local_path = path[:]
                local_path.append(n)  #  number in list
                local_path.append(x)
                for b in traverse(d[x], local_path):
                    yield b
    else:
        yield path, dic


def get_pokemons(max_items):
    """Get Pokemon and save to table."""
    # look up pokemon
    response = requests.get(BASE_URL + f"?limit={max_items}")
    pokemons = response.json()["results"]
    # add in pokemon id extractred from url
    for pokemon in pokemons:
        pokemon["id"] = pokemon["url"].replace(BASE_URL, "").replace("/", "")
    # save fast
    bulk_save(Pokemon, pokemons)
    return pokemons


def get_properties(pokemons):
    """Get Pokemon Properties and save to table"""
    for pokemon in pokemons:
        # map pokemon details
        name, url, id = pokemon["name"], pokemon["url"], pokemon["id"]
        # get properties for pokemon
        response = requests.get(url)
        properties = response.json()
        # build index recursively, and get value for each property
        property_list = []
        for i, j in traverse(properties):
            # start the property dict with 'fixed' attributes
            property = {"name": name, "pokemon_id": id, "value": j}
            # enumerate additional attributes and append
            for k, val in enumerate(i, 1):
                property[f"key_{k}"] = val
            property_list.append(property)
        # save fast
        bulk_save(Property, property_list)


def run_all(max_items=None):
    if not max_items:
        max_items = MAXIMUM_EXTRACT
    Pokemon.query.delete() 
    pokemons = get_pokemons(max_items)
    Property.query.delete()
    properties = get_properties(pokemons)
    return Pokemon.query.count()
    
    
if __name__ == "__main__":
    max_items = 100
    crawl_count = run_all(max_items)
