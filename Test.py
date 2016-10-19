import sys
from datetime import datetime

class Test(object):
    """
    Implements the test interface as described here:
    http://www.codewars.com/docs/python-test-reference-1
    """
    
    def __init__(self):
        self.desc = u"Undefined"
        self.it = u"Undefined"
        self.failures = 0
        self.successes = 0
        self.start = datetime.now()

    def describe(self, msg):
        print msg
        self.desc = msg

    def it(self, msg):
        print msg
        self.it = msg

    def _assert(self, p, actual, expected, msg):
        if not p(expected, actual):
            self._error(msg, expected, actual)
        else:
            self._success()

    def assert_equals(self, actual, expected, msg=u"{} should be {}"):
        eq = lambda a, b: a == b
        self._assert(eq, actual, expected, msg)

    def assert_not_equals(self, actual, unexpected, msg=u"{} should be {}"):
        neq = lambda a, b: a != b
        self._assert(neq, actual, unexpected, msg)

    def expect_error(self, msg, fn):
        try:
            fn()
            self._error(u"Expected an error" if not msg else msg, None, None)
        except:
            self._success()

    def expect(self, b, msg=u"Unexpected result"):
        be = lambda a, e: b
        self._assert(be, b, None, msg)

    def _error(self, msg, expected, actual):
        print u"*** ERROR: {}".format(msg.format(actual, expected))
        self.failures += 1

    def _success(self):
        print "Test Passed"
        self.successes += 1

    def report(self):
        end = datetime.now()
        print u"\nTest run complete"
        print u"Passed: {}".format(self.successes)
        print u"Failed: {}".format(self.failures)
        print u"Total:  {}".format(self.successes + self.failures)

        delta = end - self.start
        print u"Process took {:,}ms to complete".format((delta.microseconds + 1000000 * delta.seconds) // 1000)
        if self.failures == 0:
            print u"Happy Days!"
        else:
            print u"Better luck next time!"

test = Test()
sys.exitfunc=test.report
