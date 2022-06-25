package com.hust.dataintegration.data.model;

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
    Integer price;
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
    String img="https://ecdn.game4v.com/g4v-content/uploads/2021/09/15122647/game4V-iPhone13-2-1631683607-83.jpg";

}
