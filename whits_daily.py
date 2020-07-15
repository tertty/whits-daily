import requests 
import json 

flavor_master = {
    "flav_ot_day": "NULL",
    "flav_desc": "NULL"
}

response = requests.get("https://www.instagram.com/whitsfordessert/")

if response.ok: 
    html = response.text

    flavor_start_index = html.find('The flavor today')+21
    flavor_end_index = flavor_start_index

    while(html[flavor_end_index] != '!'):
        flavor_end_index += 1

    desc_start_index = flavor_end_index
    desc_end_index = desc_start_index

    while(html[desc_start_index] != 'n'):
        desc_start_index += 1

    while(html[desc_end_index] != '"'):
        desc_end_index += 1

    flavor_master["flav_ot_day"] = html[flavor_start_index:flavor_end_index]
    flavor_master["flav_desc"] = html[desc_start_index+1:desc_end_index]

    print("I see a Whit's", flavor_master["flav_ot_day"], "in your future!")
    print("Description:", flavor_master["flav_desc"])

    json_dump = json.dumps(flavor_master)

    print(json_dump)

    json_dump_file = open("whits_daily.json", "w")
    json_dump_file.write(json_dump)
    json_dump_file.close()
