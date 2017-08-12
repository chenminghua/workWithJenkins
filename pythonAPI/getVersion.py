import jenkins

server = jenkins.Jenkins('http://10.3.15.83/jenkins', username='admin', password='0816jichusuo')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))