package com.example.networkmonitor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;
import java.util.Map;

@RestController
public class StatusController {

    @Autowired
    private StatusLogRepository repository;

    private int requestCount = 0;

    @GetMapping("/status")
    public Map<String, String> getStatus() {
        requestCount++;

        String ospf = "Full";
        String bgp = "Established";

        // 模拟 OSPF 邻居状态波动，每5次出现一次 Init
        if (requestCount % 5 == 0) {
            ospf = "Init";
        }
        // 模拟 BGP 邻居断连，每7次出现一次 Idle
        if (requestCount % 7 == 0) {
            bgp = "Idle";
        }

        // 保存到数据库
        StatusLog log = new StatusLog(ospf, bgp);
        repository.save(log);

        Map<String, String> result = new HashMap<>();
        result.put("ospf_status", ospf);
        result.put("bgp_neighbor", bgp);
        result.put("request_count", String.valueOf(requestCount));
        return result;
    }
}