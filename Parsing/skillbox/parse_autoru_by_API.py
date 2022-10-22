import requests
import pandas as pd
# FrontEnd (в браузере) <= HTTP => Backend (на сервере)
# STATUS CODE (404, 200, 300, 400, 500)
# HEADERS + BODY
# HEADERS = СЛУЖЕБНАЯ ИНФОРМАЦИЯ
# BODY = пользовательская информация
# HTTP METHOD - тип запроса
# GET - получение данных
# POST - обновление данных


# Создаем функцию для HTTP запросов
# Что нужно знать? URL, params={ HEADERS, BODY, METHOD }
def fetch(url, params):
    headers = params['headers']
    body = params['body']
    method = params['method']
    if method == 'GET':
        return requests.get(url, headers=headers)
    if method == 'POST':
        return requests.post(url, headers=headers, data=body)


# Как получить запрос API?
# Перейти по ссылке в гугл хром, нажать f12, нажать на вкладку network, перейти в Fetch/XHR
# Нажать кнопку Показать N предложений на странице сайта
# В веб инспекторе увидим вкладку listing, скопируем ее (правый клик) copy as Node.js

cars = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "181.0.10186714",
    "x-client-date": "1666105589188",
    "x-csrf-token": "f38fd5b38e8990d0b22eda4ea53a2b6265cad4575f44091b",
    "x-page-request-id": "5b748b63f84e2349d22baf203778e359",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/ekaterinburg/cars/toyota/prius/all/",
    "x-yafp": "{\"a1\":\"k50Sxg==;0\",\"a2\":\"fjiD0DfABXvjgLPAUVdm1DhMgCvm2g==;1\",\"a3\":\"l5qhF5PyQMX0A8mx0jNWcQ==;2\",\"a4\":\"lEUyJ2nc/JHJKLrHk+7Nr61KlUB6VpWNmkjVLpOuYzVyYQ==;3\",\"a5\":\"hj6bO/Th+STR0w==;4\",\"a6\":\"UiE=;5\",\"a7\":\"mb61YJzTJYEYlg==;6\",\"a8\":\"oPulSPztot0=;7\",\"a9\":\"b59wUBcWZnN3uA==;8\",\"b1\":\"6T2xcKQ6PW4=;9\",\"b2\":\"TkCyYGgEm8kbTw==;10\",\"b3\":\"W3S9w9utxKS5Jg==;11\",\"b4\":\"GGyvDOVNLdA=;12\",\"b5\":\"1C+E1Gp0EJlgVg==;13\",\"b6\":\"gfHSqDMjL/bBdQ==;14\",\"b7\":\"r2XIofXtR6vxzQ==;15\",\"b8\":\"X+8LXdC9eDbDZg==;16\",\"b9\":\"fOfIjH8T2//kpQ==;17\",\"c1\":\"kLXJ3w==;18\",\"c2\":\"oqVqbTx27FfXTyq+bDK5gg==;19\",\"c3\":\"3spodfrYcUINybbtWhC7CQ==;20\",\"c4\":\"F+yuQLmXUcw=;21\",\"c5\":\"5XcCK7LktN0=;22\",\"c6\":\"JOMQFA==;23\",\"c7\":\"Jd9/Y13FWjo=;24\",\"c8\":\"d8o=;25\",\"c9\":\"znWnC+Bc4xQ=;26\",\"d1\":\"bUuRNlKLFxk=;27\",\"d2\":\"Jxw=;28\",\"d3\":\"iwUSsZvbk9a8HA==;29\",\"d4\":\"jGBfahOalyg=;30\",\"d5\":\"2NQDQQl6qkM=;31\",\"d7\":\"dA/HVykJP58=;32\",\"d8\":\"8LESb+ZncAI0bM9BDsHuauZTZol1liJ6CXI=;33\",\"d9\":\"w9iakWzvVho=;34\",\"e1\":\"x1HVuDy8Lkdd/w==;35\",\"e2\":\"TIu291xZ7Ew=;36\",\"e3\":\"lfUoIVXsI1M=;37\",\"e4\":\"ZaedY+Qyxms=;38\",\"e5\":\"gy3zS1akF0+r7Q==;39\",\"e6\":\"cH4CnRh2r2M=;40\",\"e7\":\"bron+CT+fBi6FA==;41\",\"e8\":\"RyLLs47imW8=;42\",\"e9\":\"KxNuDTBdKAI=;43\",\"f1\":\"CBhVFIBwmNpaew==;44\",\"f2\":\"/rdPRq2GBzU=;45\",\"f3\":\"bwpNG7DhUVEEnQ==;46\",\"f4\":\"pgzD12gXcjI=;47\",\"f5\":\"w0HvDhKMMeQLrw==;48\",\"f6\":\"f0KTMJzGMuDuBA==;49\",\"f7\":\"AHe/L3MChy+tww==;50\",\"f8\":\"jRNM5Ix0ebcMuQ==;51\",\"f9\":\"m1U/pSivFvM=;52\",\"g1\":\"+Aep/BIpNpn9Gg==;53\",\"g2\":\"LINDaOeBEVVkRw==;54\",\"g3\":\"05IgEHVKQn0=;55\",\"g4\":\"s1U5pgTX+NgGJA==;56\",\"g5\":\"VwQZQ8hdWUE=;57\",\"g6\":\"dI9fifqOOaA=;58\",\"g7\":\"JzbWhr4+DeM=;59\",\"g8\":\"P3FffzvdY3w=;60\",\"g9\":\"f2qgCFUpAD8=;61\",\"h1\":\"xLx+YnM/5KfIVw==;62\",\"h2\":\"sbEB9xaox/lZkw==;63\",\"h3\":\"4sTr3Q2yOHgQsw==;64\",\"h4\":\"HYpRnYkjR7WwBQ==;65\",\"h5\":\"tCx9Yf99waQ=;66\",\"h6\":\"rAZD2yxdEqei9w==;67\",\"h7\":\"sAOYRyE+iWjX1tFaHz4OX9hrdFgf7oNU+a4mk986nnBrnack;68\",\"h8\":\"aCmf67fyI7P64A==;69\",\"h9\":\"rvD/ZRE/Stj+mA==;70\",\"i1\":\"6wEZ0yR/ieU=;71\",\"i2\":\"aP3CNgmna3oKNw==;72\",\"i3\":\"9sEBGephYRXfMg==;73\",\"i4\":\"SKd/puDeeTBA9Q==;74\",\"i5\":\"tz3e5aJacNaKhQ==;75\",\"z1\":\"HuagcV1PHUhCvo4XKHIUcMFiYEB2HLkcXcXD3jQmRHtUuphvQnUDYkT/05Z64XSpEB14wh91VRNSfKsf4agOZw==;76\",\"z2\":\"Q4+MgjvonhwBc1Sck5TXzFI6g2F2QMWykBd83mRXo5VSR7Yx9pSVQfM7BxrUfx0V+AiGEy4P37fyJ14Ca94BJQ==;77\",\"y2\":\"cDaPm44Dhou/zg==;78\",\"y3\":\"NMuMa7rmCtwygA==;79\",\"y6\":\"LAS6r75Sr32/GQ==;80\",\"y8\":\"NC9bRbrF/oyDmw==;81\",\"x4\":\"CLNn26owDNWzTg==;82\",\"z5\":\"2gSrXBIB/sw=;83\",\"z4\":\"nOaQsgd3xSCPQQ==;84\",\"z6\":\"VrNM4wibfm7LKGbh;85\",\"z7\":\"oyvVIwMa+Hy3nGWi;86\",\"z8\":\"w/HxLOuJXAL5F+iQzv4=;87\",\"z9\":\"PIEhkcnfXeZyFADQ;88\",\"y1\":\"oaj3bJRnsIFyOCKJ;89\",\"y4\":\"x7xBOROA4G2+FEkI;90\",\"y5\":\"/Qn2u2WAjvEbYKaCS3Q=;91\",\"y7\":\"ZhCvsxknzPF0S/Uo;92\",\"y9\":\"N82jZzMKEE7KQEJPVmQ=;93\",\"y10\":\"ZfDn3v2LWqjRsiUGTVQ=;94\",\"x1\":\"MZwgjZhNJ519jAU6;95\",\"x2\":\"fi++guvyRJKbQfzTAZ8=;96\",\"x3\":\"0BERXkTgFO3l7VtG;97\",\"x5\":\"676L4pWZvFxZjDll;98\",\"z3\":\"9flxkhIUI5+8IKtMjnR34TEOPdKFWNx/Bk4Q8ANXqyY=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"CGvwa8LJcsKMr53VT4kosc/60Wg=;100\",\"pgrd\":\"OjlIpQGIq3z43cjk31zxFi8x+7mssXgFkOu4x1G8G4gj4Z82/m+irDaqflIAU4I9HVqMaf1Rs0abxyGtpJhQeZZ7wqf1sSInfq3PtQNA21P7aB6k2qrD1om1SdIR3G+lFaB6g040alR6HFjyRqcU+xLzPa0elvwHxObBPuIe66VdmX6b+uA1TcaItPPSjGWySXVC8skoyTTqoZFs3N8MuYYOZb4=\"}",
    "cookie": "suid=ce067da86713991be82e468cb51d5105.281353b2681ec23146fc61510d01a57e; _csrf_token=f38fd5b38e8990d0b22eda4ea53a2b6265cad4575f44091b; autoru_sid=a%3Ag634ec0ac2b4dksg88no9euujc7iatjb.b4a15d6e78055801c3e0ca05c4dd2c54%7C1666105516009.604800.xsz_0IAbPnIsedHYLCMKDA.alqsSHdDok7kmDYlDPMvyxx9hnvpVDyU2dduYwQ7aKI; autoruuid=g634ec0ac2b4dksg88no9euujc7iatjb.b4a15d6e78055801c3e0ca05c4dd2c54; from=direct; yuidlt=1; yandexuid=8026589671661940989; gdpr=0; _ym_uid=1666105519840254640; _ym_visorc=b; _ym_isad=1; spravka=dD0xNjY2MTA1NTI5O2k9OTIuMjQ4LjIzMC41NTtEPUU3RkYwQTcxOTk5QTA5NUYzOTU5MkFDQ0M3NEQwNzlFRTUyNjQ4MDBCMjQwNkU3RTU0REY4MjdBQjY3QjNGQkM4ODdGNEE0MTt1PTE2NjYxMDU1Mjk1MjU3NTAwMTU7aD0yNDA1MGJiNTkxM2EyNmNmNGU3OWE3YWVkNTA0OTE3ZQ==; crookie=rHFlXhRhrU9Nzg2A2+b6gDsbKuQr1qs+ZLwBsbHarGuyrlzrM8vvPb19drgDLqGu/JJN/hM+pO3rm+4Gl23tssY9NzA=; cmtchd=MTY2NjEwNTUzMjUxNA==; Session_id=noauth:1666105531; yandex_login=; ys=c_chck.2140123137; i=aX3xdEmWmbhVAHGVlPOGxZa9r0Zv4aR+WwgqmdRxwK/6LRTDevLpEjJ6RhEzV5eJqVvrm0JD1F9SkdISBxFyKdkDFkI=; mda2_beacon=1666105531684; sso_status=sso.passport.yandex.ru:synchronized; _yasc=txN5mvCGIfSFDESp7S/RJGCoYP0vPnQ2RKi9P6G77hp5/nAUnrzM5+gKTCJ1bGU=; from_lifetime=1666105552054; _ym_d=1666105555; layout-config={\"win_width\":964.7999877929688,\"win_height\":696.7999877929688}",
    "Referer": "https://auto.ru/ekaterinburg/cars/toyota/prius/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"TOYOTA\",\"model\":\"PRIUS\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_radius\":200,\"geo_id\":[54]}",
  "method": "POST"
})

# Заголовки
print(cars.headers)

# Выведем инфу о машинах
offers = cars.json()['offers']
for offer in offers:
    price = offer["price_info"]["USD"]
    name = offer["vehicle_info"]["model_info"]["name"]
    mileage = offer["state"]["mileage"]
    print(f"Найден {name} всего за ${price}, пробег всего {mileage} км")

# проанализируем распределение цен
fig = pd.Series([offer["price_info"]["USD"] for offer in offers]).hist()
fig.figure.savefig('fig.png')

