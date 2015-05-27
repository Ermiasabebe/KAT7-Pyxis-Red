import Pyxis
import ms
import mqt
import im
import lsm
import stefcal
import numpy
import os
import sys
import math
import tempfile
from Pyxis.ModSupport import *



def calibrate(msname='$MS', lsmname='$LSM', tdlsec='$CALSEC',
              column='$COLUMN', do_dE=False, args=[],**kw):
    """ Calibrate MS """
    
    msname, lsmname, column, tdlsec = \
interpolate_locals('msname lsmname column tdlsec')
    
    v.MS = msname
    v.LSM = lsmname
    args = ["${ms.MS_TDL} ${lsm.LSM_TDL}"] + list(args)
    
    v.LSM = lsmname
    options = {}
    #option['ms_sel.msname']=v.MS
    #option['tiggerlsm.filename']=v.LSM
    if do_dE:
        """ add dE opts into options dict"""
        options.update(dict(diffgains=True))
    options.update(kw)
    stefcal.stefcal(msname,section=tdlsec,options=options,args=args)


def cal_ms(lsm0='$LSM0', start=0, stop=4):
    """ Run pipeline on a single MS"""
   
    lsm0 = II(lsm0)
   
    # Calibrate each MS
    #run_cmd = lambda : calibrate(lsmname=lsm0)
    #run_cmd = calibrate(lsmname=lsm0)
    v.MS = CONCAT_MS
    calibrate(lsmname=lsm0)
    
    #pper("MS",run_cmd)
    #calibrate(lsmname=lsm0)
    # image combined MS
    #ms.virtconcat(output=CONCAT_MS)
    
    v.MS = CONCAT_MS
    im.make_image(restore=True, psf=True, restore_lsm=False)
	
    # run source finder
    lsm.pybdsm_search(thresh_pix=5 , thresh_isl=3)
    v.LSM = lsm.PYBDSM_OUTPUT
    x.sh("tigger-convert --append $LSM $LSM0 $LSMFINAL -f")

    # make final restored map
    x.sh("tigger-restore ${im.RESTORED_IMAGE} $LSM0 ${im.FULLREST_IMAGE} -f ")
    
# use the following command to run the script: pyxis -j8 OUTDIR=Test cal_ms; where j8 -- 8 corresponds to the number of ms that will be excuted. If you have 5 ms in the directory, you have to use the command as: pyxis -j5 OUTDIR=Test cal_ms. Note that you can assign diffent folder name in the option OUTDIR. Eg. OUTDIR= PKSJ1939-allinfo, PKSJ0010-allinfo ...
