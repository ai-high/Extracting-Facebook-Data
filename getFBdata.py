import requests
import datetime
import pandas as pd
import json

FREEGEOPIP_URL = 'http://api.ipstack.com'
key = 'cd111cd2de8b56abbf2d1be357f8543c'

def get_geolocation_for_ip(ip):
    url = '{}/{}?access_key={}'.format(FREEGEOPIP_URL, ip,key)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

#print(get_geolocation_for_ip(ip)['region_name'])


def time(stamp):
    return datetime.datetime.fromtimestamp(
        int(stamp)
    ).strftime('%Y-%m-%d %H:%M:%S')

#print(time(1538553409))
    
columns = ['Time','Type','Author','Content','Group','otherPerson','Latitude','Longitude','City','State','Country']

"""
table = []
i = 0
activities = json.load(open('USEFUL/security_and_login_information/account_activity.json'))

for a in activities['account_activity']:
    loc = get_geolocation_for_ip(a['ip_address'])
    hold = []
    hold.append(loc['latitude'])
    hold.append(loc['longitude'])
    hold.append(time(a['timestamp']))
    print(str(i)+" / "+ str(len(activities['account_activity'])))
    i+=1
   
    
df = pd.DataFrame(table)
df = df.transpose()
df.columns = ['Latitude', 'Longitude','Date/Time']
    

df.to_csv('firstgo.csv', sep='\t')

ips_saved = json.load(open('USEFUL/security_and_login_information/used_ip_addresses.json'))
i= 0
for a in ips_saved['used_ip_address']:
    loc = get_geolocation_for_ip(a['ip'])
    lat.append(loc['latitude'])
    long.append(loc['longitude'])
    print(str(i)+" / "+ str(len(ips_saved['used_ip_address'])))
    i+=1
    
table = [lat,long]
df = pd.DataFrame(table)
df = df.transpose()
df.columns = ['Latitude', 'Longitude']
    

df.to_csv('secondgo.csv', sep='\t')
"""

csv_array = []


comments = json.load(open('USEFUL/comments.json'))


for a in comments['comments']:
    tmp = []
    tmp.append(time(a['data'][0]['comment']['timestamp']))
    print(time(a['data'][0]['comment']['timestamp']))
    tmp.append('Comment')
    tmp.append(a['data'][0]['comment']['author'])
    if 'comment' in a['data'][0]['comment']:
        tmp.append(a['data'][0]['comment']['comment'])
    else:
        tmp.append("NULL")
    if 'group' in a['data'][0]['comment']:
        tmp.append(a['data'][0]['comment']['group'])
    else:
        tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('1.csv', sep='\t')


comments = json.load(open('USEFUL/event_invitations.json'))


for a in comments['events_invited']:
    tmp = []
    tmp.append(time(a['start_timestamp']))
    print(time(a['start_timestamp']))
    tmp.append('Event Invitation')
    tmp.append("NULL")
    if 'name' in a:
        tmp.append(a['name'])
    else:
        tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)


df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('2.csv', sep='\t')


comments = json.load(open("USEFUL/other_people's_posts_to_your_timeline.json"))


for a in comments['wall_posts_sent_to_you']:
    tmp = []
    tmp.append(time(a['timestamp']))
    print(time(a['timestamp']))
    tmp.append('Wall Post Recived')
    tmpString = a['title'].split()
    tmp.append(tmpString[0]+" "+tmpString[1])
    if 'data' in a:
        if 'post' in a['data'][0]:
            tmp.append(a['data'][0]['post'])
        else:
            tmp.append("NULL")
    else:
        tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('3.csv', sep='\t')



comments = json.load(open('USEFUL/posts_and_comments.json'))

for a in comments['reactions']:
    tmp = []
    tmp.append(time(a['timestamp']))
    print(time(a['timestamp']))
    tmp.append('Reaction')
    tmp.append(a['data'][0]['reaction']['actor'])
    tmp.append(a['data'][0]['reaction']['reaction'])
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)


df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('4.csv', sep='\t')



comments = json.load(open('USEFUL/your_event_responses.json'))



for a in comments['event_responses']['events_joined']:
    tmp = []
    tmp.append(time(a['start_timestamp']))
    print(time(a['start_timestamp']))
    tmp.append('Event Response')
    tmp.append('Zac Moran')
    tmp.append('Event Joined')
    tmp.append(a['name'])
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('5.csv', sep='\t')

for a in comments['event_responses']['events_declined']:
    tmp = []
    tmp.append(time(a['start_timestamp']))
    print(time(a['start_timestamp']))
    tmp.append('Event Response')
    tmp.append('Zac Moran')
    tmp.append('Event Declined')
    tmp.append(a['name'])
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('6.csv', sep='\t')

for a in comments['event_responses']['events_interested']:
    tmp = []
    tmp.append(time(a['start_timestamp']))
    print(time(a['start_timestamp']))
    tmp.append('Event Response')
    tmp.append('Zac Moran')
    tmp.append('Event Interested')
    tmp.append(a['name'])
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('7.csv', sep='\t')



comments = json.load(open('USEFUL/your_posts.json'))

