import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'mamad1381'
TOEKN = 'jsdjhnvosheiwjfokjokjsjklnfd'

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
# body = {
#     "id":"graph1",
#     "name":"Walking",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu"
# }
# headers = {
#     "X-USER-TOKEN" :TOEKN
# }
# response = requests.post(url = GRAPH_ENDPOINT , json = body , headers = headers )
# print(response.text)

PIXEL_ENDPOINT = f"PIXELA_ENDPOINT/{}