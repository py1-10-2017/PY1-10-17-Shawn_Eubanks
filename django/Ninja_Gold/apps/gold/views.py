from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
        req.session['log'] = []
        print req.session
    context = {
        "gold" : req.session['gold'],
        "log" : req.session['log']
        }
    return render(req, 'gold/index.html', context)

def process_money(req):
    place = req.POST['location']

    if place == "farm":
        print "Farm"
        gold_found = random.randrange(9, 21)
        req.session['gold'] += gold_found
        log_str = "While working on the farm, you earned " + str(gold_found) + " gold!"
        req.session['log'].append(log_str)
    elif place == "cave":
        print "Cave"
        gold_found = random.randrange(4, 10)
        req.session['gold'] += gold_found
        log_str = "While exploring a cave you found " + str(gold_found) + " gold!"
        req.session['log'].append(log_str)
    elif place == "house":
        print "House"
        gold_found = random.randrange(2, 5)
        req.session['gold'] += gold_found
        log_str = "While cleaning the house, you found " + str(gold_found) + " gold!"
        req.session['log'].append(log_str)
    elif place == "casino":
        print "Casinox"
        gold_found = random.randrange(0, 50)

        # Create a chance 5 to 1 chance to win at the casino.
        chance = random.randrange(0, 5)
        win = random.randrange(0, 5)

        if int(win) == int(chance):
            req.session['gold'] += gold_found
            log_str = "While gambleing at the casino, you WON " + str(gold_found) + " gold!"
            req.session['log'].append(log_str)
        else:
            req.session['gold'] -= gold_found
            log_str = "While gambling at the casino, you LOST " + str(gold_found) + " gold!"
            req.session['log'].append(log_str)
    else:
        print "No Data"

    return redirect('/')

def reset(req):
    req.session['gold'] = 0
    req.session['log'] = ['Game Started']

    return redirect('/')
