package com.hust.dataintegration.repository;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import com.hust.dataintegration.data.model.AppleProduct;
import com.hust.dataintegration.data.model.AppleProductType;
import com.hust.dataintegration.data.request.SearchAppleTypeRequest;
import lombok.SneakyThrows;
import org.apache.commons.lang3.StringUtils;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.action.support.IndicesOptions;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.SearchHits;
import org.elasticsearch.search.aggregations.AggregationBuilders;
import org.elasticsearch.search.aggregations.Aggregations;
import org.elasticsearch.search.aggregations.bucket.terms.Terms;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.*;
import java.util.stream.Collectors;

import static com.hust.dataintegration.utils.EsQueryUtils.*;
import static org.apache.commons.lang3.ObjectUtils.isNotEmpty;

@Repository
public class EsRepository implements IEsRepository {
    @Autowired
    private RestHighLevelClient client;

    private ObjectMapper objectMapper = new ObjectMapper()
            .setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE);

    @SneakyThrows
    @Override
    public List<AppleProductType> searchAppleType(SearchAppleTypeRequest request) {
        BoolQueryBuilder mainQuery = QueryBuilders.boolQuery();


        if (isNotEmpty(request.getName())) {
            List<String> nameStr = List.of(request.getName().split(" "));

            for (String name : nameStr) {
                addBoolFilter(mainQuery, matchQuery("name", name));
            }
        }


        if (isNotEmpty(request.getColor()))
            addBoolFilter(mainQuery, matchQuery("color", request.getColor()));

        if (isNotEmpty(request.getRam()))
            addBoolFilter(mainQuery, matchQuery("ram", request.getRam()));

        if (isNotEmpty(request.getRom()))
            addBoolFilter(mainQuery, matchQuery("rom", request.getRom()));

        if (isNotEmpty(request.getCpu()))
            addBoolFilter(mainQuery, matchQuery("cpu", request.getCpu()));

        SearchSourceBuilder builder = new SearchSourceBuilder();
        builder.query(mainQuery);
        builder.size(5000);

        SearchRequest searchRequest = new SearchRequest().indices("apple_product_type");
        searchRequest.searchType(SearchType.DFS_QUERY_THEN_FETCH);
        searchRequest.source(builder);
        searchRequest.indicesOptions(IndicesOptions.lenientExpandOpen());

        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);

        List<AppleProductType> results = getSearchResultList(searchResponse.getHits());

        List<String> ids = Optional.ofNullable(results).orElse(new ArrayList<>())
                .stream().map(AppleProductType::getId)
                .collect(Collectors.toList());

        Map<String, Long> integerIntegerMap = countByAppleTypeIds(ids);

        Optional.ofNullable(results).orElse(new ArrayList<>())
                .forEach(item -> {
                    if (integerIntegerMap.containsKey(item.getId()))
                        item.setCount(integerIntegerMap.get(item.getId()));
                });

        return results;
    }

    @SneakyThrows
    @Override
    public Map<String, Long> countByAppleTypeIds(List<String> appleTypeIds) {
        SearchSourceBuilder builder = new SearchSourceBuilder().size(0);
        builder.query(buildTermsQueryBuilder("product_type_id.keyword", appleTypeIds));
        builder.aggregation(AggregationBuilders.terms("product").field("product_type_id.keyword").size(1000));
        SearchRequest searchRequest = new SearchRequest().indices("apple_product");
        searchRequest.searchType(SearchType.DFS_QUERY_THEN_FETCH);
        searchRequest.source(builder);
        searchRequest.indicesOptions(IndicesOptions.lenientExpandOpen());

        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);

        Aggregations aggregations = searchResponse.getAggregations();
        Terms terms = aggregations.get("product");

        Collection<Terms.Bucket> buckets = (Collection<Terms.Bucket>) terms.getBuckets();

        Map<String, Long> results = new HashMap<>();

        Optional.ofNullable(buckets).orElse(new ArrayList<>()).stream().forEach(bucket -> {
            results.put((String) bucket.getKey(), bucket.getDocCount());
        });
        return results;
    }

    @SneakyThrows
    @Override
    public List<AppleProduct> searchAppleProduct(Integer appleTypeId) {
        SearchSourceBuilder builder = new SearchSourceBuilder();
        builder.query(buildTermQueryBuilder("product_type_id.keyword", appleTypeId));
        builder.size(5000);

        SearchRequest searchRequest = new SearchRequest().indices("apple_product");
        searchRequest.searchType(SearchType.DFS_QUERY_THEN_FETCH);
        searchRequest.source(builder);
        searchRequest.indicesOptions(IndicesOptions.lenientExpandOpen());

        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);

        SearchHit[] searchHits = searchResponse.getHits().getHits();
        List<AppleProduct> articleResponses = new ArrayList<>();
        for (SearchHit searchHit : searchHits) {
            String source = searchHit.getSourceAsString();
            AppleProduct articleResponse = this.objectMapper.readValue(source, AppleProduct.class);
            articleResponse.setImg(mapImg(articleResponse.getName()));
            articleResponses.add(articleResponse);
        }
        return articleResponses;
    }

    @SneakyThrows
    private List<AppleProductType> getSearchResultList(SearchHits searchHitArr) {
        List<AppleProductType> articleResponses = new ArrayList<>();
        for (SearchHit searchHit : searchHitArr) {
            String source = searchHit.getSourceAsString();
            AppleProductType articleResponse = this.objectMapper.readValue(source, AppleProductType.class);
            articleResponse.setImg(mapImg(articleResponse.getName()));
            articleResponses.add(articleResponse);
        }
        return articleResponses;
    }

    private String mapImg(String name) {
        String path = "http://localhost:8082/image/";
        if (StringUtils.containsIgnoreCase(name, "iphone 13")
                && (StringUtils.containsIgnoreCase(name, "pro") || StringUtils.containsIgnoreCase(name, "pro max")))
            return path + "iphone_13_pro_max.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 13"))
            return path + "iphone_13.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 12")
                && (StringUtils.containsIgnoreCase(name, "pro") || StringUtils.containsIgnoreCase(name, "pro max")))
            return path + "iphone_12_pro_max.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 12"))
            return path + "iphone_12.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 11")
                && (StringUtils.containsIgnoreCase(name, "pro") || StringUtils.containsIgnoreCase(name, "pro max")))
            return path + "iphone_11_pro_max.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 11"))
            return path + "iphone_11.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone x")
                && (StringUtils.containsIgnoreCase(name, "xs") || StringUtils.containsIgnoreCase(name, "xs max")))
            return path + "iphone_xs.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone x"))
            return path + "iphone_x.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 8")
                && (StringUtils.containsIgnoreCase(name, "s") || StringUtils.containsIgnoreCase(name, "plus")))
            return path + "iphone_8_plus.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 8"))
            return path + "iphone_8.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 7")
                && (StringUtils.containsIgnoreCase(name, "s") || StringUtils.containsIgnoreCase(name, "plus")))
            return path + "iphone_7_plus.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 7"))
            return path + "iphone_7.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 6")
                && (StringUtils.containsIgnoreCase(name, "s") || StringUtils.containsIgnoreCase(name, "plus")))
            return path + "iphone_6_plus.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone 6"))
            return path + "iphone_6.png";
        else if (StringUtils.containsIgnoreCase(name, "iphone"))
            return path + "iphone_13.png";
        else if (StringUtils.containsIgnoreCase(name, "apple watch") && StringUtils.containsIgnoreCase(name, "series"))
            return path + "apple_watch_series_6.png";
        else if (StringUtils.containsIgnoreCase(name, "watch"))
            return path + "apple_watch_se.png";
        else if (StringUtils.containsIgnoreCase(name, "ipad") && StringUtils.containsIgnoreCase(name, "11"))
            return path + "ipad_11_pro.png";
        else if (StringUtils.containsIgnoreCase(name, "ipad") && StringUtils.containsIgnoreCase(name, "mini"))
            return path + "ipad_mini.png";
        else if (StringUtils.containsIgnoreCase(name, "ipad"))
            return path + "ipad_air.png";
        else return path + "apple.png";
    }
}
