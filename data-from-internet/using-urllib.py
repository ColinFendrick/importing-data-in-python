from urllib.request import urlopen, Request

url = "http://www.datacamp.com/teach/documentation"
# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

print(type(response))

# Be polite and close the response!
response.close()
