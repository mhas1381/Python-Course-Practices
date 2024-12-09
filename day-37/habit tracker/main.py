import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'mamad1381'
TOEKN = 'jsdjhnvosheiwjfokjokjsjklnfd'
GRAPH_ID = "graph1"
# user_params = {
#     'token' :TOEKN,
#     'username' : USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url = PIXELA_ENDPOINT , json = user_params)
# response.raise_for_status()
# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
body = {
    "id":GRAPH_ID,
    "name":"Walking",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN" :TOEKN
}
# response = requests.post(url = GRAPH_ENDPOINT , json = body , headers = headers )
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
body = {
    # "date" : today,
    "quantity":"14",

}
# response = requests.post(url = PIXEL_ENDPOINT , json = body , headers=headers )
# print(response.text)
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.put(url = UPDATE_PIXEL_ENDPOINT , json = body , headers=headers )

response = requests.delete(url = UPDATE_PIXEL_ENDPOINT ,headers=headers )

print(response.text)
