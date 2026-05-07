package com.example.networkmonitor;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "status_logs")
public class StatusLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String ospfStatus;
    private String bgpNeighbor;
    private LocalDateTime recordTime = LocalDateTime.now();

    public StatusLog() {}
    public StatusLog(String ospfStatus, String bgpNeighbor) {
        this.ospfStatus = ospfStatus;
        this.bgpNeighbor = bgpNeighbor;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getOspfStatus() { return ospfStatus; }
    public void setOspfStatus(String ospfStatus) { this.ospfStatus = ospfStatus; }
    public String getBgpNeighbor() { return bgpNeighbor; }
    public void setBgpNeighbor(String bgpNeighbor) { this.bgpNeighbor = bgpNeighbor; }
    public LocalDateTime getRecordTime() { return recordTime; }
    public void setRecordTime(LocalDateTime recordTime) { this.recordTime = recordTime; }
}