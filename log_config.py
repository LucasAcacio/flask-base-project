import logging, logstash
    
def setup_logstash_log(app):
    app.logger.addHandler(logstash.TCPLogstashHandler(host="localhost", port=9999, version=1, message_type="json"))
    log_data = {
        "app": "myflask"
    }
    app.logger = logging.LoggerAdapter(app.logger, log_data)