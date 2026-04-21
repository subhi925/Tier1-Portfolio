# 🚀 Tier 1 & 2 System Administration Portfolio
**By Subhi Mohammed Hamed**

This repository serves as a professional documentation of my technical journey in building, managing, and securing Enterprise-grade IT infrastructures. It covers a full-stack of System Administration skills including Windows Server, Networking, Linux, and Automation.

---

## 🛠️ Phase 1: Windows Server 2022 & Active Directory Infrastructure

### **Objective**
To transform a standalone server into a centralized Identity and Access Management (IAM) hub using Microsoft Active Directory. This forms the foundation for managing users, computers, and security policies across an enterprise network.

### **Technical Stack & Environment**
* **Virtualization:** VMware Workstation Pro.
* **Operating System:** Windows Server 2022 Standard (Desktop Experience).
* **Network Role:** Primary Domain Controller (PDC).
* **Core Services:** AD DS (Active Directory Domain Services), DNS (Domain Name System).

### **Key Achievements & Implementation Details**

1. **Virtualization Optimization:**
   * Configured the VM environment with **VMware Tools** to ensure high-performance driver support, seamless mouse integration, and shared clipboard functionality.
2. **Enterprise Naming Conventions:**
   * Performed a system **Rename** to `DC-SRV-01` (Host: DC) prior to promotion, adhering to professional naming standards for server identification.
3. **Active Directory Promotion:**
   * Successfully promoted the server to a **Domain Controller** for the forest: `SUBHCOPM.LOCAL`.
   * Installed and configured the **NTDS Database** and **SYSVOL** folders for centralized data storage and policy replication.
4. **Network Infrastructure:**
   * Configured the **DNS Role** to handle internal name resolution, ensuring that all domain objects can communicate via Hostnames rather than just IP addresses.

### **Visual Documentation**

#### 🔐 Domain Authentication Success
The screenshot below confirms the successful promotion. The system now authenticates users against the `SUBHCOPM` domain rather than the local machine database.

<img width="1919" height="1079" alt="Screenshot 2026-04-08 140400" src="https://github.com/user-attachments/assets/0e69c532-e41c-4fdb-abef-9d94ae35fa26" />


#### 🟢 System Health & Roles
A look at the **Server Manager Dashboard** showing all core roles (AD DS, DNS, File Services) in a healthy, "Green" state.

<img width="1917" height="1079" alt="Screenshot 2026-04-08 140612" src="https://github.com/user-attachments/assets/274fcada-ec0e-4270-b331-b7bc8ec483ca" />

---
## 🖥️ Phase 2: Workstation Integration & Identity Management

### **Objective**
Integrating client machines into the managed environment and establishing a structured hierarchy for organizational assets.

### **Key Achievements**
1. **Domain Join Operations:**
   * Performed a **Standard Join** for a Windows Client, ensuring correct DNS pointing to `DC-SRV-01`.
   * Executed an **Offline Domain Join (ODJ)** using the `djoin` utility, demonstrating the ability to provision machines without direct network connectivity to the DC.
2. **Active Directory Logical Structure:**
   * Designed and implemented an **Organizational Unit (OU)** hierarchy to separate Users, Computers, and Service Accounts.
   * Created and managed **Active Directory Objects** (Users, Security Groups) to enforce the Principle of Least Privilege (PoLP).

### **Visual Documentation (Phase 2)**
<img width="1901" height="1074" alt="Screenshot 2026-04-21 171631" src="https://github.com/user-attachments/assets/9e402012-eb36-4b1d-9b01-7633b5fa3acd" />
<img width="980" height="879" alt="Screenshot 2026-04-21 171150" src="https://github.com/user-attachments/assets/d90240df-3936-44f5-b98d-b7bde0b677f6" />
<img width="1427" height="997" alt="Screenshot 2026-04-21 170243" src="https://github.com/user-attachments/assets/a3089be9-d551-4bf4-be9d-0ba7e4c3e4e3" />

---
## 🛠️ Troubleshooting & Technical Insights
* **Issue:** DNS Name Resolution failure during Domain Join.
* **Resolution:** Identified that the workstation was using IPv6 DNS from the local router. Manually configured the primary DNS to the DC's static IPv4 address, ensuring successful communication with the Domain Controller.
---


## 📈 Project Status & Roadmap
- [x] **Phase 1:** Windows Server 2022 & Domain Promotion.
- [x] **Phase 2:** Workstation Integration (Domain Join) & User Management.
- [ ] **Phase 3:** Group Policy Objects (GPO) & Security Hardening.
- [ ] **Phase 4:** Linux Server Integration (Ubuntu Server in AD).
- [ ] **Phase 5:** Automation with PowerShell (Bulk User Creation).

---
📫 **Contact:** [subhihamed88@gmail.com/[LinkedIn Link](https://www.linkedin.com/in/subhi-mouhammed-hamed-223410360/)]
