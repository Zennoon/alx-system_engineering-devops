DD_API_KEY="1e73407a0d9e2be7651486a816868a5c"
DD_APP_KEY="7d8dd3e23fac69e4147463b21db68f61d04f2612"

# Curl command
curl -X GET "https://api.datadoghq.com/api/v1/dashboard/437-unv-6d4" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"