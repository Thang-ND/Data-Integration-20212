package com.hust.dataintegration.data.request;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class SearchAppleTypeRequest {
    String name;
    Integer ram;
    Integer rom;
    String color;
    String cpu;
}
