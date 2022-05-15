package com.crawler.hhmb;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class HoangHaMobileCrawler {

    public static void main(String[] args) throws IOException {
        crawler("data/hoanghamobile/hoanghamobile.iphone.jl", "1", "iphone");
        crawler("data/hoanghamobile/hoanghamobile.ipad.jl", "2", "ipad");
        crawler("data/hoanghamobile/hoanghamobile.macbook.jl", "3", "macbook");
        crawler("data/hoanghamobile/hoanghamobile.apple-watch.jl", "5", "apple+watch");
    }

    public static void crawler(String fileName, String type, String keyword) throws IOException {//"https://hoanghamobile.com/tim-kiem?kwd=ipad&filters={%22type%22:%222%22}&search=true"
        Document doc = Jsoup.connect("https://hoanghamobile.com/tim-kiem?kwd="+keyword+"&filters={%22type%22:%22"+type+"%22}&search=true&p=100000000").get();

        File file = new File(fileName);
        if (!file.exists()) {
            file.createNewFile();
        }
        FileWriter fw = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fw);

        for (int i = 1; ; i++) {
            IPhone item = new IPhone().setDomain("https://hoanghamobile.com");
            Element rootItem = doc.select("body > section:nth-child(4) > div > div:nth-child(2) > div > div:nth-child(" + i + ")").first();
            if (rootItem == null) break;
            Element imgElement = rootItem.select("div > a > img").first();
            String img = imgElement.attr("src");
            item.setImg(img);
            Element infoElement = rootItem.select("div > a").first();
            String name = infoElement.attr("title");
            item.setName(name);
            String url = "https://hoanghamobile.com" + infoElement.attr("href");
            item.setUrl(url);
            Element priceElement = rootItem.getElementsByClass("price").first();
            try {
                String priceSale = priceElement.getElementsByTag("strong").text().replace(",", "").replace("đ", "").replace(" ", "");
                item.setPrice(priceSale);
            } catch (Exception e) {
            }
            try {
                String price = priceElement.getElementsByTag("strike").text().replace("đ", "").replace(",", "").replace(" ", "");
                item.setCost(price);
            } catch (Exception e) {
            }

            ObjectMapper mapper = new ObjectMapper();
            String json = mapper.writeValueAsString(item);

            bw.write(json + "\n");
        }
        bw.close();
    }
}
