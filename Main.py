import Get_All_Links as GAL
import Download_Files as DF
import Get_Already_Downloaded as GAD
webpage = "https://www.vulnhub.com/?page="
Links = GAL.Manager(webpage)
Links = GAD.Manager(Links)
DF.Manager(Links)