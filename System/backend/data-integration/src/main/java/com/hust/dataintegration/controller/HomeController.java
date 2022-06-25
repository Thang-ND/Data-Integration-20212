package com.hust.dataintegration.controller;

import com.hust.dataintegration.data.request.SearchAppleTypeRequest;
import com.hust.dataintegration.data.response.DfResponse;
import com.hust.dataintegration.repository.IEsRepository;
import lombok.experimental.Accessors;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "/api")
public class HomeController {
    @Autowired
    private IEsRepository esRepository;

    @PostMapping(value = "/search")
    public ResponseEntity<?> search(@RequestBody SearchAppleTypeRequest request){
        return DfResponse.okEntity(esRepository.searchAppleType(request));
    }

    @GetMapping(value = "/search/{productTypeId}")
    public ResponseEntity<?> search(@PathVariable Integer productTypeId){
        return DfResponse.okEntity(esRepository.searchAppleProduct(productTypeId));
    }
}