for a in comments['status_updates']:
    tmp = []
    tmp.append(time(a['timestamp']))
    print(time(a['timestamp']))
    tmp.append("Post")
    tmp.append("Zac Moran")
    try:
        tmp.append(a['data'][0]['post'])
    except:
        tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('8.csv', sep='\t')


comments = json.load(open('USEFUL/your_posts_and_comments_in_groups.json'))
c = 0

for a in comments['group_posts']:
    try:
        tmp = []
        tmp.append(time(a['timestamp']))
        print(time(a['timestamp']))
        if 'post' in a['data'][0]:
            tmp.append("Post")
        elif 'comment' in a['data'][0]:
            tmp.append("Comment")
        else:
            tmp.append("NULL")
            
        tmp.append("Zac Moran")
        
        if 'post' in a['data'][0]:
            tmp.append(a['data'][0]['post'])
        elif 'comment' in a['data'][0]:
            try:
                tmp.append(a['data'][0]['comment']['comment'])
            except:
                tmp.append("NULL")
        else:
            tmp.append("NULL")
    
        if 'comment' in a['data'][0]:
            tmp.append(a['data'][0]['comment']['group'])
        else:
            tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        csv_array.append(tmp)
    except:
        print("WHoops")
    c+=1

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('9.csv', sep='\t')



comments = json.load(open('USEFUL/your_search_history.json'))
        
    
for a in comments['searches']:
    tmp = []
    tmp.append(time(a['timestamp']))
    print(time(a['timestamp']))
    tmp.append('Search')
    tmp.append('Zac Moran')
    tmp.append(a['data'][0]['text'])
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    tmp.append("NULL")
    csv_array.append(tmp)

df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('10.csv', sep='\t')


activities = json.load(open('USEFUL/security_and_login_information/login_protection_data.json'))

for a in activities['login_protection_data']:
    if 'ip_address' in a['session']:
        tmp = []
        tmp.append(time(a['session']['created_timestamp']))
        tmp.append("Location")
        tmp.append("NULL")
        tmp.append(a['session']['ip_address'])
        tmp.append("NULL")
        tmp.append("NULL")
        loc = get_geolocation_for_ip(a['session']['ip_address'])
        print("Getting Location....")
        tmp.append(loc['latitude'])
        tmp.append(loc['longitude'])
        tmp.append(loc['city'])
        tmp.append(loc['region_name'])
        tmp.append(loc['country_name'])
        csv_array.append(tmp)
        
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('11.csv', sep='\t')  




activities = json.load(open('USEFUL/security_and_login_information/logins_and_logouts.json'))

for a in activities['account_accesses']:
    tmp = []
    tmp.append(time(a['timestamp']))
    tmp.append("Location")
    tmp.append("NULL")
    tmp.append(a['ip_address'])
    tmp.append("NULL")
    tmp.append("NULL")
    loc = get_geolocation_for_ip(a['ip_address'])
    print("Getting Location....")
    tmp.append(loc['latitude'])
    tmp.append(loc['longitude'])
    tmp.append(loc['city'])
    tmp.append(loc['region_name'])
    tmp.append(loc['country_name'])
    csv_array.append(tmp)
        
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('12.csv', sep='\t')  



activities = json.load(open('USEFUL/security_and_login_information/used_ip_addresses.json'))

for a in activities['used_ip_address']:
    tmp = []
    tmp.append("NULL")
    tmp.append("Location")
    tmp.append("NULL")
    tmp.append(a['ip'])
    tmp.append("NULL")
    tmp.append("NULL")
    loc = get_geolocation_for_ip(a['ip'])
    print("Getting Location....")
    tmp.append(loc['latitude'])
    tmp.append(loc['longitude'])
    tmp.append(loc['city'])
    tmp.append(loc['region_name'])
    tmp.append(loc['country_name'])
    csv_array.append(tmp)
        
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('13.csv', sep='\t')


activities = json.load(open("USEFUL/security_and_login_information/where_you're_logged_in.json"))

for a in activities['active_sessions']:
    tmp = []
    tmp.append(time(a['created_timestamp']))
    tmp.append("Location")
    tmp.append("NULL")
    tmp.append(a['ip_address'])
    tmp.append("NULL")
    tmp.append("NULL")
    loc = get_geolocation_for_ip(a['ip_address'])
    print("Getting Location....")
    tmp.append(loc['latitude'])
    tmp.append(loc['longitude'])
    tmp.append(loc['city'])
    tmp.append(loc['region_name'])
    tmp.append(loc['country_name'])
    csv_array.append(tmp)
        
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('14.csv', sep='\t')
        

activities = json.load(open('USEFUL/security_and_login_information/account_activity.json'))
i = 0
for a in activities['account_activity']:
    tmp = []
    tmp.append(time(a['timestamp']))
    tmp.append("Location")
    tmp.append("NULL")
    tmp.append(a['ip_address'])
    tmp.append("NULL")
    tmp.append("NULL")
    loc = get_geolocation_for_ip(a['ip_address'])
    print("Getting Location....")
    tmp.append(loc['latitude'])
    tmp.append(loc['longitude'])
    tmp.append(loc['city'])
    tmp.append(loc['region_name'])
    tmp.append(loc['country_name'])
    csv_array.append(tmp)
    print(str(i)+" / "+ str(len(activities['account_activity'])))
    i+=1
    
    
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('Final.csv', sep='\t')






























