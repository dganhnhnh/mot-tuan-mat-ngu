# e = 5
# N = 12738331786144976628408584962601932300503981320657758070592328404991407468813883686645414154009656690238190579172789903683404637273437397117457373561689012444619426823650785246522182691404988042475126388162721182642829957361466397613478409042980767743277584606227337490629695231723390631048248673270268876696120185173349837701768591415602973998294483589229947507282787032145262364771540599514486278946374659551934084334916633373157348397197599205131909762202122809096952440358033382655250548960242984611039926964337280304882882174539682794142960610875918130570131509376815338749964656662270835139574992464445560548559
# l = 43
# c = 68829034175580818037595385380486058481146119314176779392653265570684777934377061660231023209592412738533887287426451491081941388406918844870814300682923844554566803973117705604463199616847051219603692011646985814554709262873409703222220556412167145138331879306747358983145108299652047663942904777455736334417346180833984486051537873634676492222592723854998319668594793557450355021302157167591762956712631060579566159150846015743846084975678356683223634570347682709248173273897202941560635688805593516302480381214349

from Crypto.Util.number import *
msg=401*19843*94543*836939*14739387793662769600588574606779488269903714565342937604799574647732040842718691228579
print(long_to_bytes(msg))

# c=msg^e factorize cực kì nhanh trên https://www.alpertron.com.ar/ECM.HTM 