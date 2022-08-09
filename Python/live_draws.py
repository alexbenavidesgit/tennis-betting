import requests # pip install this

url = "https://tennis-odds.p.rapidapi.com/odds/prematch"
headers = {
	"X-RapidAPI-Key": "b40773ca22msh5a915ad4a2798c4p12b84cjsn7c4517677c21", # Free key, gives us 500 calls per month. 20 per minute
	"X-RapidAPI-Host": "tennis-odds.p.rapidapi.com"
}
newlist = []
i = 0

while i < 8: # TODO - fix this to be a real dynamic number instead of "8"
    # This API only gives us the max (50) results at a time so we need to paginate
    querystring = {"page":i,"size":"50"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    i = i + 1
    # Filter out womens matches
    x = 0
    maxL = len(response)
    while x < maxL:
        if "ATP" in response[x]['competition']['name']:
            newlist.append(response[x])
        elif "Challenger" in response[x]['competition']['name']:
            newlist.append(response[x])
        elif "ITF" in response[x]['competition']['name']:
            if "Women" in response[x]['competition']['name']:
                print("Skipping womens tournament")
            else:
                newlist.append(response[x])
        x = x + 1


# Print out our new list with only mens matches
# In the future we could only grab Challenger and Futures
print(newlist)