library(data.table)
library(stringr)
x=fread("C:/Users/celia/Downloads/List_of_suicides.csv", sep = ",", header=T, encoding = "UTF-8")
head(x)
names(x)
x2=x[content!="no_matching_content",.(pages_names, subcategory, content)]
x2=x2[, sep_text:="****"][, subcategory:=paste("*cat_",subcategory,sep="")][, pages_names:=paste("*page_",pages_names, sep="")][,content:=paste("\n",content, sep="")][,.(sep_text, pages_names, subcategory, content)]
x2=setorder(x2,content)
x3=x2[,.SD[1], by=content][,.(sep_text, pages_names, subcategory, content)]
x3=x3[,content:=str_replace_all(content,c("[:digit:]"=""," & "="_and_","-year"="year", "-mid"="mid","-"="_", "year old"="year_old","'"=" ","Washington ,  D . C ."="Washington_DC", "Washington,_D.C"="Washington_DC", "New York City"="New_York_City","New York"="New_York","\n( *)"="\n", "([:space:]*[.][:space:]*)"=". ","([:space:]*[,][:space:]*)"=", ","([:space:]*[;][:space:]*)"=" ; ","([:space:]*[:][:space:]*)"=" : ","\"\""="\"","Madame d Angoulême"="Madame_d_Angoulême", "St. "="St_"))]
x3=x3[,pages_names:=str_replace_all(pages_names,c("[:digit:]"=""," & "="_and_","-year"="year", "-mid"="mid","-"="_", "year old"="year_old","'"=" ","Washington ,  D . C ."="Washington_DC", "Washington,_D.C"="Washington_DC", "New York City"="New_York_City","New York"="New_York","\n( *)"="\n", "([:space:]*[.][:space:]*)"=". ","([:space:]*[,][:space:]*)"=", ","([:space:]*[;][:space:]*)"=" ; ","([:space:]*[:][:space:]*)"=" : ","\"\""="\"","Madame d Angoulême"="Madame_d_Angoulême", "St. "="St_"))]
x3=x3[,subcategory:=str_replace_all(subcategory,c("[:digit:]"=""," & "="_and_","-year"="year", "-mid"="mid","-"="_", "year old"="year_old","'"=" ","Washington ,  D . C ."="Washington_DC", "Washington,_D.C"="Washington_DC", "New York City"="New_York_City","New York"="New_York","\n( *)"="\n", "([:space:]*[.][:space:]*)"=". ","([:space:]*[,][:space:]*)"=", ","([:space:]*[;][:space:]*)"=" ; ","([:space:]*[:][:space:]*)"=" : ","\"\""="\"","Madame d Angoulême"="Madame_d_Angoulême", "St. "="St_"))]
x4=x3
x4[4,]


fwrite(x3, "C:/Users/celia/Documents/MIASHS/M1/terbis/gEPHI/donnees2.txt", sep = " ", quote=F)
