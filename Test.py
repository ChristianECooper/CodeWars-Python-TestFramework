import sys


class Test(object):
    def __init__(self):
        self.desc = "Undefined"
        self.it = "Undefined"
        self.failures = 0
        self.successes = 0

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

    def assert_equals(self, actual, expected, msg="{} should be {}"):
        eq = lambda a, b: a == b
        self._assert(eq, actual, expected, msg)

    def assert_not_equals(self, actual, unexpected, msg="{} should be {}"):
        neq = lambda a, b: a != b
        self._assert(neq, actual, unexpected, msg)

    def expect_error(self, msg, fn):
        try:
            fn()
            self._error("Expected an error" if not msg else msg, None, None)
        except:
            self._success()

    def expect(self, b, msg="Unexpected result"):
        be = lambda a, e: b
        self._assert(be, b, None, msg)

    def _error(self, msg, expected, actual):
        print "*** ERROR: {}".format(msg.format(expected, actual))
        self.failures += 1

    def _success(self):
        print "Test Passed"
        self.successes += 1

    def report(self):
        print "\nTest run complete"
        print "  Total tests: {}, Failures: {}, Successes: {}".format(
            self.failures + self.successes,
            self.failures,
            self.successes)
        if self.failures == 0:
            print "Happy Days!"
        else:
            print "Better luck next time!"


test = Test()
sys.exitfunc=test.report
