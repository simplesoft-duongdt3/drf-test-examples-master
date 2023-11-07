pytest --cov --cov-report=html:coverage_reports lecture_api_testing/tests/integration_test --junitxml=test-reports/integration_test.xml

python -m junit2htmlreport test-reports/integration_test.xml test-reports/integration_test.html
python -m junit2htmlreport test-reports/integration_test.xml --report-matrix test-reports/integration_test.html
open test-reports/integration_test.html
open coverage_reports/index.html