# System Design Case Study: URL Shortener (like bit.ly)

**Date:** 2025-09-14  
**Difficulty:** Medium  
**Estimated Users:** 100M+ daily active users  

## Problem Statement

Design a URL shortening service that takes long URLs and converts them to shorter, more manageable URLs. When users click the short URL, they should be redirected to the original long URL.

## Requirements

### Functional Requirements
- Shorten long URLs to shorter aliases
- Redirect short URLs to original long URLs
- Custom aliases (optional)
- URL expiration (optional)
- Analytics (click tracking)

### Non-Functional Requirements  
- **Availability:** 99.9% uptime
- **Latency:** < 100ms for redirects
- **Scale:** 100M URLs shortened per day
- **Read/Write Ratio:** 100:1 (more reads than writes)
- **Storage:** 5 years of URL storage

## Capacity Estimation

### Traffic
- **Writes:** 100M URLs/day = 1,157 URLs/second
- **Reads:** 10B redirects/day = 115,700 redirects/second
- **Peak traffic:** 2x average = 231,400 reads/second

### Storage
- **URL record size:** ~500 bytes (original URL + metadata)
- **Daily storage:** 100M × 500 bytes = 50 GB/day
- **5-year storage:** 50 GB × 365 × 5 = 91.25 TB

### Bandwidth
- **Incoming:** 1,157 URLs/sec × 500 bytes = 578.5 KB/sec
- **Outgoing:** 115,700 redirects/sec × 500 bytes = 57.85 MB/sec

## System Design

### High-Level Architecture
```
[Client] → [Load Balancer] → [Web Servers] → [App Servers] → [Database]
                                  ↓
                              [Cache Layer]
                                  ↓
                              [Analytics DB]
```

### API Design

#### Shorten URL
```
POST /api/v1/shorten
{
  "longUrl": "https://example.com/very/long/url",
  "customAlias": "optional",
  "expirationDate": "2026-01-01"
}

Response:
{
  "shortUrl": "https://short.ly/abc123",
  "longUrl": "https://example.com/very/long/url",
  "createdAt": "2025-09-14T10:00:00Z",
  "expirationDate": "2026-01-01T00:00:00Z"
}
```

#### Redirect URL
```
GET /abc123
Response: HTTP 301 Redirect to longUrl
```

#### Analytics
```
GET /api/v1/analytics/abc123
Response:
{
  "shortUrl": "https://short.ly/abc123",
  "totalClicks": 1234,
  "uniqueClicks": 890,
  "clicksByDate": [...],
  "topCountries": [...]
}
```

## Database Design

### URL Mapping Table
```sql
CREATE TABLE urls (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  short_url VARCHAR(7) UNIQUE NOT NULL,
  long_url TEXT NOT NULL,
  user_id BIGINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expiration_date TIMESTAMP,
  INDEX idx_short_url (short_url),
  INDEX idx_user_id (user_id)
);
```

### Analytics Table
```sql
CREATE TABLE url_analytics (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  short_url VARCHAR(7) NOT NULL,
  clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ip_address VARCHAR(45),
  user_agent TEXT,
  country VARCHAR(2),
  INDEX idx_short_url_date (short_url, clicked_at)
);
```

## URL Encoding Strategy

### Base62 Encoding
- Characters: [a-z, A-Z, 0-9] = 62 characters
- 7-character short URL = 62^7 = 3.5 trillion unique URLs
- Algorithm:
  1. Generate unique ID (auto-increment or distributed ID generator)
  2. Convert ID to Base62
  3. Pad to 7 characters if needed

### Example Implementation
```python
def encode_base62(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if num == 0:
        return chars[0]
    
    result = ""
    while num > 0:
        result = chars[num % 62] + result
        num //= 62
    
    return result.rjust(7, chars[0])  # Pad to 7 characters
```

## Scalability Solutions

### Database Scaling
- **Master-Slave replication:** Write to master, read from slaves
- **Horizontal partitioning:** Shard by short_url hash
- **Database per service:** Separate read/write databases

### Caching Strategy
- **Redis/Memcached:** Cache popular short URLs
- **Cache warm-up:** Preload trending URLs
- **TTL:** Set based on URL popularity
- **Write-through cache:** Update cache on new URLs

### Load Balancing
- **Application layer:** Round-robin or least connections
- **Geographic distribution:** CDN for global users
- **Database layer:** Read replicas in multiple regions

## Advanced Features

### Analytics Engine
- **Real-time processing:** Apache Kafka + Stream processing
- **Data warehouse:** Store aggregated analytics data
- **Machine learning:** Detect suspicious patterns, predict trends

### Security Measures
- **Rate limiting:** Prevent abuse (100 requests/minute per IP)
- **URL validation:** Check for malicious URLs
- **HTTPS enforcement:** Secure redirects only
- **Spam detection:** Machine learning-based filtering

### Monitoring & Observability
- **Metrics:** Response time, error rates, cache hit ratio
- **Logging:** Structured logs for debugging
- **Alerting:** SLA violations, high error rates
- **Health checks:** Service availability monitoring

## Technology Stack

### Backend
- **Language:** Java/Python/Go
- **Framework:** Spring Boot/Django/Gin
- **Database:** MySQL/PostgreSQL for metadata, Cassandra for analytics
- **Cache:** Redis/Memcached
- **Message Queue:** Apache Kafka/RabbitMQ

### Infrastructure
- **Cloud:** AWS/GCP/Azure
- **Containers:** Docker + Kubernetes
- **Load Balancer:** AWS ALB/Nginx
- **CDN:** CloudFlare/AWS CloudFront
- **Monitoring:** Prometheus/Grafana/DataDog

## Potential Bottlenecks & Solutions

### Database Hotspots
- **Problem:** Popular URLs causing database load
- **Solution:** Multiple cache layers, read replicas

### Single Point of Failure
- **Problem:** Database master failure
- **Solution:** Master-slave failover, multiple availability zones

### URL Collision
- **Problem:** Same short URL generated twice
- **Solution:** Database unique constraints, retry mechanism

### Cache Stampeding
- **Problem:** Multiple requests for expired cache item
- **Solution:** Lock-based cache refresh, probabilistic early expiration

## Key Learnings

1. **Read-heavy systems benefit greatly from caching**
2. **Database sharding is crucial for write scalability**
3. **Analytics data grows much faster than core data**
4. **Geographic distribution improves user experience**
5. **Rate limiting is essential for preventing abuse**
6. **Monitoring and alerting are critical for production systems**

## Related Systems
- [Content Delivery Network (CDN)](./cdn-design.md)
- [Load Balancer Design](./load-balancer.md)
- [Database Sharding Strategies](./database-sharding.md)
