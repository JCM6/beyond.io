
import json
import requests
import gzip


def getSCRYData():
    url = "https://api.scryfall.com/bulk-data"
    headers = {
        "Content-Type":"application/json; charset=utf-8"
    }
    # Example Data object:
    # data = {
    #   "object": "list",
    #   "has_more": False,
    #   "data": [
    #         {
    #         "object": "bulk_data",
    #         "id": "27bf3214-1271-490b-bdfe-c0be6c23d02e",
    #         "type": "oracle_cards",
    #         "updated_at": "2020-07-02T21:06:38.219+00:00",
    #         "uri": "https://api.scryfall.com/bulk-data/27bf3214-1271-490b-bdfe-c0be6c23d02e",
    #         "name": "Oracle Cards",
    #         "description": "A JSON file containing one Scryfall card object for each Oracle ID on Scryfall. The chosen sets for the cards are an attempt to return the most up-to-date recognizable version of the card.",
    #         "compressed_size": 10530528,
    #         "download_uri": "https://archive.scryfall.com/bulk-data/oracle-cards/oracle-cards-20200702170638.json",
    #         "content_type": "application/json",
    #         "content_encoding": "utf-8"
    #         }
    #     ]
    # }
    
    response = requests.get(url=url, headers=headers)
    print("Get URI Response Status Code: " + str(response.status_code))

    #time to get the daily uri for default cards (english)
    try:
        text = json.loads(response.text)
        uri = text.get("data")
        uri = uri[2]
        uri = uri.get("download_uri")
        print(uri)
    except:
        print("An error occurred when attempting to convert the response into json. Likely an issue with the request status not being 200.")
        print("Response Body: " + str(response.text))

    #Requesting the actual json cards object. This will be big in terms of json, but not as big as all cards.
    dataReq = requests.get(url=uri, headers=headers)
    print("Get Default Card Data Response Status Code: " + str(dataReq.status_code))
    try:
        data = dataReq.content.decode("utf-8")
        saveData = data
        try:
            data = json.loads(data)
        except:
            print("Something went wrong when loading the json object into a python dictionary. The object is likely not a json object.")
    except:
        print("Something went wrong when decoding the received object. Likely the issue is a non 200 response.")
        data = data.content

    #Time to write the data to a file.
    try:
        print("Writing the data to a file.")
        with open("saveData_dailySync.json", "w") as saveData_dailySync:
            saveData_dailySync.write(saveData)
            saveData_dailySync.close()
    except:
        print("An error occurred when writing the json file.")

    return data

def mapTrainingData(data):
    i = 0
    mappedDataObject = {}

    while i < len(data)-1:
        cardObject = data[i]
        oracleText = cardObject.get("oracle_text")
        print(oracleText)

        i += 1

    # Example Object:
    #   {"object":"card",
    #     "id":"7050735c-b232-47a6-a342-01795bfd0d46",
    #     "oracle_id":"0006faf6-7a61-426c-9034-579f2cfcfa83",
    #     "multiverse_ids":[370780],
    #     "mtgo_id":49283,
    #     "mtgo_foil_id":49284,
    #     "tcgplayer_id":69965,
    #     "name":"Sensory Deprivation",
    #     "lang":"en",
    #     "released_at":"2013-07-19",
    #     "uri":"https://api.scryfall.com/cards/7050735c-b232-47a6-a342-01795bfd0d46",
    #     "scryfall_uri":"https://scryfall.com/card/m14/71/sensory-deprivation?utm_source=api",
    #     "layout":"normal",
    #     "highres_image":true,
    #     "image_uris":{"small":"https://img.scryfall.com/cards/small/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795",
    #     "normal":"https://img.scryfall.com/cards/normal/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795",
    #     "large":"https://img.scryfall.com/cards/large/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795",
    #     "png":"https://img.scryfall.com/cards/png/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.png?1562830795",
    #     "art_crop":"https://img.scryfall.com/cards/art_crop/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795",
    #     "border_crop":"https://img.scryfall.com/cards/border_crop/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795"}
    #     ,
    #     "mana_cost":"{U}",
    #     "cmc":1.0,
    #     "type_line":"Enchantment — Aura",
    #     "oracle_text":"Enchant creature\nEnchanted creature gets -3/-0.",
    #     "colors":["U"],
    #     "color_identity":["U"],
    #     "keywords":["Enchant"],
    #     "legalities":{"standard":"not_legal",
    #     "future":"not_legal",
    #     "historic":"not_legal",
    #     "pioneer":"legal",
    #     "modern":"legal",
    #     "legacy":"legal",
    #     "pauper":"legal",
    #     "vintage":"legal",
    #     "penny":"legal",
    #     "commander":"legal",
    #     "brawl":"not_legal",
    #     "duel":"legal",
    #     "oldschool":"not_legal"},
    #     "games":["paper",
    #     "mtgo"],
    #     "reserved":false,
    #     "foil":true,
    #     "nonfoil":true,
    #     "oversized":false,
    #     "promo":false,
    #     "reprint":true,
    #     "variation":false,
    #     "set":"m14",
    #     "set_name":"Magic 2014",
    #     "set_type":"core",
    #     "set_uri":"https://api.scryfall.com/sets/e03ee1c0-ecd2-4fcc-ac3c-e8fdb103a847",
    #     "set_search_uri":"https://api.scryfall.com/cards/search?order=set\u0026q=e%3Am14\u0026unique=prints",
    #     "scryfall_set_uri":"https://scryfall.com/sets/m14?utm_source=api",
    #     "rulings_uri":"https://api.scryfall.com/cards/7050735c-b232-47a6-a342-01795bfd0d46/rulings",
    #     "prints_search_uri":"https://api.scryfall.com/cards/search?order=released\u0026q=oracleid%3A0006faf6-7a61-426c-9034-579f2cfcfa83\u0026unique=prints",
    #     "collector_number":"71",
    #     "digital":false,
    #     "rarity":"common",
    #     "flavor_text":"They call it \"stitcher's anesthesia,\" a spell to deaden the senses while the mad doctors begin their grisly work.",
    #     "card_back_id":"0aeebaf5-8c7d-4636-9e82-8c27447861f7",
    #     "artist":"Steven Belledin",
    #     "artist_ids":["f07d73b9-52a0-4fe5-858b-61f7b42174a5"],
    #     "illustration_id":"3c9e9355-4dcd-411c-b85f-47386e94854b",
    #     "border_color":"black",
    #     "frame":"2003",
    #     "full_art":false,
    #     "textless":false,
    #     "booster":true,
    #     "story_spotlight":false,
    #     "edhrec_rank":18431,
    #     "prices":{"usd":"0.07",
    #     "usd_foil":null,
    #     "eur":"0.01",
    #     "tix":"0.03"},
    #     "related_uris":{"gatherer":"https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=370780",
    #     "tcgplayer_decks":"https://decks.tcgplayer.com/magic/deck/search?contains=Sensory+Deprivation\u0026page=1\u0026utm_campaign=affiliate\u0026utm_medium=api\u0026utm_source=scryfall",
    #     "edhrec":"https://edhrec.com/route/?cc=Sensory+Deprivation",
    #     "mtgtop8":"https://mtgtop8.com/search?MD_check=1\u0026SB_check=1\u0026cards=Sensory+Deprivation"}
    # }
    return mappedDataObject


#write a function that pulls out all of the keys and mapps them into boilerplate logic that I can then refine further.

#getSCRYData()