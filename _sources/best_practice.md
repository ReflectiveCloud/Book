# Best Practices

_Modeled on the [CryoCloud Best Practices](https://book.cryointhecloud.com/content/hub_best_practices.html)_

---

## Server Launch Configuration

After logging in and clicking `Launch server`, there are two options to select: `environment` and `resource allocation`.

### **Environment Selection**

- **Select Pangeo Notebook Image** to start a Python environment with a set of common geoscience packages including those from the [Pangeo](https://pangeo.io/#ecosystem) ecosystem
- This is the environment required to run our example notebooks

### **Resource Allocation**

- **Please select the smallest resource** (RAM and CPUs) which can meet your needs for a given workflow
- The higher resource options cost us significantly more
- You can see your memory usage at the bottom of the screen when working in a notebook

---

## Cost Management

### **Server Shutdown**

To avoid unnecessary costs, please shutdown your server when you finish on the Hub:

1. `File` > `Hub Control Panel` > `Stop Server`
2. Once the `Stop Server` button disappears, your server has stopped
3. Click `Log Out`
4. Close that browser tab before starting the server again to prevent errors

### **Automatic Shutdown**

The hub will automatically shut off after **90 minutes without activity**.

---

## ⏱️ Performance Notes

- **Server startup** can take a minute or two when first launching
- **Package installations** using pip (`% pip install packagename`) only last for the duration of that session

---

## 💾 Storage Management

### **File Storage Guidelines**

- **Keep saved files in your home directory to a minimum**
- Let us know if you need to store more than around **10GB**
- We recommend workflows which:
  - Stream data without downloading to a file, OR
  - Automatically delete files after using them

### **Check Usage**

You can check total usage by running the following command in a terminal:

```bash
du -hs --exclude="shared*" ~/
```

---

## Intended Use

### **Primary Purpose**

This resource is principally intended for **analysis of climate model simulations of SRM simulations**.

### **Not Intended For**

❌ **Running climate models in the cloud** - This would take orders of magnitude more computing resources.

---

## Quick Reference

| Action               | Steps                                                         |
| -------------------- | ------------------------------------------------------------- |
| **Start Server**     | Login → Launch Server → Select Environment → Select Resources |
| **Stop Server**      | File → Hub Control Panel → Stop Server → Log Out              |
| **Check Storage**    | Run `du -hs --exclude="shared*" ~/` in terminal               |
| **Install Packages** | Use `% pip install packagename` (session-only)                |

---

_Following these best practices helps ensure efficient resource usage and cost management for all users._
