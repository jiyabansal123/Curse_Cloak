import csv

cuss_words = [
    "arse", "arsehead", "arsehole", "ass", "ass hole", "asshole", "bastard", "bitch",
    "bloody", "bollocks", "brotherfucker", "bugger", "bullshit", "child-fucker",
    "Christ on a bike", "Christ on a cracker", "cock", "cocksucker", "crap", "cunt",
    "dammit", "damn", "damned", "damn it", "dick", "dick-head", "dickhead", "dumb ass", 
    "dumb-ass", "dumbass", "dyke", "faggot", "father-fucker", "fatherfucker", "fuck", 
    "fucker", "fucking", "god dammit", "goddammit", "God damn", "god damn", "goddamn", 
    "Goddamn", "goddamned", "goddamnit", "godsdamn", "hell", "holy shit", "horseshit", 
    "in shit", "jackarse", "jack-ass", "jackass", "Jesus Christ", "Jesus fuck", 
    "Jesus Harold Christ", "Jesus H. Christ", "Jesus, Mary and Joseph", "Jesus wept", 
    "kike", "mother fucker", "mother-fucker", "motherfucker", "nigga", "nigra", "nigger",
    "pigfucker","prostitute", "piss", "prick", "pussy","redneck", "shit", "shit ass", "shite", "sibling fucker", 
    "sisterfuck", "sisterfucker", "slut", "son of a bitch", "son of a whore", "spastic", "hello",
    "sweet Jesus", "twat", "wanker", "whore"
]

with open('cuss_words.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Cuss Word"])
    for word in cuss_words:
        writer.writerow([word])

print("CSV file created successfully.")
