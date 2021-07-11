import boto3
from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('jobmaxresults')
    #obj_list = s3.list_objects_v2(Bucket=my_bucket)
    urllist = my_bucket.objects.all()
    #keylist = my_bucket.objects.all().keys()
    #urllist = ['https://jobmaxresults.s3.amazonaws.com/' + key['Key'] for key in urllist]
    #urllist = ['https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg',
    #           'https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg']
    return render_template('index.html', urllist=urllist)

