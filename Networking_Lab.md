# Tier 1 Support - Knowledge Base 🛠️

## Chapter 1: Networking Basics
In this chapter, I learned how to identify network settings and troubleshoot connectivity.

### Lab 1.1: Local Network Configuration
* **IP Address:** 192.168.68.107
* **Subnet Mask:** 255.255.255.0
* **Default Gateway:** 192.168.68.1

> **Insight:** If the Default Gateway is missing, the computer cannot reach the internet (like WhatsApp or Google) because it doesn't know the "exit door" from the local network.

### Lab 1.2: Connectivity Testing
To verify internet access, I used the `ping` tool to contact Google's DNS (8.8.8.8).

* **Command:** `ping 8.8.8.8`
* **Packets Sent:** 4
* **Packets Received:** 4
* **Packet Loss:** 0%
* **Status:** Success. The computer can reach external networks.
### Lab 1.3: Route Tracing
I used the `tracert` tool to map the path from my computer to Google's DNS.

* **Command:** `tracert 8.8.8.8`
* **Total Hops:** 10
* **First Hop:** 192.168.68.1 (Local Router/Gateway)
* **Insight:** Since the first hop responded correctly, the connection between the PC and the local router is stable.
### Lab 1.4: DNS Resolution
I tested the DNS resolution using the `nslookup` tool to translate a domain name into an IP address.

* **Command:** `nslookup google.com`
* **Resolved IP (IPv4):** 142.250.75.78
* **DNS Server used:** 192.168.1.1
* **Insight:** DNS is critical for users. If DNS fails, users cannot access websites by their names even if they have an active internet connection.
