def testException(a):
    try:
        print('try...')
        r = 10 / a
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')

# testException(0)
# testException(3)



def tryError(a):
    try:
        print('try...')
        r = 10/int(a)
        print('print %s' % r)
    except ZeroDivisionError as e:
        print('ZeroDivisionError except:',e)
    except ValueError as e:
        print('ValueError except:',e)
    else:
        print('no error')
    finally:
        print('finally...')
    print('end')

# tryError('')
# tryError(0)
# tryError('121')
# tryError(2)

import logging

def loggingError(a):
    try:
        print('try...')
        r = 10/int(a)
        print('print %s' % r)
    except ZeroDivisionError as e:
        logging.exception(e)
    except ValueError as e:
        logging.exception(e)
    else:
        print('no error')
    finally:
        print('finally...')
    print('end')

loggingError('o')

loggingError(0)