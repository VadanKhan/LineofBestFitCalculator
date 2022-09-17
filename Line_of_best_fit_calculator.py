# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:34:45 2021

@author: Vadan
"""

import numpy as np

xvals2 = xvals**2
yvals2 = yvals**2
xyvals = xvals*yvals
xmean = np.mean(xvals)
ymean = np.mean(yvals)
sumx = np.sum(xvals)
sumy = np.sum(yvals)
sumx2 = np.sum(xvals2)
sumy2 = np.sum(yvals2)
sumxy = np.sum(xyvals)
Sxy = sumxy - (sumx*sumy)/n
Sxx = sumx2 - (sumx**2)/n

B = Sxy/Sxx
print('Gradient of line is: ',B)
a = ymean - B*xmean
print('y-intercept of line is: ',a)
Tlin = B*xvals + a