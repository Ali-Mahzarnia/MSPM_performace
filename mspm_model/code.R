
library(stringr)

path_behave = 'AD_DECODE_data3.xlsx'
behave = read_xlsx(path_behave)

mesureQSM_path ='QSM_average.xlsx'
measureQSM = read_xlsx(mesureQSM_path)
# 
# for (l in 1:dim(measureQSM)[1]) {
#   name = measureQSM[l,2]
#   name = substr(name , 3,  6)
#   measureQSM[l,2] = name
#   }

behave$measureQSM = NA
for (i in 1:dim(measureQSM)[1]) {
  name =measureQSM [i,2] 
  name = substr(name, 3,  6)
  index_behave = which(name ==behave$MRI_Exam )
  if (length(index_behave)>0)
  { behave$measureQSM[index_behave]= as.numeric(measureQSM [i,3]) }
  # print(name)
}


mesureFA_path ='fas_average.xlsx'
measureFA = read_xlsx(mesureFA_path)


behave$measureFA = NA
for (i in 1:dim(measureFA)[1]) {
  name =measureFA [i,2] 
  name = substr(name, 3,  6)
  index_behave = which(name ==behave$MRI_Exam )
  if (length(index_behave)>0)
  { behave$measureFA[index_behave]= as.numeric(measureFA[i,3]) }
  # print(name)
}

# for (l in 1:dim(measureFA)[1]) {
#   name = measureFA[l,2]
#   name = substr(name , 3,  6)
#   measureFA[l,2] = name
# }

mesureVol_path ='volumes_average.xlsx'
measureVol = read_xlsx(mesureVol_path)

# for (l in 1:dim(measureVol)[1]) {
#   name = measureVol[l,2]
#   name = substr(name , 3,  6)
#   measureVol[l,2] = name
# }



behave$measureVol = NA
for (i in 1:dim(measureVol)[1]) {
  name =measureVol [i,2] 
  name = substr(name, 3,  6)
  index_behave = which(name ==behave$MRI_Exam )
  if (length(index_behave)>0)
  { behave$measureVol[index_behave]= as.numeric(measureVol[i,3]) }
  # print(name)
}



# 
# common_ID_path = 'QSM_cell_mspm.txt'
# common_ID = read.delim(common_ID_path, header = F)
# for (j in 1:dim(common_ID)[1]) {
#   ID = common_ID[j,1] 
#   ID = str_remove(ID, "/Users/alex/brain_data/AD_DECODE/QSM_zscored_u/smoothed/S0")
#   ID = str_remove(ID, "_QSM_to_MDT.nii.gz,1 ")
#   ID = str_remove(ID, "_QSM_to_MDT.nii.gz,1")
#   common_ID[j,1] =ID
#   }
# 
# 
# 
# 

lm = lm( Delay_BensonTotal ~ measureQSM + measureFA +measureVol  , data=behave)
sqrt(mean((lm$residual)^2))
sd(behave$Delay_BensonTotal[!is.na(behave$Delay_BensonTotal)])
