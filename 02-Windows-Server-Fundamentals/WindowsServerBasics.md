# 🖥️ Chapter 2: Windows Server 2022 & Infrastructure

## 1. What is Windows Server?
Windows Server is an **Enterprise-class operating system** by Microsoft[cite: 12]. It is designed to provide services to multiple users simultaneously and offers administrators full control over data, applications, and networks[cite: 12]. It serves as the core platform for IT infrastructure in organizations[cite: 12].

---

## 2. Workgroup vs. Domain
Understanding the transition from a local to a centralized network is key for IT management.

### 🏠 Workgroup (Peer-to-Peer)
*   **Local Management:** Each computer has its own security database and local user accounts[cite: 12].
*   **Login Requirements:** To log on to a computer, you must have a specific account defined on that machine[cite: 12].
*   **Scope:** Typically used for small networks with fewer than 20 computers[cite: 12].

### 🏢 Domain (Centralized Management)
*   **Active Directory:** Uses a centralized database stored on **Domain Controllers (DC)** to control security and permissions for all computers[cite: 12].
*   **Consistency:** Allows administrators to enforce uniform settings across the network[cite: 12].
*   **Scalability:** Supports thousands of computers and provides higher security for large organizations[cite: 12].

---

## 3. Active Directory (AD) Core Technologies
Active Directory provides various network services to manage identities and resources[cite: 12]:

*   **LDAP:** A protocol used to query and modify directory services over TCP/IP (Port 389)[cite: 12].
*   **Kerberos:** The default authentication protocol, allowing secure identity proofing over non-secure networks[cite: 12].
*   **Single Sign-On (SSO):** Enables users to log in once and access multiple resources[cite: 12].
*   **DNS Integration:** AD uses DNS-based naming to organize resources like users, groups, and printers[cite: 12].

---

## 4. Logical Structure & Objects


### Organizational Units (OUs)
OUs are used to organize objects within a domain and minimize the number of domains needed[cite: 12]. They can contain users, groups, computers, and even other OUs[cite: 12]. OUs are typically created based on geography, roles, or departments and are used to deploy **Group Policies**[cite: 12].

### AD Objects & Identifiers
*   **Objects:** Represent network resources like users or printers, defined by a set of attributes[cite: 12].
*   **GUID/SID:** Every object is assigned a unique 128-bit number (SID or GUID)[cite: 12]. If a user changes their name, their permissions remain intact because they are linked to the GUID, not the name[cite: 12].

---

## 5. User Accounts & Security Groups
*   **User Accounts:** Used for **Authentication** (identity), **Authorization** (access level), and **Auditing** (tracking actions)[cite: 12].
    *   **UPN:** Email-style login (`Username@domainname`)[cite: 12].
    *   **SAMAccountName:** Legacy login (`DomainName\Username`), limited to 20 characters[cite: 12].
*   **Computer Accounts:** Required for each Windows machine to authenticate and access domain resources[cite: 12].
*   **Security Groups:** Lists of accounts used to simplify the assignment of rights and permissions[cite: 12]. 
*   **Distribution Groups:** Used solely for email distribution; they cannot be assigned security permissions[cite: 12].
