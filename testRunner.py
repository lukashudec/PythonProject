import runpy

def run_unit_test_with_coverage():
    import pytest
    pytest.main(["-x", "test_unit/test_calendar_class.py",
                 '--html-report', './report/pytest',
                 '--verbose',
                 '--disable-warnings',
                 '--cov-report', 'html:./report/coverage',
                 '--cov', 'Calendar'])

    if __name__ == '__main__':
        run_unit_test_with_coverage()


def run_end2end():
    import pytest
    pytest.main(["-x", "test_e2e/tests.py",
                 '--html-report', './report/pytest',
                 '--verbose',
                 '--disable-warnings'])

    if __name__ == '__main__':
        run_unit_test_with_coverage()