package model;

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
}
