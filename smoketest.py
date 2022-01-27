from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest


assertionsTest=TestLoader().loadTestsFromTestCase(AssertionsTest)
searchtest=TestLoader().loadTestsFromTestCase(SearchTest)

smoketest=TestSuite([assertionsTest,searchtest])

kwargs={
    "output": 'smoke-test'
}
runner=HTMLTestRunner(**kwargs)
runner.run(smoketest)