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
import math

#path_mask =  '/Users/alex/Documents/MATLAB/ad_decode/JAC_univariate_age_interaction/jac_e4byagegte3byagep0p05fdrc9788.nii'

#mask = nib.load(path_mask)
#mask_data= mask.get_fdata()
#np.sum(mask_data)


path_fa= '/Users/alex/brain_data/AD_DECODE/fa_zscored_u/smoothed/' 
path_Vol = '/Users/alex/brain_data/AD_DECODE/jac_zscored_u/smoothed/'
path_QSM= '/Users/alex/brain_data/AD_DECODE/QSM_zscored_u/smoothed/'

volumes = os.listdir(path_Vol); volumes = [v for v in volumes if  '.nii' in v ]
QSMs = os.listdir(path_QSM); QSMs = [v for v in QSMs if  '.nii' in v ]
fas = os.listdir(path_fa); fas = [v for v in fas if  '.nii' in v ]




path_mask =  '/Users/alex/Documents/MATLAB/ad_decode/JAC_univariate_age_interaction/jac_e4byagegte3byagep0p05fdrc9788.nii'

mask = nib.load(path_mask)
mask_data= mask.get_fdata()

mask_data = np.nan_to_num(mask_data, copy=True, nan=0.0, posinf=None, neginf=None)
mask_data = np.where(mask_data != 0, 1, mask_data)


volumes_masked_average = np.zeros((len(volumes)))
for i in range(len(volumes)):
    temp_image = nib.load(path_Vol+volumes[i] )
    temp_image_data = temp_image.get_fdata()
    volumes_masked_average[i] = np.mean(temp_image_data*mask_data)

volume_average_ID = np.column_stack((volumes,volumes_masked_average))
volume_average_ID = pd.DataFrame(volume_average_ID)
volume_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/volumes_average_uni.xlsx")





path_mask =  '/Users/alex/Documents/MATLAB/ad_decode/QSM_univariate_age_interaction/QSM_E4changesfastetE3FDRC1816.nii'

mask = nib.load(path_mask)
mask_data= mask.get_fdata()


mask_data = np.nan_to_num(mask_data, copy=True, nan=0.0, posinf=None, neginf=None)
mask_data = np.where(mask_data != 0, 1, mask_data)


file_result=nib.Nifti1Image(mask_data, mask.affine, mask.header)
nib.save(file_result, "/Users/alex/Documents/MATLAB/ad_decode/QSM_univariate_age_interaction/E4byage_gt_E3byage_Nariman_test.nii")


QSM_masked_average = np.zeros((len(QSMs)))
for i in range(len(QSMs)):
    temp_image = nib.load(path_QSM+QSMs[i] )
    temp_image_data = temp_image.get_fdata()
    QSM_masked_average[i] = np.mean(temp_image_data*mask_data)

QSM_average_ID = np.column_stack((QSMs,QSM_masked_average))
QSM_average_ID = pd.DataFrame(QSM_average_ID)
QSM_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/QSM_average_uni.xlsx")




path_mask =  '/Users/alex/Documents/MATLAB/ad_decode/FA_univariate_age_interaction/FA_E4byagegtE3byagep0p05FDRc2190.nii'

mask = nib.load(path_mask)
mask_data= mask.get_fdata()

mask_data = np.nan_to_num(mask_data, copy=True, nan=0.0, posinf=None, neginf=None)
mask_data = np.where(mask_data != 0, 1, mask_data)

fas_masked_average = np.zeros((len(fas)))
for i in range(len(fas)):
    temp_image = nib.load(path_fa+fas[i] )
    temp_image_data = temp_image.get_fdata()
    fas_masked_average[i] = np.mean(temp_image_data*mask_data)
    
fas_average_ID = np.column_stack((fas,fas_masked_average))
fas_average_ID = pd.DataFrame(fas_average_ID)
fas_average_ID.to_excel(excel_writer = "/Users/alex/AlexBadea_MyPapers/MSPM/masked_average/fas_average_uni.xlsx")


