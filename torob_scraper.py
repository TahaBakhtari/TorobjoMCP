import json
import requests

input_query = input("product : ")

def get_data(page_url):
	data = []
	response = requests.get(page_url)
	results = response.json()["results"]
	for post in results:
		name = post["name1"]
		price =  post["price"]
		url = "https://torob.com" +post["web_client_absolute_url"]

		if price != 0 :
			data.append({"title": name, "price": price, "url": url})

			if len(data) >= 10:
				return data
		
	next_page = response.json()["next"]
	while next_page and len(data) < 10:
		
		response = requests.get(next_page)
		results = response.json()["results"]
		
		for post in results:
			name = post["name1"]
			price =  post["price"]
			url = "https://torob.com" +post["web_client_absolute_url"]
			
			if price != 0 :
				data.append({"title": name, "price": price, "url": url})
				if len(data) >= 10:
					return data
		
		next_page = response.json()["next"]
		print(len(data))
			
	return data

url = f"https://api.torob.com/v4/base-product/search/?page=0&sort=popularity&size=24&query={input_query}&q={input_query}&source=next_desktop"

full_data = get_data(url)
if full_data :
	with open(f"{input_query}.json", "w", encoding="UTF-8") as file:
		json.dump(full_data, file, ensure_ascii=False, indent=4)
	
	# Display the JSON output in the console
	print(json.dumps(full_data, ensure_ascii=False, indent=4))
else:
	print("nothing")