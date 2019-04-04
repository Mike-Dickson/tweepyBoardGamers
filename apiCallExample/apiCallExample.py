import http.client, urllib.request, urllib.parse, urllib.error, base64
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '59b9f21a57ac40a2a97453c6f9190bed'
}
params = urllib.parse.urlencode({ })

body = {
  "documents": [
        {
            "language": "en",
            "id": "1",
            "text": "First document. Hello world."
        },
        {
            "language": "en",
            "id": "2",
            "text": "Final document. Calling Cognitive API again."
        }
    ]
}
try:
    conn = http.client.HTTPSConnection('westus2.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))