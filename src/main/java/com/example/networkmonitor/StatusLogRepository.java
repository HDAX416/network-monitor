package com.example.networkmonitor;

import org.springframework.data.jpa.repository.JpaRepository;

public interface StatusLogRepository extends JpaRepository<StatusLog, Long> {
}