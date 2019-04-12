# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:19:29 2019

@author: Marketa
"""


import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



DF_control = sp.genfromtxt('E:/control_fluo.tsv')
DF_target = sp.genfromtxt('E:/target_fluo.tsv')

plt.figure(figsize =(6,5))
sns.distplot(DF_control, hist = True, color = 'black', bins = range(1,5000, 100), norm_hist =True, kde= False, hist_kws=dict(alpha=0.8))
sns.distplot(DF_target, hist = True, color = 'red', bins = range(1,5000, 100), norm_hist =True, kde= False, hist_kws=dict(alpha=0.7))

plt.rcParams["font.size"] = 20
plt.xlim(1,2800)
plt.ylim(0,0.0041, 0.002)
plt.xlabel('Fluorescence intensity [a.u.]') #fontsize = 10
plt.ylabel('Normalised counts')
plt.legend(('Control','Target'))
plt.xticks()
plt.yticks()
plt.gcf().set_tight_layout(True) 
#plt.title('Control sample')
#plt.grid(axis='y', alpha=0.75)
#plt.xscale("log")
plt.savefig('plot2.png')



#_________________________________________________________________

DF_control_all = sp.genfromtxt('C:/Users/Marketa/Desktop/control_fluo.tsv')
DF_target_all = sp.genfromtxt('C:/Users/Marketa/Desktop/target_fluo.tsv')

plt.figure(figsize =(6,5))
plt.rcParams["font.size"] = 20
sns.set_style("white")
# Some features are characteristic of 2D: color palette and wether or not color the lowest range
sns.kdeplot(DF_control_all[:,1], DF_control_all[:,0], cmap="Greys", shade=True, shade_lowest=False, n_levels = 30)
#sns.scatterplot(DF_control_all[:,1], DF_control_all[:,0], marker = "+", color = ".2")
sns.kdeplot(DF_control_all[:,1], DF_control_all[:,0])
plt.xlim(-300,2800)
plt.ylim(0,0.08)
plt.xlabel('Fluorescence intensity [a.u.]') #fontsize = 10
plt.ylabel('Deformation')
plt.xticks()
plt.yticks()
plt.gcf().set_tight_layout(True) 

plt.figure(figsize =(6,5))
plt.rcParams["font.size"] = 20
sns.set_style("white")
# Some features are characteristic of 2D: color palette and wether or not color the lowest range
sns.kdeplot(DF_target_all[:,1], DF_target_all[:,0], cmap="Reds", shade=True, shade_lowest=False, n_levels = 30)
#sns.scatterplot(DF_control_all[:,1], DF_control_all[:,0], marker = "+", color = ".2")
sns.kdeplot(DF_target_all[:,1], DF_target_all[:,0])
plt.xlim(-300,2800)
plt.ylim(0,0.08)
plt.xlabel('Fluorescence intensity [a.u.]') #fontsize = 10
plt.ylabel('Deformation')
plt.xticks()
plt.yticks()
plt.gcf().set_tight_layout(True) 
