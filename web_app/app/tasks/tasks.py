from app import celery, db, Money


def add_sync(x, y):
    import time
    time.sleep(1)
    result = x+y
    db.session.add(Money(money=result, api='sync'))
    db.session.commit()

@celery.task()
def add_async(x, y):
    import time
    time.sleep(1)
    result = x+y
    db.session.add(Money(money=result, api='async'))
    db.session.commit()


@celery.task()
def mul(x, y):
    return x * y


@celery.task()
def xsum(numbers):
    return sum(numbers)
