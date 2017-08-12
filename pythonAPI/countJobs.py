import jenkins

server = jenkins.Jenkins('http://10.3.15.83/jenkins', username='admin', password='***')
print(server.jobs_count())