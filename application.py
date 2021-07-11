#import boto3
from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    #s3 = boto3.resource('s3')
    #my_bucket = s3.Bucket('jobmaxresults/')
    #urllist = my_bucket.objects.all()
    urllist = ['https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg',
               'https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg']
    return render_template('index.html', urllist=urllist)