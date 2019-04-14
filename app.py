#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask
'''

import os
from flask import Flask
import io
import os, glob
import np
import shutil
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask import render_template
from flask import request
import oneplot as op

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello():
    return render_template('index.html')    

'''
@app.route('/remove')
def remove():
    delete_old_images()
    return dir_path
'''    

@app.route('/plot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def string2int_array(ar):
    arint = []
    for i in ar:
        print(i)
        arint.append(int(i))

    return arint

# No caching at all for API endpoints.
# https://stackoverflow.com/questions/45583828/python-flask-not-updating-images
@app.after_request
def add_header(response):
    print('called special method')
    response.cache_control.no_store = True
    response.cache_control.public = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response    

@app.route('/', methods=['POST'])
def show_result():

    rid = str(random.randint(1, 5000))
    result_filename = 'static/images/one_'+rid+'.png'
    
    op.predict_and_save(result_filename)
    
    return render_template('index.html', result = 1,  name = 'plot', url = '/'+result_filename)    

'''
    https://matplotlib.org/examples/pylab_examples/log_demo.html
'''
def plot():
    pass
    
    # log x axis
    plt.subplot(222)
    plt.semilogx(t, np.sin(2*np.pi*t))
    plt.title('semilogx')
    plt.grid(True)    

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig    

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8086))
    
    app.run(host= host, port = port, use_reloader = False)