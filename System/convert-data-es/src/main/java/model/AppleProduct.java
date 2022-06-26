package model;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class AppleProduct {
    String id;
    String productTypeId;
    String name;
    String ram;
    String rom;
    String color;
    String url;
    String cpu;
    String os;
    String gpu;
    String price;
    String connect;
    String screentype;
    String frontCamera;
    String rearCamera;
    String batteryCapacity;
    String bluetooth;
    String wifi;
    String size;
    String resolution;
    String weight;
    String jackAudio;
    String mobileNetwork;
    String sim;
    String security;
    String material;
}
