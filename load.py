import praw
import re
import os.path
import configparser
config = configparser.ConfigParser()

import sys

if (len(sys.argv)<2):
    exit('Erro: precisa informar o nome do usuario')

#import pdb;pdb.set_trace()

config.read('config.ini')




reddit = praw.Reddit(client_id=config['LOAD']['ClientID'],
                     client_secret=config['LOAD']['ClientSecret'],
                     user_agent=config['LOAD']['UserAgent'])

user_name = sys.argv[1]


comments = []
#import pdb;pdb.set_trace()
i=0
for comment in reddit.redditor(user_name).comments.new(limit=None):
    i=i+1
    comments.append(comment.body)
    #print(comment.body)

print(i)
texto = " ".join(comments)
texto = re.sub(r'http\S+', '', texto)
texto = texto.replace('&nbsp;','')
texto = texto.replace('&ndash;','')
texto = texto.replace('&mdash;','')

f = open(os.path.join('data', user_name),'w')
f.write(texto)