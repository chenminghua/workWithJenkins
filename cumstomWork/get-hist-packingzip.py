# Author:chenminghuaht@foxmail.com
# Version:1.0
# usage: python2.X ${JOB_NAME}

import os,sys
import os.path
import urllib
import urllib2
import json

job_name = sys.argv[1]

def getJobJson(job_name):
    job_url = "http://10.3.15.83/jenkins/job/%s/api/python?pretty=true" % (job_name)
    try:
        print "the job url is :" + job_url
        data = urllib2.urlopen(job_url).read()
        data = data.replace('None', '0').replace('True', '1').replace('False', '0')
        return data
    except Exception,e:
        print e

def getBuildJson(buildNumber):
    build_url = "http://10.3.15.83/jenkins/job/%s/%s/api/python?pretty=true" % (job_name, buildNumber)
    print "build url is:" + build_url
    try:
        data = urllib2.urlopen(build_url).read()
        data = data.replace('None', '0').replace('True', '1').replace('False', '0')
        return data
    except Exception,e:
        print e


def saveFile(fileUrl, fileName):
    print "will save file " + fileUrl
    status = urllib.urlopen(fileUrl).code
    if (status != 404):
        urllib.urlretrieve(fileUrl, fileName)
    else:
        print "the build has no currentapkinfos.xml"


if __name__ == '__main__':
    data = getJobJson(job_name)
    value = json.loads(data)
    for build in value["builds"]:
        buildUrl=build["url"]
        buildNumber=str(build["number"])
        buildJson = json.loads(getBuildJson(buildNumber))
        url = buildJson["url"]
        for arti in buildJson["artifacts"]:
            fileName = str(arti['fileName'])
            print "file name is:" + fileName
            if(fileName.startswith('packing_zip')):
                packingzipurl=url + "artifact/" + arti["relativePath"]
                print packingzipurl
                saveFile(str(packingzipurl), fileName)