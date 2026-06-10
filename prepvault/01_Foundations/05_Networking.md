---
type: concept
tags: [foundations, networking]
created: 2024-06-10
---

# Computer Networking Deep Dive

## Overview
Computer Networking is the study of how computers communicate with each other. For a software engineer, networking knowledge is essential for building distributed systems, optimizing web performance, and securing applications.

---

## 1. Network Models

### The OSI Model (7 Layers)
The Open Systems Interconnection (OSI) model is a conceptual framework that describes the functions of a networking system.
1. **Physical Layer**: The physical hardware (cables, hubs, bits).
2. **Data Link Layer**: Node-to-node data transfer (frames, MAC addresses, switches, Ethernet).
3. **Network Layer**: Routing data between different networks (packets, IP addresses, routers).
4. **Transport Layer**: End-to-end communication and error recovery (segments, TCP/UDP).
5. **Session Layer**: Managing sessions between applications.
6. **Presentation Layer**: Data translation, encryption, and compression (SSL/TLS often starts here).
7. **Application Layer**: Interaction with the end-user (HTTP, FTP, SMTP, DNS).

### The TCP/IP Model (4 Layers)
A more practical model used for the modern internet.
1. **Network Access Layer**: Combines OSI layers 1 and 2.
2. **Internet Layer**: Equivalent to OSI layer 3.
3. **Transport Layer**: Equivalent to OSI layer 4.
4. **Application Layer**: Combines OSI layers 5, 6, and 7.

---

## 2. The Network Layer (IP)
The Network Layer is responsible for packet forwarding and routing.
- **IP Addresses**:
    - **IPv4**: 32-bit addresses (e.g., 192.168.1.1). Limited pool.
    - **IPv6**: 128-bit addresses (e.g., 2001:0db8:85a3...). Virtually unlimited.
- **Subnetting & CIDR**: A way to divide a network into smaller, manageable sub-networks. CIDR notation (e.g., /24) defines the network prefix length.
- **NAT (Network Address Translation)**: Allows multiple devices on a private network to share a single public IP address.
- **Routing**: The process of selecting a path for traffic in a network or between or across multiple networks.

---

## 3. The Transport Layer (TCP & UDP)

### TCP (Transmission Control Protocol)
TCP is connection-oriented and provides reliable, ordered delivery of data.
- **Three-Way Handshake**:
    1. Client sends **SYN**.
    2. Server sends **SYN-ACK**.
    3. Client sends **ACK**.
- **Reliability mechanisms**: Sequence numbers, acknowledgments (ACKs), and retransmission of lost packets.
- **Flow Control**: Prevents the sender from overwhelming the receiver using a **Sliding Window**.
- **Congestion Control**: Prevents the sender from overwhelming the network (Slow Start, Congestion Avoidance).

### UDP (User Datagram Protocol)
UDP is connectionless and provides "best-effort" delivery.
- **Characteristics**: Fast, low overhead, no guarantees on order or delivery.
- **Use Cases**: Video streaming, online gaming, DNS, VoIP.

---

## 4. Application Layer Protocols

### HTTP/HTTPS
The protocol of the World Wide Web.
- **HTTP Methods**: GET (read), POST (create), PUT (update), DELETE (delete), PATCH (partial update).
- **Status Codes**:
    - 2xx: Success (200 OK, 201 Created).
    - 3xx: Redirection (301 Moved Permanently, 304 Not Modified).
    - 4xx: Client Error (400 Bad Request, 401 Unauthorized, 404 Not Found).
    - 5xx: Server Error (500 Internal Server Error, 503 Service Unavailable).
- **HTTPS**: HTTP over SSL/TLS. Provides encryption, data integrity, and authentication.
- **HTTP Versions**:
    - **HTTP/1.1**: Persistent connections but suffers from Head-of-Line (HoL) blocking.
    - **HTTP/2**: Multiplexing (multiple requests over one TCP connection), header compression (HPACK), server push.
    - **HTTP/3**: Uses **QUIC** (over UDP) to eliminate TCP HoL blocking and improve connection migration.

### DNS (Domain Name System)
The "phonebook" of the internet.
- **Hierarchy**: Root servers -> TLD servers (.com, .org) -> Authoritative Name Servers.
- **Record Types**:
    - **A**: Maps domain to IPv4.
    - **AAAA**: Maps domain to IPv6.
    - **CNAME**: Alias (one domain to another).
    - **MX**: Mail exchange server.
    - **TXT**: Arbitrary text (used for verification).

