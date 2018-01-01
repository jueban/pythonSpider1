from conf import response
import json

json1 = response.Response()
json2 = json1.json('oh,shit', 2, 'oh,天呐')
print(json2)
