import requests


payload = {}
headers = {
  'authority': 'api2.bybit.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'ru,en;q=0.9',
  'guid': 'b2a6f601-3980-aaff-2ef6-1dfed4a9600f',
  'origin': 'https://www.bybit.com',
  'referer': 'https://www.bybit.com/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'traceparent': '00-a368cef585c4de611737a36b5f3cdaab-b4cad24ea9b1c543-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
  'Cookie': '_abck=44F597239F09CEE88E32C516380C01F1~-1~YAAQHwxAFw5dd8KNAQAAR+ZEygtk+kaVY8ERys/6kBFhoKa4M2fcyISmkExn3i9Fk4GsGrSZUY7oho4beaaWwBUX0chbAhTQL4+Mf74EgJb/FjRfx3Ji9t2I98a0a87VxdTYud4OzL2KiVOrvQ6fH7TQ2B6JM18Z4PzU53vzjKFbR+pzaRxRDSM1cQW9z1N3PuVr2onR8ckEpt9OLg+JPgSZqkJFVh1wwab8K08ooo0966CNN3gxn+FP0/gWaoDdftCkfVlt+BCu7vV2oUWy2UaTqGigiSS95ENJqEzn5balvRnWlxhwPt7Y9sJ13/Q8Y+034xFQdMh+Pt0Yq8a4ODS9TL725ZK2SkRw0Anw7SGfDVRNhqf9h9KbEqihBlZnFbfq02bsv3WFJV6DR0GfPk9yMN/XH2Q=~0~-1~-1; ak_bmsc=2D8FA907B2F31E0EDA03331D3350CAE3~000000000000000000000000000000~YAAQHwxAFziNd8KNAQAAK11HyhYatT9srcmLDa6/yX3nMZNm+Q9W/uDbPZJI+sIOZX7MzifHRE+StBLkxLBW1lCIgpv8GoQs4m4KCNVYFwCAzJ8hktTAgTkox9kPLj0pPT6fuaNbimno3il5QUVJW24AkMqsmRMeh/JDq4JeNhlHKz88UEg/fuFNn0kATjq554yYWrBNXKcWjyKl5FiHntBuHXfG3WgBQRgzi3TgshShCxNATveUbNbqe9m4RvYs+gLNI0vooG7afPxpO/1j8UPH1vliF///2M15wuNSUdt0ii/0gjBNhmpFdv65v3fcxpUJcMkO+1yIAYwqn6FU4U/BlibpvRe6y5efnXqHPvwDBl5ZkHcfC9dV; bm_sv=F455BD6C3CD2D24EC3DB64709E0BB4CC~YAAQHwxAFw9dd8KNAQAAR+ZEyhaunTc8hwF0lzPi5QgPUAN+YhDG9tDevH/oEdpZkg3xDf/qOvm5TJphzulnd9yE5xnG0GaNnbWbvj0TjNt59quHc+nYnNlOs4DryeQoyH6dA/VoEGM33OtR7SDY9jhIu/aDr5UA30urz4vm4Fx7d7OuhEmzS+tB5kqz7Oc2obzf2nuTpM2eYih2aoDgGGhLjtqusCtge7NZ8d6tKfK7JO+22qMNWXtvVJcygdDu~1; bm_sz=388033FE235865F384FB532B835503FC~YAAQHwxAFzmNd8KNAQAAK11HyhYp+FfSK/0IxIpMcArwlUtUKv3wbJfO7FdkY/S4DxYsF43dlDwcJyM/JIPf6xciMb1/B0+2qo1EkJ/UmdCp+IOWsCOs/9bwpCMo+2gUC8FRgle6Ljj7DCX+Lh46sWX6meV4/VSrqXN6sK2Ke6BHD/sSe6IVDSzH6Thr6ff8zD6PqdK0CNSQYrxeIooN4AZz9+gzGe34/7OcrLSP+Qj0NxVeyi1o7oGxKJiteAsfYcPoim7ps2MVHFnrGNVxCcjCnKvfcU6UvfxotqmTPpm1NLt9Gdr/KkIPmjz7oZHG6/NgFu4dSUE+XRMt~4272451~3617857'
}

urls=[]

with open('bybit_urls.txt', 'r', encoding='utf-8') as file:
  for url in file:
    urls.append(url.replace('\n',''))


for url in urls:
  response = requests.request("GET", url, headers=headers, data=payload).json()
  pairs_list=list(response['result'])
  for pair in pairs_list:
    if not pair.endswith('T'):
      continue
    spot=response['result'][pair][-1]
    result = f"{pair} - {spot['c']}"
    print(result)