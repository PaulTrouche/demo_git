import os
import random
i=0
liste_club = {
1 :"Paris Saint Germain",
2: "Monaco",
3 : "OM",    
4 : "OL",
5 : "Nice",
6 : "Saint Etienne",
7: "Bordeaux",
8: "Rennes",
9: "Lille",
10: "Nantes",
11:"Man City",
12:"Tottenham",
13:"Chelsea",
14:"Liverpool",
15:"Arsenal",
16:"Man United",
17:"Everton",
18:"West Ham",
19:"Leicester",
20:"LA Galaxy",
21:"Cristal Palace",
22:"Watford",
23:"New Castle",
24:"Juventus",
25:"Milan AC",
26:"Inter Milan",
27:"As Roma",
28:"Naples",
29:"Lazio",
30:"Fiorentina",
31:"Torino",
32:"Udinese",
33:"Bayern Munich",
34:"Dortmund",
35:"Bayer Leverkusen",
36:"Wolfsburg",
37:"Moenchengladbach",
38:"Schalke 04",
39:"Francfort",
40:"Werder Brem",
41:"Leipzig",
43:"FC Barcelone",
44:"Real Madrid",
45:"Atletico Madrid",
46:"FC Séville",
47:"Villareal",
48:"Valance",
49:"Athletic Bilbao",
50:"Betis Séville",
52:"Real Sociedad",
53:"Porto",
54:"Benfica",
55:"Sporting",
56:"CSKA Moscou",
57:"Zenith",
59:"Besiktas",
60:"Fenerbache",
61:"Galatasaray",
62:"Ajax",
63:"Psv",
64:"River Plate",
58:"Boca Junior",
42:"Shakhtar",
51:"Santos",
}

liste = []
while i<64:
    de = random.randint(1, 64)
    while de not in liste:      
        print(liste_club[de])        
        i +=1
        if i%2==0:
          print("_____ \n\n")
        liste.append(de)
os.system("pause")


