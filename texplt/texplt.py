# -*- coding: utf-8 -*-
"""
Prepares matplotlib figures for publishing in Latex. Originally based
on [1]. Replaces figure() and savefig() calls.

[1] http://nipunbatra.github.io/2014/08/latexify/

@author: Christian Sieber <c.sieber@tum.de>
"""

import matplotlib.pyplot as plt
from math import sqrt


def texFigure(fig_width = None, 
              fig_height = None, 
              columns = 1, 
              font_size = 8, 
              font_scale = 100, 
              **kwargs):
    """
    Replaces matplotlib's figure() call and uses Latex-friendly default values.    

    Parameters
    -----------
    fig_width: float, optional
        Force a specific width of the figure.
    fig_height: float, optional
        Force a specific height of the figure.
    columns: {1, 2}, optional
        Set one or two column style mode.
    font_size: float, optional
        Set all fonts in the figure to a specific size. Default: 8
    font_scale: float, optional
        Scale all fonts in the figure. Default: 100 %
    """

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large: %d so will reduce to %d inches."
              % (fig_height, MAX_HEIGHT_INCHES))
        
        fig_height = MAX_HEIGHT_INCHES
        
    font_size = font_size * (font_scale / 100)

    params = {'backend': 'ps',
              'text.latex.preamble': [r'\usepackage{gensymb}'],
              'axes.labelsize': font_size, # fontsize for x and y labels (was 10)
              'axes.titlesize': font_size,
              'legend.fontsize': font_size, # was 10
              'xtick.labelsize': font_size,
              'ytick.labelsize': font_size,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'font.family': 'serif',
              'font.serif' : ['Times'],
              'font.size': font_size, # was 10
              'grid.alpha': 0.4,
              'axes.grid': True
    }

    plt.rcParams.update(params)
    
    return plt.figure(**kwargs) 
    
    
def texSaveFig(fname, **kwargs):
    """
    Replaces matplotlib's savefig() call.
    """

    plt.tight_layout()
    
    if 'bbox_inches' not in kwargs:
        kwargs['bbox_inches'] = 'tight'
    
    if 'kwargs' not in kwargs:
        kwargs['pad_inches'] = 0
    
    return plt.savefig(fname, **kwargs)
    

def strToTex(string):
    return string.replace('_','\_')
    