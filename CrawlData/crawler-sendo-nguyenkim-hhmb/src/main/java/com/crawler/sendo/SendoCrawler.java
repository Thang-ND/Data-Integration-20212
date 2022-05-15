package com.crawler.sendo;


import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.jetbrains.annotations.NotNull;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SendoCrawler {

    public static void main(String[] args) throws IOException {
        crawlerIphone();
        crawlerIpad();
        crawlerMacbook();
        crawlerAppleWatch();

    }

    @SneakyThrows
    public static void crawlerIpad() {
        Response response = getResponse("ipad", 0);
        JsonNode jsonNode = new ObjectMapper().readTree(response.body().string());
        for (int j = 0; j < 60; j++) {
            String data = String.valueOf(jsonNode.get("data").get(j));
            appendFile("data/sendo/sendo.ipad.jl", data);
        }
    }

    @SneakyThrows
    public static void crawlerAppleWatch() {
        Response response = getResponse("apple watch", 0);
        JsonNode jsonNode = new ObjectMapper().readTree(response.body().string());
        for (int j = 0; j < 60; j++) {
            String data = String.valueOf(jsonNode.get("data").get(j));
            appendFile("data/sendo/sendo.watch.jl", data);
        }
    }

    @SneakyThrows
    public static void crawlerMacbook() {
        for (int i = 0; i < 2; i++) {
            Response response = getResponse("macbook", i);
            JsonNode jsonNode = new ObjectMapper().readTree(response.body().string());
            for (int j = 0; j < 60; j++) {
                String data = String.valueOf(jsonNode.get("data").get(j));
                appendFile("data/sendo/sendo.macbook.jl", data);
            }
        }
    }

    public static void crawlerIphone() throws IOException {
        List<String> sp = new ArrayList<>();
        sp.add("iphone 4");
        sp.add("iphone 5");
        sp.add("iphone 6");
        sp.add("iphone 7");
        sp.add("iphone 8");
        sp.add("iphone x");
        sp.add("iphone 11");
        sp.add("iphone 12");
        sp.add("iphone 13");


        for (int i = 0; i < sp.size(); i++) {
            Response response = getResponse(sp.get(i), 0);
            JsonNode jsonNode = new ObjectMapper().readTree(response.body().string());
            for (int j = 0; j < 60; j++) {
                String data = String.valueOf(jsonNode.get("data").get(j));
                appendFile("data/sendo/sendo.iphone.jl", data);
            }
        }
    }

    private static void appendFile(String url, String data) throws IOException {
        File file = new File(url);

        if (!file.exists()) {
            file.createNewFile();
        }

        FileWriter fw = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(data + "\n");
        bw.close();
    }

    @NotNull
    private static Response getResponse(String keyword, int page) throws IOException {
        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        Request request = new Request.Builder()
                .url("https://searchlist-api.sendo.vn/web/products?q=" + keyword + "&platform=web&page=" + page + "&size=60&sortType=rank&search_type=&app_ver=2.24.15&track_id=53cb60ea-0c79-4aef-afe9-4667a1a33756&search_suggestion_list=&search_textbox_string=&click_suggestion_index=")
                .method("GET", null)
                .addHeader("authority", "searchlist-api.sendo.vn")
                .addHeader("sec-ch-ua", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"")
                .addHeader("sec-ch-ua-mobile", "?0")
                .addHeader("user-agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36")
                .addHeader("sec-ch-ua-platform", "\"Linux\"")
                .addHeader("accept", "*/*")
                .addHeader("origin", "https://www.sendo.vn")
                .addHeader("sec-fetch-site", "same-site")
                .addHeader("sec-fetch-mode", "cors")
                .addHeader("sec-fetch-dest", "empty")
                .addHeader("referer", "https://www.sendo.vn/")
                .addHeader("accept-language", "vi,en-US;q=0.9,en;q=0.8,bn;q=0.7")
                .addHeader("cookie", "aff_last_click=Affiliate%7Cgoogle%7Cwww_sendo_vn%7C; _ga=GA1.2.2026885182.1652199356; _gid=GA1.2.744737133.1652199356; _tt_enable_cookie=1; _ttp=839fb56f-8008-4814-b1d7-88175a50ccff; client_id=4eaedfe7-ee09-44d5-b639-1c81636d121a; tracking_id=53cb60ea-0c79-4aef-afe9-4667a1a33756; _strs=1652199356.utmcsr%3Dgoogle%7Cutmccn%3D15838893098-130814814126%7Cutmcmd%3Dcpc%7Cutmctr%3D%7Cutmcct%3D%7Cgclid%3DCj0KCQjwmuiTBhDoARIsAPiv6L-TLz8lP7rfKSFVSFJcVTqsIY0T8ZmLvF6DcClB7yNy-Yc6wUYbXoAaAq4nEALw_wcB; _gac_UA-32891946-6=1.1652228915.Cj0KCQjwmuiTBhDoARIsAPiv6L-TLz8lP7rfKSFVSFJcVTqsIY0T8ZmLvF6DcClB7yNy-Yc6wUYbXoAaAq4nEALw_wcB; cto_bundle=ekWro19ST1AlMkJETmRuREZhUjVvOU83TTN5MXZVMCUyRm1rS3IlMkZua2xid0VjMTN0VUFibUNrNDJUMEkxMUZsZEpadlkwbWtJWWxKOU0waGFTamRKc09hTnU4b3huTlNsNVNLZ0hPSFp5SVpoMmlGTEYzNXNGdDhIN3JVcmtQcFhoQlI3eXZyMzZVQUg0Q1B0UmclMkJJdzN2SlFlcyUyRnl3JTNEJTNE")
                .build();
        Response response = client.newCall(request).execute();
        return response;
    }

}