---

## 5. Modern Networking Components

### Load Balancers
Distributes incoming traffic across a group of backend servers.
- **Sticky Sessions**: Ensuring a user stays on the same server.
- **Health Checks**: Automatically removing failed servers from the rotation.

### Content Delivery Networks (CDN)
A system of distributed servers that deliver web content based on the geographic location of the user.
- **Benefits**: Reduced latency, improved load times, reduced bandwidth costs, protection against traffic spikes.

### API Gateways
An API management tool that sits between a client and a collection of backend services.
- **Functions**: Authentication, rate limiting, request routing, protocol translation.

---

## 6. Networking Security
- **Firewalls**: Monitors and controls incoming and outgoing network traffic based on security rules.
- **Proxy vs. Reverse Proxy**:
    - **Proxy**: Sits in front of clients to hide their identity or filter traffic.
    - **Reverse Proxy**: Sits in front of servers to provide load balancing, caching, and SSL termination.
- **VPN (Virtual Private Network)**: Creates a secure, encrypted "tunnel" over a public network.

---

---

## 7. Deep Dive: Key Protocols

### The SSL/TLS Handshake (HTTPS)
1. **Client Hello**: Client sends supported SSL/TLS versions, cipher suites, and a random number.
2. **Server Hello**: Server chooses the best SSL/TLS version and cipher suite, sends its digital certificate (containing its public key) and another random number.
3. **Authentication**: Client verifies the server's certificate with a Certificate Authority (CA).
4. **Premaster Secret**: Client generates a third random number, encrypts it with the server's public key, and sends it to the server.
5. **Session Keys**: Both parties generate session keys from the three random numbers. These are symmetric keys used for the remainder of the session.
6. **Finished**: Both send encrypted messages confirming the handshake is complete.

### TCP Congestion Control
Congestion control prevents the sender from overwhelming the network.
- **Tahoe**: Simple. Uses Slow Start (exponential growth) and Congestion Avoidance (linear growth). If a timeout occurs, it drops the window size back to 1.
- **Reno**: Adds "Fast Recovery." If three duplicate ACKs are received, it assumes a packet was lost but the network is still mostly functional. It reduces the window size by half instead of dropping to 1.
- **BBR (Bottleneck Bandwidth and Round-trip propagation time)**: A modern algorithm from Google that focuses on maximizing throughput and minimizing delay rather than reacting only to packet loss.

---

## Role-Specific Applications
- **[[02_Role_Tracks/02_Frontend_Engineer|Frontend]]**: Optimizing asset loading (HTTP/2, CDNs), managing browser cache, understanding CORS (Cross-Origin Resource Sharing), using WebSockets for real-time features.
- **[[02_Role_Tracks/03_Backend_Engineer|Backend]]**: Implementing secure REST/gRPC APIs, managing server-to-server communication, configuring reverse proxies (Nginx/HAProxy), optimizing database connection pooling.
- **[[02_Role_Tracks/04_ML_Engineer|ML/Data]]**: Moving large datasets over the network (S3, HDFS), low-latency model serving, distributed computing (Spark/Ray communication).
- **[[02_Role_Tracks/05_DevOps_Engineer|DevOps]]**: Configuring VPCs, subnets, and security groups, managing DNS and SSL certificates, monitoring network performance and security (WAF, DDoS protection).
- **[[02_Role_Tracks/06_Data_Engineer|Data Engineering]]**: Managing data ingestion pipelines over the network, optimizing data transfer throughput, handling API rate limits.
- **[[02_Role_Tracks/07_Product_Manager|Product Management]]**: Understanding network-related product constraints (latency, bandwidth), evaluating CDN and cloud provider tradeoffs.

## Related Topics
- [[01_Foundations/01_DSA|DSA]]
- [[01_Foundations/03_System_Design|System Design]]
- [[01_Foundations/04_Operating_Systems|Operating Systems]]
- [[02_Role_Tracks/01_General_SWE|General SWE Track]]

## Resources
- [Computer Networking: A Top-Down Approach (Kurose & Ross)](https://gaia.cs.umass.edu/kurose_ross/index.php)
- [High Performance Browser Networking (Ilya Grigorik)](https://hpbn.co/)
- [MDN: How the Web Works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)