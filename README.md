# AzureFunctionsPythonHttp4MBBug

Repro repo for azure functions azure-functions-python-worker release 1.1.2 703 hotfix.
Issue: Python unable to process 4MB loads.
https://github.com/Azure/azure-functions-python-worker/pull/703

Includes sample 3.99MB txt file and 4.01MB txt file.

Hit this issue in az production while trying to image/doc process with Python.
Burned a few days on it.  Repro'd locally in func.exe core tools.

Maintainers
TODO: Got E2E test for various file / payload sizes?
SUGGEST: Do we automate E2E test with DevOps/Postman?
https://medium.com/@ganeshsirsi/how-to-configure-postman-newman-api-tests-in-azure-devops-or-tfs-and-publish-html-results-caf60a25c8b9

Note: 💪 Go open source! Thanks for MS team for releasing this hotfix!




