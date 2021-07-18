import string

import boto3
from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('jobmaxresults')
    #obj_list = s3.list_objects_v2(Bucket=my_bucket)
    #objlist = my_bucket.objects.all()
    objlist = map(lambda x: (x.bucket_name, x.key), my_bucket.objects.all())
    urllist = [('https://jobmaxresults.s3.amazonaws.com/' + j.replace(' ', '+'), j.replace('.jpg','')) for i, j in objlist]
    #keylist = [j.replace(' ', '+') for i, j in objlist]

    #bucket, keylist = objlist
    #keylist = my_bucket.objects.all().keys()
    #urllist = ['https://jobmaxresults.s3.amazonaws.com/' + key['Key'] for key in urllist]
    #urllist = ['https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg',
    #           'https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg']
    return render_template('index.html', urllist=urllist)

application.run()