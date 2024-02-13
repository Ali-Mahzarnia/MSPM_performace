


path_behave = 'AD_DECODE_data3.xlsx'
behave = read_xlsx(path_behave)

mesure_path ='fas_average_uni.xlsx'
measure = read_xlsx(mesure_path)

behave$measure = NA
for (i in 1:dim(measure)[1]) {
  name =measure [i,2] 
  name = substr(measure [i,2], 3,  6)
  index_behave = which(name ==behave$MRI_Exam )
  if (length(index_behave)>0)
  { behave$measure[index_behave]= as.numeric(measure [i,3]) }
  # print(name)
}

lm = lm( Delay_BensonTotal ~ measure , data=behave)
sqrt(mean((lm$residual)^2))
sd(behave$Delay_BensonTotal[!is.na(behave$Delay_BensonTotal)])
