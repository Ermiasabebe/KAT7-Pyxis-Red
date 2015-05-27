

The pipeline first produce an image from the data after cleaning. From the image, it extracts source/s and makes local sky model (lsm). Using the lsm, self-calibration will be done. Note that the measurement set is the concatenation of all the MSs observed during the research period. However, for some of the datasets the selfcalibration couldn't proceed by giving an error:

- "***CRITICAL*** 23.70% (2730/11520) data points were flagged in the stefcal process. Can not take. Stopping!" 
- Too many data points (23.70%) flagged. Check your stefcal settings?

We need to see any alternative in our setting to correct for the falgging.

After extracting the sources in the images, the reliability of the sources is also checked using the script from Lorato. The analysis gives whether the sources are reliable to some extent based on some criteria (Lorato or Sphe can describe their method very well). The analysis actually rejects some of the extarcted sources as it considers them as unreliable (the reliablity is 0). 
