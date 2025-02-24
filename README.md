# 🔍 Basic Port Scanner

A Python-based **Port Scanner** that scans a given IP address over a range of ports to find **open ports** and report the results.

---

## ⚙️ Core Functionality

The script scans a target **IP address** and a range of ports to identify open ports.

### 🖥️ **User Input:**
- **Target IP Address** (e.g., `192.168.1.1`)  
- **Port Range** (e.g., `20-100`)  

### 🔄 **Scanning Logic:**
- Connects to each port in the specified range using **Python sockets**.  
- **Open ports** are reported if a connection is successful.  
- **Closed ports** are ignored.  

---

## 🚨 Error & Input Handling

### ❌ **Invalid IP Address:**
- Validates the IP address format and checks if it is reachable.  
- If invalid or unreachable, it displays:  
  ```
  [-] The IP address {target_ip} is not reachable or does not exist.
  ```

### ❌ **Invalid Port Range:**
- Ensures the user inputs a **valid numeric range** (e.g., `20-80`).  
- Displays an error if the range is invalid.

### ❌ **Unreachable Host:**
- **Pings** the target IP to check if the host is online.  
- Stops the scan if the host is down.

---

## 📋 Output

### ✅ **Open Ports:**  
If open ports are found, the script displays:
```
[+] Port 22 is open
[+] Port 80 is open
```

### ⚠️ **No Open Ports:**  
If no open ports are found, it notifies:
```
[!] No open ports found in the given range.
```

### ⚡ **Invalid Inputs:**  
- Provides clear, user-friendly error messages for invalid inputs.

---

## 🚀 How to Run the Script

### 📁 **1. Prepare the Script**
1. Open your code editor (**VS Code**, **PyCharm**, etc.).  
2. Paste the code into a file named:  
   ```
   port_scanner.py
   ```

### 🖥️ **2. Run the Script**
1. Open **Terminal** or **Command Prompt**.  
2. Navigate to the script's directory:  
   ```bash
   cd /path/to/your/script/
   ```  
3. Run the script:  
   ```bash
   python port_scanner.py
   ```

### 📊 **3. Follow the Prompts**
1. Enter the **IP address** and **port range** when asked.  
2. View the scan results directly in the terminal! 🔍  

