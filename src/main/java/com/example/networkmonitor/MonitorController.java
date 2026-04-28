package com.example.networkmonitor;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;
import java.util.Map;

@RestController
public class MonitorController {

    @GetMapping("/status")
    public Map<String, String> getStatus() {
        Map<String, String> status = new HashMap<>();
        status.put("service", "Network Monitor");
        status.put("ospf_status", "Running");
        status.put("bgp_neighbor", "172.25.85.75 - Established");
        return status;
    }
}