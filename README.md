# 🛒 PwnStore - The Unofficial Pwnagotchi App Store

**Stop downloading massive ZIP files.** PwnStore is a powerful plugin manager for Pwnagotchi that works both from the **command line** and through a **mobile-friendly web interface**. Browse, install, update, and manage plugins surgically—downloading only the files you need.

[![CLI Version](https://img.shields.io/badge/CLI-v2.5-green)](https://github.com/wpa-2/pwnagotchi-store) [![UI Version](https://img.shields.io/badge/Web_UI-v1.0-blue)](https://github.com/wpa-2/pwnagotchi-store) [![Gallery](https://img.shields.io/badge/Gallery-Live-orange)](https://pwnstore.org/) [![Python](https://img.shields.io/badge/python-3-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPL3-red)](LICENSE)

---

## 📦 Four Ways to Use PwnStore

PwnStore gives you **four different interfaces** - use whichever fits your workflow:

### 🖥️ 1. CLI Tool (Command Line)
Perfect for **SSH access** and **automation**. The core engine that handles all plugin management.
- Direct terminal control
- Scriptable and automatable
- Full debugging output
- Works via SSH from anywhere

### 🌐 2. Web UI Plugin (On-Device Browser Interface)
Perfect for **mobile users** and **visual browsing**. One-click installs from your phone or desktop browser.
- Access at: `http://<your-pwnagotchi-ip>/plugins/pwnstore_ui/`
- Touch-optimized interface
- Real-time install/uninstall
- No SSH required

### 🌍 3. GitHub Pages Gallery (Public Web Catalog)
Perfect for **browsing and discovering** plugins before you install. View the full catalog online.
- Browse at: **[https://pwnstore.org/](https://pwnstore.org/)**
- View all 66+ plugins with descriptions
- Filter by category
- Generate install commands
- No Pwnagotchi connection needed

### 🛠️ 4. Interactive Troubleshooting Wizard
Perfect for **solving problems** and **getting help** when things go wrong. A step-by-step wizard that guides you through common issues.
- Access at: **[https://pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)**
- Interactive decision tree - no searching docs
- Click-to-copy commands
- Platform-specific guides (Windows/Mac/Linux)
- Version detection (v2.9.5.4+ vs older)
- Mobile-friendly interface

![Troubleshoot Wizard](images/c.png)

**Common issues the wizard solves:**
- 🔌 **Connection Problems** - USB, Ethernet, SSH setup for all platforms
- ⚙️ **Configuration** - How to edit config.toml, enable plugins, fix syntax errors
- 🖥️ **Display Issues** - 80+ display types, rotation fixes, hardware troubleshooting
- 🔌 **Plugin Problems** - Install, update, debug plugins
- 🔑 **SSH Keyless Setup** - Passwordless access for Windows/Mac/Linux
- ❓ **General Help** - Commands, file locations, common tips

**All interfaces use the same plugin registry** - consistent experience everywhere!

### 📊 Quick Comparison

| Feature | CLI Tool | Web UI Plugin | GitHub Pages | Troubleshoot Wizard |
|---------|----------|---------------|--------------|---------------------|
| **Access** | SSH required | Browser on device | Any browser, anywhere | Any browser, anywhere |
| **Install Plugins** | ✅ Yes | ✅ Yes | ❌ View only | ❌ Guides only |
| **Uninstall Plugins** | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Browse Catalog** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Troubleshoot Issues** | ⚠️ Manual | ⚠️ Manual | ❌ No | ✅ Interactive wizard |
| **Search/Filter** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Category-based |
| **Mobile Friendly** | ❌ Terminal only | ✅ Touch optimized | ✅ Responsive | ✅ Touch optimized |
| **Works Offline** | ✅ Yes* | ✅ Yes* | ❌ Needs internet | ✅ Standalone HTML |
| **Pwnagotchi Needed** | ✅ Required | ✅ Required | ❌ Browse without device | ❌ No device needed |

*Requires internet to download plugins, but can list already installed ones offline.

---

## ✨ Features

### Core Features (CLI + UI)
* **📦 Lightweight Registry:** Queries a remote JSON manifest; doesn't bloat your device
* **🎯 Surgical Installs:** Downloads single `.py` files or extracts specific plugins from archives automatically
* **🧠 Smart Config Hints:** Scans plugin code and suggests exact config.toml entries
* **⚡ Auto-Config:** Automatically adds `enabled = true` so plugins load on restart
* **🔄 Self-Updating:** Update the tool itself and bulk-upgrade installed plugins
* **🏷️ Auto-Categorized:** GPS, Social, Display, Hardware, Attack, System

### Web UI Exclusive Features
* **📱 Mobile-Optimized:** Touch-friendly interface works perfectly on phones
* **🎨 Retro Terminal Theme:** Classic Pwnagotchi green-on-black aesthetic
* **✨ One-Click Installs:** No SSH needed - just tap [Install]
* **🔍 Live Search & Filters:** Find plugins instantly by name, category, or description
* **✅ Real-Time Status:** Installed plugins show green ✓ badge
* **💬 Toast Notifications:** Visual feedback for all actions

### Troubleshooting Wizard Features
* **🐾 Winking Pwny:** Animated mascot guides you through problems
* **🎯 Smart Decision Trees:** Answer questions to find the right solution
* **📋 Step-by-Step Guides:** Clear instructions for every issue
* **📋 Click-to-Copy Commands:** All commands copy with one click
* **🚨 Critical Warnings:** Red pulsing alerts for common mistakes (apt-get upgrade!)
* **🖥️ Display Selector:** Dropdown with 80+ display types, auto-generates config

---

## 🚀 Installation

### Step 1: Install CLI Tool (Required)

SSH into your Pwnagotchi and run:

```bash
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

### Step 2: Install Web UI Plugin (Optional but Recommended)

```bash
# Download the UI plugin
sudo wget -O /usr/local/share/pwnagotchi/custom-plugins/pwnstore_ui.py https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore_ui.py

# Enable in config
sudo nano /etc/pwnagotchi/config.toml
```

Add these lines:
```
[main.plugins.pwnstore]
enabled = true

[main.plugins.pwnstore_ui]
enabled = true

```

Restart Pwnagotchi:
```bash
sudo systemctl restart pwnagotchi
```

Then open in your browser: `http://<your-pwnagotchi-ip>/plugins/pwnstore_ui/`

### Step 3: Access Troubleshooting (No Install Needed!)

Just visit: **[https://pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)**

Works on any device, any browser. Perfect for when you can't connect to your Pwnagotchi!

---

## 📖 Usage

### 🖥️ CLI Commands

#### List & Search
Browse available plugins (auto-categorized by GPS, Social, Display, etc.):
```bash
pwnstore list
pwnstore search discord
pwnstore sources          # Show repository sources
```

#### Get Plugin Details
View author, version, description, and source URL:
```bash
pwnstore info <plugin_name>
```

#### Install a Plugin
Downloads, enables, and scans for required settings:
```bash
sudo pwnstore install <plugin_name>
```
**Smart Hint:** If the plugin requires specific settings (like API keys), PwnStore will print them after installation.

#### Manage Updates
```bash
sudo pwnstore update      # Plugin updates
sudo pwnstore upgrade     # Pwnstore upgrades
```

#### Uninstall a Plugin
Removes the file and disables it in `config.toml`:
```bash
sudo pwnstore uninstall <plugin_name>
```

---

### 🌐 Web UI Interface

Access the store at: `http://<your-pwnagotchi-ip>/plugins/pwnstore_ui/`

**From Desktop:**
1. Open your browser
2. Navigate to the URL above
3. Browse the plugin gallery
4. Click [Install] on any plugin
5. Wait for success notification
6. Restart Pwnagotchi

**From Mobile:**
1. Connect to Pwnagotchi's WiFi
2. Open browser (Safari, Chrome, etc.)
3. Visit the plugins page
4. Tap [Install] - optimized for touch
5. Get instant visual feedback
6. No SSH needed! 📱

#### Web UI Features:
- 🔍 **Live Search:** Type to filter plugins instantly
- 🏷️ **Category Filters:** Display, GPS, Social, Hardware, Attack, System
- ✓ **Status Badges:** See which plugins are already installed
- ℹ️ **Quick Info:** Tap info button for plugin details
- 🗑️ **One-Click Uninstall:** Remove plugins just as easily

---

### 🛠️ Troubleshooting Wizard

**Access:** **[https://pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)**

Can't connect to your Pwnagotchi? Display not working? Plugin won't install? The troubleshooting wizard has you covered:

**How to Use:**
1. Visit the wizard in any browser
2. Click the category that matches your problem
3. Answer a few simple questions
4. Get step-by-step instructions
5. Copy commands with one click
6. Follow the guide to fix your issue

**Perfect for:**
- 🆕 **New users** setting up their first Pwnagotchi
- 🔧 **Troubleshooting** connection, display, or plugin issues
- 📱 **Mobile users** who need help while working on their device
- 🤔 **Anyone stuck** who doesn't want to search through docs

---

## 🌐 Public Web Gallery (Browse Online)

**Access anywhere:** **[https://pwnstore.org/](https://pwnstore.org/)**

This is a **public catalog** you can browse from any device, even without your Pwnagotchi nearby:

### What You Can Do:
- 📖 **Browse all plugins** with descriptions and categories
- 🔍 **Search and filter** by category (Display, GPS, Social, Hardware, Attack, System)
- 📋 **Copy install commands** - click any plugin to get the command
- 🔗 **View GitHub sources** - direct links to plugin repositories
- 📱 **Access from anywhere** - desktop, tablet, phone (no Pwnagotchi needed)

### How to Use It:
1. Visit [pwnstore.org](https://pwnstore.org/)
2. Browse or search for plugins
3. Click on a plugin card to see install command
4. Copy the command (e.g., `sudo pwnstore install discord`)
5. SSH into your Pwnagotchi and paste the command

**Perfect for:** Planning your plugin setup, discovering new plugins, or sharing the catalog with others!

---

## ⚙️ How It Works

### The Architecture

```
┌─────────────────────────────────────────────────────────┐
│              User Interface Layer                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. CLI Tool (pwnstore)                                 │
│     • Terminal commands                                 │
│     • SSH access required                               │
│     • Direct control                                    │
│                                                         │
│  2. Web UI Plugin (pwnstore_ui.py)                      │
│     • Browser on Pwnagotchi (10.0.0.2/plugins/...)     │
│     • Mobile-friendly, one-click installs               │
│     • Calls CLI tool via subprocess                     │
│                                                         │
│  3. GitHub Pages Gallery                                │
│     • Public catalog (pwnstore.org)                     │
│     • Browse from anywhere                              │
│     • View-only, generates commands                     │
│                                                         │
│  4. Troubleshooting Wizard                              │
│     • Public help wizard (pwnstore.org/troubleshoot)    │
│     • Interactive problem-solving                       │
│     • No installation required                          │
│              ↓                                          │
├─────────────────────────────────────────────────────────┤
│           Core Engine (CLI Tool)                        │
│  • Downloads from GitHub                                │
│  • Manages config.toml                                  │
│  • Scans for dependencies                               │
│  • Validates plugins                                    │
│              ↓                                          │
├─────────────────────────────────────────────────────────┤
│        Remote Registry (plugins.json)                   │
│  • 66+ plugins indexed                                  │
│  • 8 repository sources                                 │
│  • Auto-updated via GitHub Actions                      │
│  • Used by all interfaces                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Key Points:**
- **CLI Tool** = The engine (does the actual work)
- **Web UI Plugin** = Steering wheel (calls CLI tool)
- **GitHub Pages** = Window shopping (browse only, then use CLI/UI to install)
- **Troubleshoot Wizard** = Roadside assistance (interactive help when stuck)
- All access the **same plugin registry**

### The Registry System

PwnStore doesn't scan GitHub in real-time (too slow). Instead:

1. **The Builder (`builder.py`):** Scans known plugin repositories (listed in `repos.txt`), categorizes them using keyword logic, and generates a sorted `plugins.json`

2. **The Registry (`plugins.json`):** Hosted in this repository, contains all plugin metadata

3. **The Client (CLI/UI):** Reads the JSON to perform actions

4. **GitHub Actions:** Automatically rebuilds the registry when `repos.txt` is updated

---

## 🤝 Adding New Plugins

Want to add a plugin to the store?

1. **Fork this repository**
2. **Add the plugin's GitHub URL** to `repos.txt`
3. **Submit a Pull Request**
4. **Wait for merge** - the registry will auto-update via GitHub Actions

### Example Addition to `repos.txt`:
```
https://github.com/username/pwnagotchi-plugin-name
```

Once merged, the plugin will appear in both CLI and Web UI automatically!

---

## 📊 Current Statistics

- **66+ plugins** indexed
- **8 repository sources** monitored
- **6 categories:** Display, GPS, Social, Hardware, Attack, System
- **Auto-updated:** Registry rebuilds on every commit

View sources:
```bash
pwnstore sources
```

Output:
```
REPOSITORY / SOURCE                                | PLUGINS
-----------------------------------------------------------------
github.com/Sniffleupagus/pwnagotchi_plugins        | 22
github.com/NeonLightning/pwny                      | 12
github.com/AlienMajik/pwnagotchi_plugins           | 10
github.com/wpa-2/Pwnagotchi-Plugins                | 7
github.com/unitMeasure/pwn-plugins                 | 7
github.com/jayofelony/pwnagotchi-torch-plugins     | 6
github.com/cyberartemio/wardriver-pwnagotchi-plugin | 1
github.com/marbasec/UPSLite_Plugin_1_3             | 1
-----------------------------------------------------------------
Total Plugins Indexed: 66
```

---

## 🆘 Troubleshooting

### Need Help? Use the Interactive Wizard!

**Visit: [https://pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)**

The wizard covers:
- ✅ Connection issues (Windows/Mac/Linux)
- ✅ Configuration problems
- ✅ Display not working
- ✅ Plugin installation issues
- ✅ SSH keyless setup
- ✅ General help and commands

### CLI Tool Issues

**pwnstore command not found:**
```bash
# Reinstall
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

**Install fails:**
```bash
# Check logs
sudo pwnstore install <plugin> --verbose

# Try manual install
cd /usr/local/share/pwnagotchi/custom-plugins/
wget <plugin-url>
```

### Web UI Issues

**Page won't load:**
```bash
# Check plugin is enabled
grep pwnstore_ui /etc/pwnagotchi/config.toml

# Check Pwnagotchi is running
sudo systemctl status pwnagotchi

# Check logs
sudo journalctl -u pwnagotchi | grep pwnstore_ui
```

**Install button doesn't work:**
```bash
# Verify CLI tool is installed
which pwnstore

# Check browser console for errors (F12)
```

**CSRF token errors:**
The latest version includes CSRF protection - make sure you're running the latest `pwnstore_ui.py`

---

## 🎯 Use Cases

### For New Users
**Use: Troubleshooting Wizard** ([pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html))
- Step-by-step setup guides
- Platform-specific instructions
- Copy commands with one click
- Perfect for first-time setup

### For Casual Users
**Use: Web UI Plugin** (`/plugins/pwnstore_ui/`)
- Browse plugins on your phone while connected to Pwnagotchi
- One-click install without SSH knowledge
- Visual feedback with toast notifications
- Perfect for non-technical users

### For Plugin Discoverers
**Use: GitHub Pages Gallery** ([pwnstore.org](https://pwnstore.org/))
- Browse plugins from work/home before buying hardware
- Plan your plugin setup in advance
- Share the catalog with friends
- No Pwnagotchi required to explore

### For Power Users
**Use: CLI Tool** (via SSH)
- Script plugin installations
- Automate updates
- SSH from anywhere
- Full control and debugging info

### For Developers
**Use: All Four!**
- Browse GitHub Pages to see what exists
- Test via CLI for debugging
- Check Web UI for user experience
- Use wizard to test help documentation
- Add your plugins to the store via PR

---

## 💡 Pro Tips

1. **Update regularly:** `sudo pwnstore update` to get the latest features
2. **Bookmark the UI:** Add `/plugins/pwnstore_ui/` to your mobile home screen
3. **Bookmark the wizard:** Save [pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html) for when things break
4. **Use CLI for debugging:** `pwnstore info <plugin>` shows full technical details
5. **Check sources:** `pwnstore sources` to see where plugins come from
6. **Read logs:** `sudo journalctl -u pwnagotchi -f` to watch installations in real-time

---

## 📚 Documentation

- **Installation Guide:** See above
- **Web UI Demo:** [https://pwnstore.org/](https://pwnstore.org/)
- **Troubleshooting Wizard:** [https://pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)
- **Discord Support:** [Join the Pwnagotchi Discord](https://discord.gg/jFasAGdTFm)

---

## 🌟 Community Resources

- **[Discord]** - https://discord.gg/jFasAGdTFm
- **[Troubleshoot]** - https://pwnstore.org/troubleshoot.html
- **[GitHub Wiki]** - https://github.com/jayofelony/pwnagotchi/wiki
- **[Reddit]** - https://reddit.com/r/pwnagotchi
- **[Official Site]** - https://pwnagotchi.org
- **[Pwnmail Test]** - https://opwngrid.xyz/search/a1dcea78603b44e3fc3de09f0b9a0a5e28ffbd2e69429494e0d77bb34a2623ea

---

## ☕ Support the Development

If this tool saved you time or saved your SD card from clutter, consider buying me a coffee!

**[Buy me a coffee (WPA2)](https://buymeacoffee.com/wpa2)**

<a href="https://buymeacoffee.com/wpa2">
  <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=wpa2&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" />
</a>

### 💬 Got Questions or Feedback?

**Message me via Pwnmail:** [Test my Pwnagotchi](https://opwngrid.xyz/search/a1dcea78603b44e3fc3de09f0b9a0a5e28ffbd2e69429494e0d77bb34a2623ea)

This is my test Pwnagotchi - send me a message to test if Pwnmail works or to reach out with feedback, bug reports, or plugin suggestions!

---

## 📜 License

GPL-3.0 License - See [LICENSE](LICENSE) file for details

## 🙏 Credits

**Created by WPA2**

Special thanks to:
- The Pwnagotchi community
- Plugin developers who make this ecosystem possible
- Contributors who help maintain the registry

---

## 🔮 Roadmap

- [x] Interactive troubleshooting wizard
- [ ] Plugin dependency resolution
- [ ] Version pinning support
- [ ] Local plugin development mode
- [ ] Auto-backup before updates
- [ ] Plugin ratings/reviews
- [ ] Custom repository support
- [ ] Integration with Pwnagotchi updates

---

**Made with 💚 for the Pwnagotchi community**
