package com.hust.dataintegration.data.request;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class SearchAppleTypeRequest {
    String name;
    String ram;
    String rom;
    String color;
    String cpu;
}
