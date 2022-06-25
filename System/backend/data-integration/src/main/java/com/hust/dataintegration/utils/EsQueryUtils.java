package com.hust.dataintegration.utils;

import org.elasticsearch.index.query.*;

import java.util.List;
import java.util.stream.Collectors;

public class EsQueryUtils {

    public static  <T> TermsQueryBuilder buildTermsQueryBuilder(String key, List<T> values) {
        return QueryBuilders.termsQuery(key, values);
    }

    public static  <T> TermQueryBuilder buildTermQueryBuilder(String key, T value) {
        return QueryBuilders.termQuery(key, value);
    }

    public static  <T> MatchPhraseQueryBuilder buildMatchPhraseQuery(String key, T value) {
        return QueryBuilders.matchPhraseQuery(key, value);
    }

    public static  <T> List<MatchPhraseQueryBuilder> buildMatchPhraseQuery(String key, List<T> values) {
        return values.stream()
                .map(value -> QueryBuilders.matchPhraseQuery(key, value))
                .collect(Collectors.toList());
    }


    public static  <T extends QueryBuilder> void addBoolFilter(BoolQueryBuilder boolQueryBuilder, T condition) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.filter().add(condition);
    }

    public static  <T extends QueryBuilder> void addBoolFilter(BoolQueryBuilder boolQueryBuilder, List<T> conditions) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.filter().addAll(conditions);
    }

    public static  <T extends QueryBuilder> void addBoolMust(BoolQueryBuilder boolQueryBuilder, List<T> conditions) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.must().addAll(conditions);
    }

    public static  <T extends QueryBuilder> void addBoolMustNot(BoolQueryBuilder boolQueryBuilder, List<T> conditions) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.mustNot().addAll(conditions);
    }

    public static  <T extends QueryBuilder> void addBoolShould(BoolQueryBuilder boolQueryBuilder, List<T> conditions) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.should().addAll(conditions);
    }

    public static <T extends QueryBuilder> void addBoolMust(BoolQueryBuilder boolQueryBuilder, T condition) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.must().add(condition);
    }

    public static  <T extends QueryBuilder> void addBoolMustNot(BoolQueryBuilder boolQueryBuilder, T condition) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.mustNot().add(condition);
    }

    public static  <T extends QueryBuilder> void addBoolShould(BoolQueryBuilder boolQueryBuilder, T condition) {
        if (boolQueryBuilder == null) boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.should().add(condition);
    }


    public static  <T> BoolQueryBuilder boolShouldMatchPhraseQuery(String key, List<T> values) {
        BoolQueryBuilder boolQueryBuilder = QueryBuilders.boolQuery();
        boolQueryBuilder.should().addAll(buildMatchPhraseQuery(key, values));
        return boolQueryBuilder;
    }

    public static  <T> MatchQueryBuilder matchQuery(String key, List<T> values) {
        return QueryBuilders.matchQuery(key, values);
    }

    public static  <T> MatchQueryBuilder matchQuery(String key, T value) {
        return QueryBuilders.matchQuery(key, value);

    }

}
