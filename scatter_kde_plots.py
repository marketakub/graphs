# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:40:50 2019

@author: Marketa
"""
import scipy as sp
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import interpn
from matplotlib import cm


def density_scatter( x , y, bins, ax = None, sort = True, **kwargs )   :

    if ax is None :
        fig , ax = plt.subplots(figsize=(6, 5))
    data , x_e, y_e = np.histogram2d( x, y, bins = bins)
    z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , np.vstack([x,y]).T , method = "splinef2d", bounds_error = False )

    # Sort the points by density, so that the densest points are plotted last
    if sort :
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]

    ax.scatter( x, y, c=z, cmap = cmap_vir, marker = ".", s = 4, **kwargs )
    plt.xlim(50,10000)
    plt.ylim(0,0.15)
    plt.xlabel('Fluorescence intensity [a.u.]') #fontsize = 10
    plt.ylabel('Deformation')
    plt.xticks()
    plt.yticks()
    plt.xscale("log")
    plt.gcf().set_tight_layout(True) 

    return ax

def kde_plot( x, y ) :
    
    plt.figure(figsize =(6,5))
    plt.rcParams["font.size"] = 20
    sns.set_style("white")
    # Some features are characteristic of 2D: color palette and wether or not color the lowest range
    #sns.kdeplot(x, y, cmap="Reds", shade=True, shade_lowest=False, n_levels = 30)
    sns.kdeplot(x, y, cbar=True)
    plt.xlim(-300,2800)
    plt.ylim(0,0.08)
    plt.xlabel('Fluorescence intensity [a.u.]') #fontsize = 10
    plt.ylabel('Deformation')
    plt.xticks()
    plt.yticks()
    plt.gcf().set_tight_layout(True) 

    return plt

######## colormap chan be changed here
cmap_vir = cm.get_cmap('viridis')


############## specify source file path
############## files are exported from Shapeout as .tsv with two columns (e.g. deformation and fluorescence)
DF_control_all = sp.genfromtxt('C:/Users/Marketa/Desktop/control_fluo.tsv')
DF_target_all = sp.genfromtxt('C:/Users/Marketa/Desktop/target_fluo.tsv')

# SCATTER PLOTS 
#if you want to swap the x and y axes, just swap 0 and 1 below
density_scatter(DF_control_all[:,1], DF_control_all[:,0], bins = [1000,100] )
density_scatter(DF_target_all[:,1], DF_target_all[:,0], bins = [1000,100] )


# KDE PLOTS
#if you want to swap the x and y axes, just swap 0 and 1 below
kde_plot(DF_control_all[:,1], DF_control_all[:,0])
kde_plot(DF_target_all[:,1], DF_target_all[:,0])