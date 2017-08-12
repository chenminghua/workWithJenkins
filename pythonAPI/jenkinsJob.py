import jenkins

server = jenkins.Jenkins('http://10.3.15.83/jenkins', username='admin', password='***')

#print all jobs json data
jobs = server.get_jobs()
print(jobs)

my_job = server.get_job_config('5507-Hotel_Manual')
print(my_job)

my_nodes = server.get_nodes()
print(my_nodes)
