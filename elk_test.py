import logging
import random
import logstash

logging.basicConfig(format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

host = 'localhost'
logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))
logger.error('python-logstash: test logstash error message.')

for i in range(0,5):
    x = random.randint(0,2)
    y = random.randint(3,6)
    if(x==0):
        logger.warning('warning Message {0}'.format(x*y))
    elif(x==1):
        logger.critical('critical Message {0}'.format(x*y))
    else:
        logger.error('error Message {0}'.format(x*y))
