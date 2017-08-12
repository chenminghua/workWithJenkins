import jenkins

server = jenkins.Jenkins('http://10.3.15.83/jenkins', username='admin', password='0816jichusuo')
print(server.jobs_count())