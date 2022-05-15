package com.crawler.nguyenkim;

import com.crawler.hhmb.IPhone;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class NguyenKimCrawler {
    public static void main(String[] args) {
        crawler("data/nguyenkim/nguyenkim.iphone.jl", "iphone");
        crawler("data/nguyenkim/nguyenkim.ipad.jl", "ipad");
        crawler("data/nguyenkim/nguyenkim.macbook.jl", "macbook");
        crawler("data/nguyenkim/nguyenkim.apple-watch.jl", "apple+watch");
    }

    @SneakyThrows
    public static void crawler(String fileName, String keyword) {
        File file = new File(fileName);
        if (!file.exists()) {
            file.createNewFile();
        }
        FileWriter fw = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fw);

        String link = "https://www.nguyenkim.com/tim-kiem.html?tu-khoa="+keyword+"&thuong-hieu=apple&trang=";
        for (int i = 1; ; i++) {
            Document document = Jsoup.connect(link + i).get();
            Elements itemsElement = document.getElementsByClass("product-card nk-new-layout-product-grid");
            if (itemsElement.isEmpty()) break;

            for (Element element : itemsElement) {
                IPhone item = new IPhone().setDomain("https://www.nguyenkim.com");
                String name = element.attr("data-product-name");
                item.setName(name);
                String img = element.select("div > div > a > img").attr("src");
                item.setImg(img);
                String url = element.select("div > div > a").attr("href");
                item.setUrl(url);
                try {
                    String price = element.getElementsByClass("product-card__price-after-amount").text().replace(".", "").replace("đ", "");
                    item.setPrice(price);
                } catch (Exception e) {
                }

                try {
                    String cost = element.getElementsByClass("product-card__price-before-amount").text().replace(".", "").replace("đ", "");
                    item.setCost(cost);
                } catch (Exception e) {
                }

                ObjectMapper mapper = new ObjectMapper();
                String json = mapper.writeValueAsString(item);

                bw.write(json + "\n");
            }
        }
        bw.close();
    }
}
