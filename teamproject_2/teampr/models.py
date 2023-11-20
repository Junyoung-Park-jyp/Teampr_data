from teampr import db
import os
import pandas as pd
import sqlite3
import pymysql
from flask import Flask, render_template, request, session, redirect, url_for


class WineData(db.Model):
    __tablename__ = 'wine_info'
    id = db.Column(db.Integer,primary_key=True)
    prod_name = db.Column(db.String(200), nullable=False)
    winery = db.Column(db.Text(), nullable=False)
    wine_type = db.Column(db.Text(), nullable=False)    
    score = db.Column(db.Float())
    price = db.Column(db.Integer, nullable=False)
    flavor1 = db.Column(db.Text())
    flavor2 = db.Column(db.Text())
    prod_link = db.Column(db.Text(), nullable=False)

class RateBeer(db.Model):
    __tablename__ = 'ratebeer_data'
    index = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Text(), nullable=False)
    prod_name = db.Column(db.String(200), nullable=False) 
    review_date = db.Column(db.Date(), nullable=False)
    score = db.Column(db.Float(), nullable=False)
    aroma = db.Column(db.Integer())
    appearance = db.Column(db.Integer())
    flavor = db.Column(db.Integer())
    mouthfeel = db.Column(db.Integer())
    overall = db.Column(db.Integer())

class NonAlcoholBeer(db.Model):
    __tablename__ = 'nonalco_beer'
    index = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(200), nullable=False) 
    price = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float(), nullable=False)
    review_text = db.Column(db.Text(), nullable=False)
    review_date = db.Column(db.Date(), nullable=False)
    review_text2 = db.Column(db.Text())

class Whiskey(db.Model):
    __tablename__ = 'whiskey_data'
    index = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(200), nullable=False) 
    prod_link = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(50), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Float(), nullable=False)