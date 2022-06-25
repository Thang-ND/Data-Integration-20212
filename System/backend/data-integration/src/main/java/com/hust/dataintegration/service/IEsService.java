package com.hust.dataintegration.service;

import com.hust.dataintegration.data.model.AppleProductType;
import com.hust.dataintegration.data.request.SearchAppleTypeRequest;

import java.util.List;

public interface IEsService {
    List<AppleProductType> searchAppleType(SearchAppleTypeRequest request);
}
