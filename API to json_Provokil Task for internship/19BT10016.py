import requests

INTMAX = int(1e12)

author = input()

resp = requests.get(f'https://poetrydb.org/author/{author}')

totalLineCount = 0
countmin = INTMAX
    
listmin = []

respjson = resp.json()

if type(respjson) == list:
    for poem in respjson:
        CurrentLcount = int(poem["linecount"])
        CurrentPName = poem["title"]
        totalLineCount += CurrentLcount
        if CurrentLcount < countmin:
            countmin = CurrentLcount
            listmin.clear()
            listmin.append(CurrentPName)
        elif CurrentLcount == countmin:
            listmin.append(CurrentPName)

    print(totalLineCount)
    for poemname in listmin:
        print(poemname)
    
elif type(respjson) == dict and respjson["status"] == 404:
    print("0\n-")
