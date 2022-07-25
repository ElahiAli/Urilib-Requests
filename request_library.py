#working with request library.
import requests

# getting response 200

test_get = requests.get("https://httpbin.org/html")
print(test_get)

test_post = requests.post("https://httpbin.org/post")
print(test_post)

test_put = requests.put("https://httpbin.org/put")
print(test_put)

test_patch = requests.patch("https://httpbin.org/patch")
print(test_patch)

test_delete = requests.delete("https://httpbin.org/delete")
print(test_delete)

test_head = requests.head("https://httpbin.org/", data ={'key':'value'})
print(test_head)
print(test_head.headers)



