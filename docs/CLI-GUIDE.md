# 🖥️ CLI Guide - Command Line Interface

Complete reference for PwnStore CLI commands.

---

## 📦 Installation

```bash
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

Verify installation:
```bash
which pwnstore    # Should show: /usr/local/bin/pwnstore
```

---

## 📖 Basic Commands

### List All Plugins
Browse the entire catalog (auto-categorized by type):
```bash
pwnstore list
```

### Search for Plugins
Find plugins by name or description:
```bash
pwnstore search discord
pwnstore search gps
pwnstore search display
```

### Get Plugin Info
View detailed information about a specific plugin:
```bash
pwnstore info <plugin_name>
```

Shows:
- Author
- Version
- Description
- Category
- Source URL
- Download URL

---

## ⚡ Install & Uninstall

### Install a Plugin
Downloads the plugin and automatically:
- Places it in your custom plugins directory (read from `config.toml`)
- Adds `enabled = true` to your `config.toml`

```bash
sudo pwnstore install <plugin_name>
```

**Example:**
```bash
sudo pwnstore install discord
```

**Smart Hints:**  
If the plugin requires additional config (like API keys), PwnStore will print the required settings after installation.

### Uninstall a Plugin
Removes the plugin file and disables it in config:
```bash
sudo pwnstore uninstall <plugin_name>
```

---

## 🔄 Updates

### Update Installed Plugins
Check for and apply updates to your installed plugins:
```bash
sudo pwnstore update
```

### Upgrade PwnStore Itself
Update PwnStore to the latest version:
```bash
sudo pwnstore upgrade
```

---

## 📊 Repository Management

### View Plugin Sources
See which GitHub repos are being monitored:
```bash
pwnstore sources
```

Example output:
```
REPOSITORY / SOURCE                                | PLUGINS
-----------------------------------------------------------------
github.com/Sniffleupagus/pwnagotchi_plugins        | 22
github.com/NeonLightning/pwny                      | 12
github.com/AlienMajik/pwnagotchi_plugins           | 10
github.com/wpa-2/Pwnagotchi-Plugins                | 7
-----------------------------------------------------------------
Total Plugins Indexed: 71
```

---

## 🎯 Common Workflows

### Installing Your First Plugin
```bash
# 1. Browse available plugins
pwnstore list

# 2. Get details about a plugin
pwnstore info discord

# 3. Install it
sudo pwnstore install discord

# 4. Restart Pwnagotchi
sudo systemctl restart pwnagotchi

# 5. Check it loaded
pwnlog
```

### Keeping Everything Updated
```bash
# Update installed plugins
sudo pwnstore update

# Upgrade PwnStore itself
sudo pwnstore upgrade

# Restart Pwnagotchi
sudo systemctl restart pwnagotchi
```

### Finding a Specific Type of Plugin
```bash
# Search for GPS plugins
pwnstore search gps

# Search for display plugins
pwnstore search display

# Search for social plugins
pwnstore search discord telegram
```

---

## 🔧 Advanced Usage

### Check Installed Plugins
List what's currently in your plugins directory:
```bash
ls -la $(grep custom_plugins /etc/pwnagotchi/config.toml | cut -d'"' -f2)
```

### View Plugin Config
See what PwnStore added to your config:
```bash
grep -A 5 "plugins.<plugin_name>" /etc/pwnagotchi/config.toml
```

---

## 🐛 Troubleshooting

### Command Not Found
```bash
# Reinstall PwnStore
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

### Install Fails

**Check network connectivity:**
```bash
ping -c 3 github.com
```

**Try manual install** (check your `custom_plugins` path in `/etc/pwnagotchi/config.toml` first):
```bash
cd <your_custom_plugins_directory>
sudo wget <plugin_raw_url>
```

### Plugin Won't Load
```bash
# Check it's enabled
grep <plugin_name> /etc/pwnagotchi/config.toml

# Check Pwnagotchi logs
pwnlog

# Run in debug mode
sudo systemctl stop pwnagotchi
sudo pwnagotchi --debug
```

---

## 💡 Pro Tips

1. **Always use sudo** for install/uninstall operations
2. **Update regularly** to get new plugins: `sudo pwnstore update`
3. **Check logs** after installing: `pwnlog`
4. **Read plugin info** before installing: `pwnstore info <n>`
5. **Restart Pwnagotchi** after installing plugins
6. **⚠️ NEVER run** `sudo apt-get upgrade` (breaks Pwnagotchi!)
7. **✅ OK to run** `sudo apt-get update`

---

## 📚 Related Guides

- [Web UI Guide](WEB-UI-GUIDE.md) - Use the browser interface
- [Troubleshooting](TROUBLESHOOTING.md) - Fix common issues
- [FAQ](FAQ.md) - Quick answers

---

**[← Back to Main README](../README.md)**
