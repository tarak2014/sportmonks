import requests
import codecs, json
import time
import csv
#from datetime import timedelta, datetime



r = requests.get('https://soccer.sportmonks.com/api/v2.0/fixtures/11867274?api_token=l8ckspab5WNy2ACGFwyXuBUPtxV8nqAGxshwIeLgndja5AeZibmwsULIMmfx&include=events')
flag = []
x= r.json()
data = x['data']
json_id = data['events']['data']
for i in json_id:
    event_id = i['id']
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
    
    a = str(event_id),str(event_team_id),str(event_type),str(event_fixture_id),str(event_player_id),str(event_player_name),str(event_related_player_id),str(event_related_player_name),str(event_minute),str(event_extra_minute),str(event_reason),str(event_injuried),str(event_result)
    if(event_id not in flag):
        flag.append(event_id)
        print(flag)
        with open("test.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(a)
            

    
        
        

        

        
        
        
        
        
            

        

 
        


