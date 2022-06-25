package com.hust.dataintegration.data.model;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class AppleProductType {
    String id;
    String name;
    String ram;
    String rom;
    String color;
    String cpu;
    String img="https://ecdn.game4v.com/g4v-content/uploads/2021/09/15122647/game4V-iPhone13-2-1631683607-83.jpg";
    long count;
}
