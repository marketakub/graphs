# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:38:46 2019

@author: Marketa
"""
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns


########## here the input files have only 1 column (from Shapeout export e.g. fl-1 channel, or deformation)
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
