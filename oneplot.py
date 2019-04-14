#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://matplotlib.org/examples/pylab_examples/log_demo.html
'''

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import random
import os

def startpy():

    plt.subplots_adjust(hspace=0.4)
    t = np.arange(0.01, 20.0, 0.01)   

    # log x axis
    plt.subplot(222)
    rno = random.randint(1, 50)
    plt.semilogx(t, np.sin(2 * np.pi * t * rno))
    plt.title('semilogx')
    plt.grid(True)
    plt.show()

def delete_old_images():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + '/static/images/'
    #shutil.rmtree(dir_path) 

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(dir_path):
        for file in f:            
            files.append(os.path.join(r, file))

    for f in files:
        #print(f)
        #shutil.rmtree(f) 
        os.remove(f)    

def predict_and_save(result_filename):

    delete_old_images()    
        
    plt.subplots_adjust(hspace=0.4)
    t = np.arange(0.01, 20.0, 0.01)   

    # log x axis
    plt.subplot(222)
    rno = random.randint(1, 50)
    plt.semilogx(t, np.sin(2 * np.pi * t * rno))
    plt.title('semilogx')
    plt.grid(True)    

    plt.savefig(result_filename)    
        

if __name__ == '__main__':
    startpy()