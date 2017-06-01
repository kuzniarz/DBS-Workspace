import csv
import re
from datetime import datetime

input_file = 'american-election-tweets.csv'
output_file = 'aetDATA.csv'
output_file_hashtags = 'aetTAGS.csv'
i = 0

removables =['\n']
def fix_data(tweet):
    for remove in removables:
        hashtag = hashtag.replace(remove, '')
    return tweet
    
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
        d['text'] = removeEmoji(row[1])
        d['hashtags'] = upperfind_hashtags(row[1])
        d['is_retweet'] = str2bool(row[2])
        d['time'] = time2stamp(row[4])
        d['is_quote_status'] = str2bool(row[6])
        d['retweet_count'] = int(row[7])
        d['favorite_count'] = int(row[8])
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
    i = 0
    writer = csv.writer(output, delimiter=';')
    writer.writerow(["ID","value"])
    for element in sorted(hashtags):
        writer.writerow([str(i),element])
        i = i + 1
    
