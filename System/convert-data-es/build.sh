curl -X DELETE 'localhost:9200/apple_product'
curl -X DELETE 'localhost:9200/apple_product_type'
curl -X POST 'localhost:9200/hotel/_bulk?pretty' -H 'Content-type: application/json' --data-binary @./src/main/resources/data/productType.jl
curl -X POST 'localhost:9200/hotel/_bulk?pretty' -H 'Content-type: application/json' --data-binary @./src/main/resources/data/product.jl
