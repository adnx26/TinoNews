curl --location --request POST 'https://us-west-2.aws.data.mongodb-api.com/app/data-wbhnv/endpoint/data/v1/action/findOne' \
--header 'Content-Type: application/json' \
--header 'Access-Control-Request-Headers: *' \
--header 'api-key: vEU5ZmAsdzLubiS3RmoTGwuKmTA7qRGy4PfizvMsk210Jo9tR3oAGHWkrYBmHiA2' \
--data-raw '{
    "collection":"sales",
    "database":"sample_supplies",
    "dataSource":"TinoNews",
    "projection": {"_id": 1}
}'