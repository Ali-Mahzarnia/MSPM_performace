#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:51:06 2024

@author: alex
"""

import nibabel as nib
import numpy as np
import os
import pandas as pd


path_mask =  '/Users/alex/Documents/MATLAB/ad_decode/mspm_ad_decode/L_01_c02/E4byage_gt_E3byage_binaryclusters.nii'

mask = nib.load(path_mask)
mask_data= mask.get_fdata()
#np.sum(mask_data)


 path_fa= '/Users/alex/brain_data/AD_DECODE/fa_zscored_u/smoothed/' 
 path_Vol = '/Users/alex/brain_data/AD_DECODE/jac_zscored_u/smoothed/'
 path_QSM= '/Users/alex/brain_data/AD_DECODE/QSM_zscored_u/smoothed/'

volumes = os.listdir(path_Vol); volumes = [v for v in volumes if  '.nii' in v ]
QSMs = os.listdir(path_QSM); QSMs = [v for v in QSMs if  '.nii' in v ]
fas = os.listdir(path_fa); fas = [v for v in fas if  '.nii' in v ]


volumes_masked_average = np.zeros((len(volumes)))
for i in range(len(volumes)):
    temp_image = nib.load(path_Vol+volumes[i] )
    temp_image_data = temp_image.get_fdata()
    volumes_masked_average[i] = np.mean(temp_image_data*mask_data)

volume_average_ID = np.column_stack((volumes,volumes_masked_average))
volume_average_ID = pd.DataFrame(volume_average_ID)
volume_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/volumes_average.xlsx")



QSM_masked_average = np.zeros((len(QSMs)))
for i in range(len(QSMs)):
    temp_image = nib.load(path_QSM+QSMs[i] )
    temp_image_data = temp_image.get_fdata()
    QSM_masked_average[i] = np.mean(temp_image_data*mask_data)

QSM_average_ID = np.column_stack((QSMs,QSM_masked_average))
QSM_average_ID = pd.DataFrame(QSM_average_ID)
QSM_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/QSM_average.xlsx")


fas_masked_average = np.zeros((len(fas)))
for i in range(len(fas)):
    temp_image = nib.load(path_fa+fas[i] )
    temp_image_data = temp_image.get_fdata()
    fas_masked_average[i] = np.mean(temp_image_data*mask_data)
    
fas_average_ID = np.column_stack((fas,fas_masked_average))
fas_average_ID = pd.DataFrame(fas_average_ID)
fas_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/fas_average.xlsx")


