import string

import werkzeug.utils as utils
import boto3
from flask import Flask, render_template, request, url_for

application = Flask(__name__)

@application.route('/')
def index():
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
    #'https://jobmaxresults.s3.amazonaws.com/wordcloud_AWS+developer_2020-11-21.jpg']
    return render_template('index.html', urllist=urllist)


@application.route('/analyze', methods=['POST'])
def analyze():
    job_title = request.form['job_title']
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='JOBMAXSEARCH')
    response = queue.send_message(MessageBody=job_title)

    return utils.redirect(url_for('index'))

application.run()