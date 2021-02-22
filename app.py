# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:20:56 2021

@author:C Vijaya Kumar
"""

from flask import Flask, render_template,url_for




app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/about/')
def about():

    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)