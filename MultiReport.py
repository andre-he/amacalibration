import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

import report

class MultiReport: 
    def _init_(self,names): 
        reports = []
        for name in names: 
            new_report = [name, report.Report(name)]
            reports.append(new_report) 
            
    def render_genparam: 
        for r in reports: 
            r[1].render_genparam()
            
    def render_i2c: 
        for r in reports: 
            r[1].render_i2c()
            
    def render_bgo: 
        for r in reports: 
            r[1].render_bgo()
            
    def render_calib_bandgapcontrol: 
        for r in reports: 
            r[1].render_calib_bandgapcontrol()   
            
    def render_calib_rampgain: 
        for r in reports: 
            r[1].render_calib_rampgain()       
            
    def render_icalib: 
        for r in reports: 
            r[1].render_icalib()        

    

        