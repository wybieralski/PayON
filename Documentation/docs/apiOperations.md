Page last revised on: {{ git_revision_date }}

## General Response

All response messages has the fields 'code' and 'response'. The code is the type HTTP Status, and the response always return a 'status' and a body message when necessary. 

## Errors

The API uses the following error codes:

| Code |	                                 Meaning                                                 |
|------| --------------------------------------------------------------------------------------------|
| 400  |	Bad Request -- Your request is invalid.                                                  |
| 401  |	Unauthorized -- Your API key is wrong.                                                   |
| 403  |	Forbidden -- Access to the requested resource or action is forbidden.                    |
| 404  |	Not Found -- The requested resource could not be found.                                  |
| 405  |	Method Not Allowed -- You tried to access an endpoint with an invalid method.            |
| 406  |	Not Acceptable -- You requested a format that isn't JSON.                                |
| 429  |	Too Many Requests -- You're sending too many requests.                                   |
| 500  |	Internal Server Error -- We had a problem with our server. Try again later.              |
| 503  |	Service Unavailable -- We're temporarily offline for maintenance. Please try again later.|