import requests


se = requests.session()
se.cookies.update({'visit-month':'February'})

res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2022'})
print(res.text)

#Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r= requests.post(url,files=files)
print(r.status_code)
print(r.text)








