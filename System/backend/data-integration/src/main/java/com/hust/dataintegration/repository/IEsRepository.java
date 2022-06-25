package com.hust.dataintegration.repository;


import com.hust.dataintegration.data.model.AppleProduct;
import com.hust.dataintegration.data.model.AppleProductType;
import com.hust.dataintegration.data.request.SearchAppleTypeRequest;

import java.util.List;
import java.util.Map;

public interface IEsRepository {
    List<AppleProductType> searchAppleType(SearchAppleTypeRequest request);
    Map<String, Long> countByAppleTypeIds(List<String> appleTypeIds);
    List<AppleProduct> searchAppleProduct(Integer appleTypeId);
}
