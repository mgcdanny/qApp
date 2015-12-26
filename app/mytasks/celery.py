from celery import Celery

# Docker sets rmq to etc/hosts file via the command --link rmq_c:rmq
app = Celery('mytasks', broker='amqp://rmq', backend='rpc://', include=['mytasks.tasks'])
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
    CELERY_IGNORE_RESULT=False
)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
