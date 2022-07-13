import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import lombok.SneakyThrows;
import model.AppleProduct;
import model.AppleProductType;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;
import java.util.stream.Collectors;

public class ConvertData {
    @SneakyThrows
    public static void convert() {
        ObjectMapper objectMapper = new ObjectMapper()
                .setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE);

        int lenType = 403;
        String pathType = "/home/thanhnv/Desktop/e/Data-Integration-20212/DataMatching/products_Result.json";
        String jsonStringType = getAllTextInFile(pathType);
        JSONObject objType = new JSONObject(jsonStringType);
        JSONObject nameType = objType.getJSONObject("name");
        JSONObject cpuType = objType.getJSONObject("cpu");
        JSONObject colorType = objType.getJSONObject("color");
        JSONObject ramType = objType.getJSONObject("ram");
        JSONObject romType = objType.getJSONObject("rom");
        JSONObject listId = objType.getJSONObject("list_id");

        List<AppleProductType> appleProductTypeList = new ArrayList<>();
        Map<String, String> mapProductAndProductType = new HashMap<>();

        for (int i = 0; i <= lenType; i++) {
            AppleProductType appleProductType = new AppleProductType()
                    .setId(String.valueOf(i))
                    .setName(nameType.get(String.valueOf(i)).equals(null) ? null : nameType.getString(String.valueOf(i)))
                    .setCpu(cpuType.get(String.valueOf(i)).equals(null) ? null : cpuType.getString(String.valueOf(i)))
                    .setColor(colorType.get(String.valueOf(i)).equals(null) ? null : colorType.getString(String.valueOf(i)))
                    .setRam(ramType.get(String.valueOf(i)).equals(null) ? null : ramType.getString(String.valueOf(i)))
                    .setRom(romType.get(String.valueOf(i)).equals(null) ? null : romType.getString(String.valueOf(i)));

            appleProductTypeList.add(appleProductType);

            JSONArray jsonArray = listId.getJSONArray(String.valueOf(i));
            for (int j = 0; j < jsonArray.length(); j++) {
                String productId = String.valueOf(jsonArray.getInt(j));
                mapProductAndProductType.put(productId, String.valueOf(i));
            }
        }


        int len = 2773;
        String path = "/home/thanhnv/Desktop/e/Data-Integration-20212/DataMatching/data.json";
        String jsonString = getAllTextInFile(path);
        JSONObject obj = new JSONObject(jsonString);
        JSONObject name = obj.getJSONObject("name");
        JSONObject url = obj.getJSONObject("url");
        JSONObject cpu = obj.getJSONObject("cpu");
        JSONObject gpu = obj.getJSONObject("gpu");
        JSONObject ram = obj.getJSONObject("ram");
        JSONObject rom = obj.getJSONObject("rom");
        JSONObject os = obj.getJSONObject("os");
        JSONObject resolution = obj.getJSONObject("resolution");
        JSONObject price = obj.getJSONObject("price");
        JSONObject connect = obj.getJSONObject("connect");
        JSONObject screenType = obj.getJSONObject("screentype");
        JSONObject color = obj.getJSONObject("color");
        JSONObject frontCamera = obj.getJSONObject("front_camera");
        JSONObject rearCamera = obj.getJSONObject("rear_camera");
        JSONObject batteryCapacity = obj.getJSONObject("battery_capacity");
        JSONObject bluetooth = obj.getJSONObject("bluetooth");
        JSONObject wifi = obj.getJSONObject("wifi");
        JSONObject size = obj.getJSONObject("size");
        JSONObject weight = obj.getJSONObject("weight");
        JSONObject jackAudio = obj.getJSONObject("jack_audio");
        JSONObject mobileNetwork = obj.getJSONObject("mobile_network");
        JSONObject sim = obj.getJSONObject("sim");
        JSONObject security = obj.getJSONObject("security");
        JSONObject material = obj.getJSONObject("material");
        List<AppleProduct> appleProducts = new ArrayList<>();
        for (int i = 0; i <= len; i++) {
            AppleProduct appleProduct = new AppleProduct()
                    .setId(String.valueOf(i))
                    .setName(name.get(String.valueOf(i)).equals(null) ? null : name.getString(String.valueOf(i)))
                    .setUrl(url.get(String.valueOf(i)).equals(null) ? null : url.getString(String.valueOf(i)))
                    .setCpu(cpu.get(String.valueOf(i)).equals(null) ? null : cpu.getString(String.valueOf(i)))
                    .setGpu(gpu.get(String.valueOf(i)).equals(null) ? null : gpu.getString(String.valueOf(i)))
                    .setRam(ram.get(String.valueOf(i)).equals(null) ? null : ram.getString(String.valueOf(i)))
                    .setRom(rom.get(String.valueOf(i)).equals(null) ? null : rom.getString(String.valueOf(i)))
                    .setOs(os.get(String.valueOf(i)).equals(null) ? null : os.getString(String.valueOf(i)))
                    .setResolution(resolution.get(String.valueOf(i)).equals(null) ? null : resolution.getString(String.valueOf(i)))
                    .setPrice(price.get(String.valueOf(i)).equals(null) ? null : String.valueOf(price.get(String.valueOf(i))))
                    .setConnect(connect.get(String.valueOf(i)).equals(null) ? null : connect.getString(String.valueOf(i)))
                    .setScreentype(screenType.get(String.valueOf(i)).equals(null) ? null : screenType.getString(String.valueOf(i)))
                    .setColor(color.get(String.valueOf(i)).equals(null) ? null : color.getString(String.valueOf(i)))
                    .setFrontCamera(frontCamera.get(String.valueOf(i)).equals(null) ? null : frontCamera.getString(String.valueOf(i)))
                    .setRearCamera(rearCamera.get(String.valueOf(i)).equals(null) ? null : rearCamera.getString(String.valueOf(i)))
                    .setBatteryCapacity(batteryCapacity.get(String.valueOf(i)).equals(null) ? null : String.valueOf(batteryCapacity.get(String.valueOf(i))))
                    .setBluetooth(bluetooth.get(String.valueOf(i)).equals(null) ? null : bluetooth.getString(String.valueOf(i)))
                    .setWifi(wifi.get(String.valueOf(i)).equals(null) ? null : wifi.getString(String.valueOf(i)))
                    .setSize(size.get(String.valueOf(i)).equals(null) ? null : String.valueOf(size.get(String.valueOf(i))))
                    .setWeight(weight.get(String.valueOf(i)).equals(null) ? null : String.valueOf(weight.get(String.valueOf(i))))
                    .setJackAudio(jackAudio.get(String.valueOf(i)).equals(null) ? null : jackAudio.getString(String.valueOf(i)))
                    .setMobileNetwork(mobileNetwork.get(String.valueOf(i)).equals(null) ? null : mobileNetwork.getString(String.valueOf(i)))
                    .setSim(sim.get(String.valueOf(i)).equals(null) ? null : sim.getString(String.valueOf(i)))
                    .setSecurity(security.get(String.valueOf(i)).equals(null) ? null : security.getString(String.valueOf(i)))
                    .setMaterial(material.get(String.valueOf(i)).equals(null) ? null : material.getString(String.valueOf(i)))
                    .setProductTypeId(mapProductAndProductType.get(String.valueOf(i)));

            appleProducts.add(appleProduct);
        }

