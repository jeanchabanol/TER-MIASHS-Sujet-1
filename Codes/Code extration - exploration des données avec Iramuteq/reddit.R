library(jsonlite)
library(data.table)
library(stringr)

setwd("C:/Users/celia/Documents/MIASHS/M1/terbis/reddit/données/")


# liste des csv à importer :
liste_json <- list.files(recursive = TRUE,"Suicide", pattern = ".json", full.names = TRUE)
# import des données :
dt=as.data.frame(t(sapply(liste_json, fromJSON)))
#Transformation en data.table
setDT(dt)
#Modification du DT
#Suicide
dt=dt[!subreddit=="u_RedditCareResources",][, ':='(sep_text="****",suicide="*suicide_T",subreddit=paste("*subreddit_",subreddit,sep=""),content=paste("\n",title,"\n",text,sep=""))][,.(sep_text,suicide,subreddit,content) ]
#Nettoyage
#On garde seulment les ccaractères autorisés
dt[,content:=iconv(content,from = 'UTF-8', to = 'ASCII//TRANSLIT')]
#[,content:=str_replace_all(content,c("[:digit:]"=""," & "=" and ","-year"="year", "-mid"="mid","-"="_", "year old"="year_old","'"=" ","[*]"=""))]

#On enregistre en fichier texte
fwrite(dt, "donnees_suicide.txt", sep = " ", quote=F)



