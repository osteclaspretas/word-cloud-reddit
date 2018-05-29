import praw
import re
import os.path


reddit = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='testscript by /u/username')

user_name = "felipeko"


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