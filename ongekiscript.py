import os, json
from datetime import datetime
from glob import glob

def getConstants(): #get constant json, this is using from reiwa NEW ongeki gen
    constPath = './ongeki_const_all.json'
    if not os.path.isfile(constPath):
        print(f"Missing the ONGEKI chart constants json", + constPath)
        return None
    
    with open(constPath, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    const_map = {song["title"]: song for song in data}
    return const_map

def parseLatest(): #gets latest ongeki rating json in root
    directory = "./"  
    prefix = "ongekirating.tachi"  
    files = glob(os.path.join(directory, f"{prefix}*"))
    if not files:
        print(f"No files found with prefix '{prefix}' in {directory}")
        return None
    latest_file = max(files, key=os.path.getctime)
    if latest_file:
        print(f"Latest file: {latest_file}")
    with open(latest_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

#function changing technical score to rating 2dp by ongeki rating and chart constant
def scoreToRating(score, cc):
    if score >= 1007500:
        rating = cc + 2
    elif score >= 1000000:
        rating = cc + 1.5 + (0.01 * ((score - 1000000)/150 ) )
    elif score >= 990000:
        rating = cc + 1 + (0.01 * ((score - 990000)/200 ) )
    elif score >= 970000:
        rating = cc + (0.01 * ((score - 970000)/200 ) )
    elif score < 970000:
        rating = cc - (0.01 * ((970000 - score)/175 ) )
    return f"{rating:.2f}"


def mapToRating(data, constants):
    ratingList = []
    fmt = "%Y-%m-%dT%H:%M:%S.%f"
    newDate = '2022-03-02T15:00:00.000Z'
    newDate = newDate.rstrip("Z")
    newDate = datetime.strptime(newDate, fmt)

    for pb in data:
        sheet_id = pb.get("sheetId", "")
        title, difficulty = sheet_id.split("__onrt__")

        song_meta = constants.get(title)
        if not song_meta:
            continue
        if difficulty not in song_meta:
            continue
        cc = song_meta[difficulty].get("const")
        new = False
        date = song_meta.get("add_date")
        chartDate = date.rstrip("Z")
        chartDate = datetime.strptime(chartDate, fmt)

        if chartDate >= newDate : # is later than
            new = True

        score = pb.get("achievementRate", {}).get("score")
        if score is None:
            continue

        rating = scoreToRating(score, cc)
        ratingList.append({
            "title": title,
            "difficulty": difficulty,
            "cc" : cc,
            "rating": rating,
            "new" : new
        })
    return ratingList

def sortByRating(plays):
    sorted_ratings = sorted(plays, key=lambda x: float(x["rating"]), reverse=True)
    #print (sorted_ratings)

    b30 = sorted_ratings[:30]
    average = sum(float(entry["rating"]) for entry in b30) / 30
    average = f"{average:.2f}"

    print ("\nBEST 30 songs,  Average: " + str(average) + "\n")
    for index, entry in enumerate(b30, start=1):
        print(f"{index}. Title: {entry['title']}, Difficulty: {entry['difficulty']}, CC: {entry['cc']}, Rating: {entry['rating']}")

    return sorted_ratings, b30

#filter new entries from sorted rated list and print them 
def outNew(list):
    newList = [entry for entry in list if entry.get("new")]
    topNew = newList[:20]

    #print new 15 and 5 close to border
    print("\nNEW 15 songs in BRIGHT MEMORY\n")
    for index, entry in enumerate(topNew, start=1):
        print(f"{index}. Title: {entry['title']}, Difficulty: {entry['difficulty']}, CC: {entry['cc']}, Rating: {entry['rating']}")
        if index == 15:
            print("====== NEW 15 BORDER ======")

if __name__ == "__main__":
    playerData = parseLatest()
    constData = getConstants()
    rated = mapToRating(playerData, constData)
    sortedRated , b30 = sortByRating(rated)
    outNew(sortedRated)
    


    

    
