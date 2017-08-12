#!/usr/bin/python
# -*- FileName:makeOtaPatch.py -*-
# Execute: python makeOtaPatch.py ${MP_BUILD_NAME}
# author:cmh

##############################################################
#完成ota制作前的各版本的packing.zip文件以及工具文件的准备工作#
##############################################################
import os, sys, stat
import shutil
#define some variable for the script
#these variable will be changed in deifferent jenkins-job
mp_build_name = sys.argv[1]
mp_workspace = '/home/jenkins/.jenkins/jobs/' + mp_build_name + '/builds/'
tool_path = '/home/jenkins/tools/otazip'
packing_zip_path = os.getcwd() + '/release/otazip/zip/'
#job_name=sys.argv[1]
mp_upload_home = '/home/ftp/data/otapacking/' + mp_build_name + '_ota/ota-related/android'

print os.getcwd()
#step1:copy ftp files to workspace
print '########################################'
print 'start to copy mp build files to workspace'
shutil.copytree(mp_upload_home,os.getcwd() + '/release/android/')

#step2:copy tools to workspace
print '#######################################'
print 'start to copy tools to workspace'
shutil.copytree(tool_path,os.getcwd()+'/release/otazip')

#step3:copy packing.zip to specific dir
print '######################################'
print 'start to copy packing.zip to specific dir'
hisbuilds = os.listdir(mp_workspace)
for build in hisbuilds:
    if build.isdigit():
        zipFilePath = mp_workspace + build + '/archive/release/otazip/zip'
        files = os.listdir(zipFilePath)
        for zipFile in files:
            filePath = os.path.join(zipFilePath, zipFile)
            if os.path.isfile(filePath):
                print 'will copy file ' + filePath + ' to  ' + packing_zip_path
                shutil.copyfile(filePath, packing_zip_path + '/' + zipFile)

#step4:start to call makepatch.py
print '#####################################'
print 'start to call makepatch.py'