        BufferedWriter bw = null;
        FileWriter fw = null;

        File file = new File("/home/thanhnv/Desktop/thdl/Data-Integration-20212/System/convert-data-es/src/main/resources/data/productType.jl");

        // if file doesnt exists, then create it
        if (!file.exists()) {
            file.createNewFile();
        }

        // true = append file
        fw = new FileWriter(file.getAbsoluteFile(), true);
        bw = new BufferedWriter(fw);

        for(AppleProductType appleProductType : appleProductTypeList){
            String json = objectMapper.writeValueAsString(appleProductType);

            bw.write("{\"index\": {\"_index\": \"apple_product_type\", \"_id\":\""+ appleProductType.getId() +"\"}}\n");
            bw.write(json+"\n");
        }

        bw.close();
        fw.close();


        file = new File("/home/thanhnv/Desktop/thdl/Data-Integration-20212/System/convert-data-es/src/main/resources/data/product.jl");

        // if file doesnt exists, then create it
        if (!file.exists()) {
            file.createNewFile();
        }

        // true = append file
        fw = new FileWriter(file.getAbsoluteFile(), true);
        bw = new BufferedWriter(fw);

        for(AppleProduct appleProduct : appleProducts){
            String json = objectMapper.writeValueAsString(appleProduct);
            String encrypt = encrypt(appleProduct.getUrl()+appleProduct.getColor().toUpperCase());
            bw.write("{\"index\": {\"_index\": \"apple_product\", \"_id\":\""+ encrypt +"\"}}\n");
            bw.write(json+"\n");
        }

        bw.close();
        fw.close();
    }

    public static String readFile(String path, Charset encoding) throws IOException {
        String content = Files.lines(Paths.get(path), encoding)
                .collect(Collectors.joining(System.lineSeparator()));

        return content;
    }

    private static MessageDigest sha256;

    // generated password is stored encrypted (using also user name for hashing)
    public synchronized static String encrypt(String hash) {
        try {

            StringBuilder builder = new StringBuilder();
            builder.append(hash);

            // first time , encrypt user name , password and static key
            String encryptedCredentials = encryptionIterator(builder.toString());
            return encryptedCredentials;
        }

        catch (Exception e) {
            e.printStackTrace();
        }

        return "";
    }

    private static String encryptionIterator(String content) {
        try {
            sha256 = MessageDigest.getInstance("SHA-256");
            // append the static key to each iteration
            byte[] passBytes = (content).getBytes();
            sha256.reset();
            byte[] digested = sha256.digest(passBytes);
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < digested.length; i++) {
                sb.append(Integer.toHexString(0xff & digested[i]));
            }

            return sb.toString();
        } catch (NoSuchAlgorithmException ex) {
            ex.printStackTrace();
        }

        return "";
    }

    public static void main(String[] args) {
        convert();
    }

    public static String getAllTextInFile(String path) {
        String content = null;
        try {
            content = readFile(path, StandardCharsets.UTF_8);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content;
    }

}
