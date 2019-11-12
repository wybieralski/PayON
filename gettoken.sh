#!/bin/bash

#1) on https://console.developers.google.com/ register project and associate API from library
# OUTPUT: client_id,client_secret
client_id="338566750389-v2m95nvg2lh3tnq7s1ndbft5ib08ntpl.apps.googleusercontent.com"
client_secret="qa6DctRzCOaWfLygbj22aRx8"

#2) get authorization code at the following link using web browser
# OUTPUT: code
scope="https://www.googleapis.com/auth/drive"
url="https://accounts.google.com/o/oauth2/auth?client_id=$client_id&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=$scope&response_type=code"
code="..."

#3) use the code to obtain a OAuth2.0 Token
# OUTPUT: token and refresh_token in JSON
curl --request POST --data "code=$code&client_id=$client_id&client_secret=$client_secret&redirect_uri=urn:ietf:wg:oauth:2.0:oob&grant_type=authorization_code" https://accounts.google.com/o/oauth2/token
refresh_token="..."
token="..."

#4) refresh if needed
curl --request POST --data "--data 'client_id=$client_id&client_secret=$client_secret&refresh_token=$refresh_token&grant_type=refresh_token" https://accounts.google.com/o/oauth2/token

#5) get status of token
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=$token"

#6) use the token in a specific API (assed ass access_token=$token)
docid="http://localhost:8040/google/auth	"
curl "https://docs.google.com/spreadsheets/d/$docid/export?format=csv&access_token=$token"