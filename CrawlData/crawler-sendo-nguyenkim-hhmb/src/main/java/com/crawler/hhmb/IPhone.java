package com.crawler.hhmb;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class IPhone {
    String domain;
    String name;
    String img;
    String price;
    String cost;
    String url;
}
