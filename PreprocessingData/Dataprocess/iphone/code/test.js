let fs = require("fs"); 

let data = fs.readFileSync('input.json');
let obj = JSON.parse(data.toString());
//console.log(JSON.stringify(obj, null, '\t'));
let name = [];
/*for (let i=0; i<obj.length; i++ ) {
    name[i] = obj[i].name;
    console.log(name[i]);
}*/


let color = ["ĐEN","TRẮNG","XANH","HỒNG","TÍM","ĐỎ","BẠC","VÀNG",
            "ĐỒNG","XANH LÁ","XANH DƯƠNG","CAM","XANH SAN HÔ",
            "PACIFIC BLUE","SPACE GRAY","SILVER","MIDNIGHT GREEN",
            "GOLD","ROSE GOLD","SUNSET GOLD","BLACK","WHITE","GREEN",
            "PINK","RED PURPLE","THE SILVER","YELLOW","COPPER",
            "BLUE","RED","ORANGE","CORAL GREEN"];
let model = ["IPHONE 13","IPHONE 12","IPHONE 11","IPHONE 8","IPHONE X","IPHONE 7",
            "IPHONE 6","IPHONE 5","IPHONE 4","IPHONE 13 PRO","IPHONE 12 PRO","IPHONE 11 PRO",
            "IPHONE XS","IPHONE XR","IPHONE 6 PLUS","IPHONE 6S",
            "IPHONE SE 2", "IPHONE SE 3", "IPHONE 13 PRO MAX",
            "IPHONE 13 MINI","IPHONE 12 PRO MAX",
            "IPHONE 12 MINI","IPHONE 11 PRO MAX",
            "IPHONE XS MAX",
            "IPHONE 8 PLUS","IPHONE 7 PLUS",
            "IPHONE SE","IPHONE 6S PLUS",
            "IPHONE 5C","IPHONE 5S","IPHONE 4S","IPHONE 3GS","IPHONE 3G","IPHONE 2G",
            "IPAD MINI 3","IPAD MINI 1",
            "IPAD PRO 12,9","IPAD PRO 9.7","IPAD PRO 10.5","IPAD PRO 12.9","IPAD 10.2",
            "IPAD 9 10.2","IPAD AIR 10.9","IPAD PRO M1 12.9","IPAD AIR 10.9 INCH","IPAD 10.2 INCH",
            "IPAD MINI 6","IPAD 2010","IPAD 2 2011","IPAD PRO M1 11 INCH","IPAD 10.2 INCH",
            "IPAD 6 MINI","IPAD 3 MINI","IPAD AIR 3","IPAD GEN 9","IPAD PRO M1 11","IPAD AIR M1 10.9","IPAD MINI GEN 6TH","IPAD PRO M1 11","IPAD AIR4 10.9",
            "IPAD 3 2012","IPAD 4 2012","IPAD MINI 2012","IPAD AIR 2013",
            "IPAD MINI 2","IPAD AIR 2 2014","IPAD MINI 3 2014","IPAD PRO 12,9 INCH",
            "IPAD MINI 4","IPAD PRO 9.7 INCH","IPAB 2017","IPAD PRO 10.5 INCH","IPAD PRO 12.9 INCH",
            "IPAD PRO 12.9 INCH 2017","IPAD 2018","IPAD PRO 11","IPAD PRO 12.9 INCH 2018",
            "IPAD AIR 2019","IPAD MINI 5","IPAD 10.2 INCH 2019","IPAD AIR 4",
            "IPAD AIR 4 2020","IPAD PRO 11 INCH 2020","IPAD PRO 12.9 INCH 2020","IPAD PRO 12.9 INCH 2021",
            "IPAD 9","IPAD 9 10.2 INCH","IPAD 9 10.2 INCH 2021","IPAB MINI 6 2021",
            "IPAD AIR 5 M1","IPAD AIR 5 M1 2022","IPAD PRO M1 12.9 INCH",
            "IPAD MINI 7.9 INCH","IPAD PRO M1 2021 12.9 INCH","IPAD PRO M1 2021 11 INCH","IPAD AIR 10.5 INCH",
            "IPAD PRO M1 2021 12.9 INCH","IPAD PRO M1 2021 12.9 INCH","IPAD AIR 10.5 INCH",
            "APPLE GEN 1","APPLE SERIES 1","APPLE SERIES 2","APPLE SERIES 3","APPLE SERIES 4",
            "APPLE SERIES 5","APPLE SERIES 6","APPLE SE","APPLE WATCH GEN 1","APPLE WATCH SE",
            "APPLE WATCH SERIES 1","APPLE WATCH SERIES 2","APPLE WATCH SERIES 3","APPLE WATCH SERIES 4",
            "APPLE WATCH SERIES 5","APPLE WATCH SERIES 6","APPLE WATCH S1","APPLE WATCH S2","APPLE WATCH S3",
            "APPLE WATCH S4","APPLE WATCH S5","APPLE WATCH S6","APPLE WATCH S7"];
let disk = ["16GB","32GB","64GB","128GB","256GB","512GB","1TB"];
let ram = [" 16GB"," 8GB"," 6GB"," 4GB"," 3GB"," 2GB"," 1GB"];
let status = ["100%","99%", "98%", "97%","96%","95%","94%","93%","92%","91%","90","85%","80%","75%","cũ", "99,99%"];


for (let i=0; i<obj.length; i++) {
    for (let j=0; j<color.length; j++) {
        if (obj[i].name.toUpperCase().includes(color[j]) == true) {
            obj[i]["Color-split"]= color[j];
        }
    }
    for (let j=0; j<model.length; j++) {
        if (obj[i].name.toUpperCase().includes(model[j]) == true) {
            obj[i]["Model-split"]= model[j];
        }
    }
    for (let j=0; j<disk.length; j++) {
        if (obj[i].name.toUpperCase().includes(disk[j]) == true) {
            obj[i]["Rom-split"]= disk[j];
        }
    }
    for (let j=0; j<ram.length; j++) {
        if (obj[i].name.toUpperCase().includes(ram[j]) == true) {
            obj[i]["Ram-split"]= ram[j];
        }
    }
    for (let j=0; j<status.length; j++) {
        if (obj[i].name.toUpperCase().includes(status[j]) == true) {
            obj[i]["Status-split"]= status[j];
        }
    }
}
const result = obj;
//console.log(JSON.stringify(result, null, '\t'));
//result = JSON.stringify(data);
fs.writeFile("output.json", JSON.stringify(obj), function(err) {
    if (err) {
        console.log(err);
    }
});
for (let i=0; i<obj.length; i++) {
    if (obj[i]["Model-split"] == null) {
        console.log(obj[i].name);
    }
    
}
