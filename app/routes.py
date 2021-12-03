from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Pokemon, Property
import requests
from app.crawl import run_all
from app.results import sample_query

@app.route("/")
def index():
    crawl_count = Pokemon.query.count()
    return render_template("index.html", crawl_count=crawl_count)

@app.route("/properties")
def properties():
    query = sample_query()
    data = query.all()
    return render_template("properties.html", data=data)

# TODO pass count to get
@app.route("/crawl")
def crawl():
    """Clears down tables and reloads - can take maz count parameter"""
    crawl_count = run_all()
    return render_template("index.html", crawl_count=crawl_count)
