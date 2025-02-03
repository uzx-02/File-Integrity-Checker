# **File Integrity Checker**

**Company:** CODTECH IT SOLUTIONS  

**Name:** Uzair Shaikh  

**Intern ID:** CT12OUP  

**Domain:** Cyber Security & Ethical Hacking  

**Duration:** 8 Weeks  

**Mentor:** Neela Santosh

### **Task Description:**

In this task, I was required to build a tool that monitors changes in files by calculating and comparing hash values to ensure file integrity. The deliverable was a Python script utilizing libraries like `hashlib` to achieve this functionality. The task involved detecting modifications in files, keeping track of their hashes, and logging changes to notify the user of any alterations in monitored files.

### **Tools Used:**

- **Programming Language:** Python
- **Libraries/Modules:**  
  - `xxhash`: Used for fast hashing of files. It’s known for being faster than traditional hashing algorithms like MD5 and SHA.
  - `hashlib`: Primarily used for hashing in the script, though I focused on `xxhash` due to its faster computation.
  - `logging`: Used for logging file integrity checks, hash comparisons, and any errors encountered.
  - `os`: Utilized for file handling and checking file existence.
  - `json`: Used to store and load hash values of files.
  - `concurrent.futures.ThreadPoolExecutor`: For performing file integrity checks in parallel, enhancing performance when monitoring multiple files.

- **IDE:** Visual Studio Code (VS Code) was the IDE used to write, test, and debug the Python script.

### **Task Implementation:**

The main goal of this task was to create a system that checks files for modifications by calculating their hash values, comparing them with previously stored hashes, and logging any changes. Here’s how I approached the problem:

1. **Hash Calculation:**  
   The `calculate_file_hash` function reads the file and generates its hash using the `xxhash` algorithm. The file is read in chunks to avoid memory overload when dealing with large files, and any issues, such as a missing file, are logged.

2. **Storing and Loading Hashes:**  
   File hash values are stored in a JSON file (`file_hashes.json`). This ensures that previously computed hashes are available for future comparisons. Functions `load_hashes` and `save_hashes` handle reading and writing this JSON file.

3. **Monitoring File Integrity:**  
   The `monitor_file_integrity` function compares the hash of each file against the stored hash. If the hashes match, no changes are detected. If they differ, it indicates the file has been modified, and the change is logged with both the previous and current hash values. New files are added to the monitoring system.

4. **Parallel Processing:**  
   The script utilizes `ThreadPoolExecutor` from `concurrent.futures` for parallel processing, allowing the monitoring of multiple files simultaneously. This improves performance when scaling the tool to monitor large numbers of files.

5. **Logging:**  
   Instead of simple `print()` statements, the script uses `logging` to generate detailed logs. These logs provide information on file additions, hash comparisons, and any encountered errors, offering better traceability and easier troubleshooting.

### **Application of the Tool:**

This file integrity checker is highly applicable in scenarios where ensuring that files remain unaltered is critical. Potential applications include:

* **Data Security:**  
  Monitoring sensitive documents to detect unauthorized changes and maintain confidentiality.

* **Backup Systems:**  
  Verifying the integrity of backup files, ensuring they haven’t been altered or corrupted over time.

* **Software Deployment:**  
  Ensuring that deployed software files or configurations haven’t been tampered with after deployment.

* **File System Auditing:**  
  Auditing files in sensitive environments to detect any modifications, crucial for industries like finance or legal where file integrity is paramount.

### **Output Achieved:**

The final output of the task was a Python script that effectively monitors changes in files by comparing their hash values. The script generates a log file that tracks file additions, modifications, and hash comparisons, allowing users to ensure the integrity of important files. For example, the log generated from running the script on `example_file.txt` displayed the following entries:

```
2025-02-03 20:10:14,913 - INFO - New file added for monitoring: example_file.txt
2025-02-03 20:15:27,135 - WARNING - File modified: example_file.txt
2025-02-03 20:15:27,135 - WARNING - Stored hash: 095b5421daef4e24
2025-02-03 20:15:27,135 - WARNING - Current hash: c624c7bec2766ff9
```

This log indicates that the file `example_file.txt` was added for monitoring and later modified. The old and new hash values were successfully captured in the log.

### **Conclusion:**

By utilizing the specified tools and following a structured approach, I created a Python-based file integrity checker that meets the task's requirements. The script can monitor a wide range of files and is scalable to handle multiple files concurrently, making it a robust solution for file integrity management. The use of parallel processing and logging ensures both performance and traceability.
