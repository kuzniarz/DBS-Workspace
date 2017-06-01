import csv
import re
from datetime import datetime

#Speicher mit denen gearbeitet wird
input_file = 'american-election-tweets.csv'
output_file = 'aetDATA.csv'
output_file_hashtags = 'aetTAGS.csv'
i = 0

#Hilfsfunktionen fuer die Verarbeitung der Daten
    
def str2bool(string):
    return string == 'True'
    
def upperfind_hashtags(tweet):
    tweet.replace("# ", '#')
    tags = re.findall(r"#(\w+)", tweet)
    return [tag.upper() for tag in tags]
    
def time2stamp(string):
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')
    
def removeEmoji(string):
    string.encode('UTF-8', errors='ignore')
    return string.replace("b'",'')

data=[]
with open(input_file, "r", errors='ignore') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader) # skip the header
    for row in reader:
        # Format the data and put everything in a nice-looking JSON format
        d = dict()
        d['1_id'] = i
        d['2_handle'] = row[0]
        d['3_is_retweet'] = str2bool(row[2])
        d['4_time'] = time2stamp(row[4])
        d['5_is_quote_status'] = str2bool(row[6])
        d['6_retweet_count'] = int(row[7])
        d['7_favorite_count'] = int(row[8])
        d['8_text'] = removeEmoji(row[1])
        d['9_hashtags'] = upperfind_hashtags(row[1])
        i = i + 1
        data.append(d)

with open(output_file, "w") as output:
    writer = csv.DictWriter(output, fieldnames=d.keys(), delimiter=';')
    writer.writeheader()
    for line in data:
        writer.writerow(line)
    
#print(data)

#make hashtags set
hashtags = set()
for tweet in data:
    for h in tweet['hashtags']:
        hashtags.add(h)
        
with open(output_file_hashtags, "w") as output:
    writer = csv.writer(output, delimiter=';')
    writer.writerow(["value","total_count"])
    for element in sorted(hashtags):
        i=0
        for tweet in data:
            for l in tweet['hashtags']:
                if element==l:
                    i = i + 1
        writer.writerow([element,str(i)])
    
