import csv
import re
import collections
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
        d['id'] = i
        d['handle'] = row[0]
        d['is_retweet'] = str2bool(row[2])
        d['time'] = time2stamp(row[4])
        d['is_quote_status'] = str2bool(row[6])
        d['retweet_count'] = int(row[7])
        d['favorite_count'] = int(row[8])
        d['text'] = removeEmoji(row[1])
        d['hashtags'] = upperfind_hashtags(row[1])
        od = collections.OrderedDict(sorted(d.items()))
        i = i + 1
        data.append(od)

fnames = ['id', 'handle', 'is_retweet', 'time', 'is_quote_status', 'retweet_count', 'favorite_count', 'text']

with open(output_file, "w") as output:
    writer = csv.DictWriter(output, fieldnames=fnames, delimiter=';', extrasaction='ignore')
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
    
