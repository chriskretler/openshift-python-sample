# for deployments!

bind = '0.0.0.0:8000'
workers = 3

# log to stdout - handy for docker
accesslog = '-'

# log to to stderr - handy for docker
# errorlog = '-'
# loglevel = 'info'

# default accesslog format
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# accesslog format including timing plus request and response headers
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(B)s %(L)s %({Host}i)s %({Content-Type}o)s'

# accesslog simplified format, plus timing.
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(L)s'
