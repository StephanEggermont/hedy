# This file is used to configure gunicorn,
# used on Heroku.

def worker_exit(server, worker):
    # When the worker is being exited (perhaps because of a timeout),
    # give the query_log handler a chance to flush to disk.
    import querylog
    querylog.emergency_shutdown()