from flask import Flask, render_template, redirect, url_for, request, session
import jinja2
from functions import *
import functions
import openai
import os
import time
import chat



app = Flask(__name__)
app.secret_key = 'super_extra_secret_key'

usage = []

@app.route('/')
def index():
    return redirect('/form')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        usage.append(request.form['zip_code'])
        usage.append(request.form['household_people'])
        usage.append(request.form['shower_duration'])
        usage.append(request.form['toilet_flushes'])
        usage.append(request.form['dishwasher_cycles'])
        
        global zipcode, ppl, shower, flush, cycles
        zipcode = usage[0]
        ppl = usage[1]
        shower = usage[2]
        flush = usage[3]
        cycles = usage[4]
        
        if (ppl == None) or (int(ppl) <= 0):
            usage.clear()
            return redirect('/form')
        
        return redirect('/stats')
    else:
        return render_template('form.html')


@app.route('/stats')
def success():
    
    functions.calculate_usage(shower, flush, cycles)
    functions.average_usage(zipcode)
    global total_usage, average_zip_usage, shower_usage, flush_usage, cycle_usage
    total_usage, shower_usage, flush_usage, cycle_usage = functions.calculate_usage(shower, flush, cycles)
    average_zip_usage = average_usage(zipcode)
    functions.comparing(total_usage, average_zip_usage)
    level, compliment = functions.comparing(total_usage, average_zip_usage)
    return render_template('comparison.html', shower_rate=shower_usage, toilet_rate=flush_usage,
                            dishwasher_rate=cycle_usage, your_usage=total_usage,
                            zip_world_usage=average_zip_usage, level=level, compliment=compliment)


@app.route("/chat")
def chat1():
    
    chat.role(usage, total_usage, shower_usage, flush_usage, cycle_usage, average_zip_usage)
    return render_template("index.html")

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chat.get_response(userText))

@app.route('/refresh')
def refresh():
    time.sleep(600) # Wait for 10 minutes
    return redirect('/refresh')


if __name__ == '__main__':
    app.run(debug=True)
