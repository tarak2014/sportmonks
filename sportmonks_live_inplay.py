import requests
import json
import time
import csv
#from datetime import timedelta, datetime


def get_events_data():
    
    dataform = requests.get('https://soccer.sportmonks.com/api/v2.0/livescores/now?api_token=l8ckspab5WNy2ACGFwyXuBUPtxV8nqAGxshwIeLgndja5AeZibmwsULIMmfx&include=odds,events').json()
    events = []
    #x= r.json()
    data = dataform['data']
    #print(datas)
    for d in data:
        current_id = d['id']
        if(current_id == 11864072):
            json_id = d['events']['data']
            print(json_id)
            for i in json_id:
                print(i)
                event_id = i['id']
                print(event_id)
                event_team_id = i['team_id']
                event_type = i['type']
                event_fixture_id = i['fixture_id']
                event_player_id = i['player_id']
                event_player_name = i['player_name']
                event_related_player_id =  i['related_player_id']
                event_related_player_name = i['related_player_name']
                event_minute = i['minute']
                event_extra_minute = i['extra_minute']
                event_reason = i['reason']
                event_injuried = i['injuried']
                event_result = i['result']
        
                a = [str(event_id),str(event_team_id),str(event_type),str(event_fixture_id),str(event_player_id),str(event_player_name),str(event_related_player_id),str(event_related_player_name),str(event_minute),str(event_extra_minute),str(event_reason),str(event_injuried),str(event_result)]
                if(event_id not in events):
                    events.append(event_id)
                    print(events)
                    with open("test.csv", "a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(a)
                        time.sleep(10)
 
while True:
    get_events_data()
         
