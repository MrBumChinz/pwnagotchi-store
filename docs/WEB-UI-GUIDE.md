# 🌐 Web UI Guide - Browser Interfaces

PwnStore offers two browser-based interfaces: the on-device Web UI and the public GitHub Pages gallery.

---

## 🌐 On-Device Web UI

Access PwnStore through your browser on mobile or desktop - no SSH required!

### Installation

```bash
# 1. Install CLI tool (if not already installed)
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore

# 2. Download the UI plugin
sudo wget -O /usr/local/share/pwnagotchi/custom-plugins/pwnstore_ui.py https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore_ui.py

# 3. Enable in config
sudo nano /etc/pwnagotchi/config.toml
```

Add these lines:
```toml
[main.plugins.pwnstore]
enabled = true

[main.plugins.pwnstore_ui]
enabled = true
```

Restart Pwnagotchi:
```bash
sudo systemctl restart pwnagotchi
```

### Access the Web UI

**URL:** `http://<your-pwnagotchi-ip>/plugins/pwnstore_ui/`

**Default IPs:**
- USB connection: `http://10.0.0.2/plugins/pwnstore_ui/`
- Hostname (v2.9.5.4+): `http://pwnagotchi.local/plugins/pwnstore_ui/`

---

## 📱 Using the Web UI

### From Desktop

1. Connect to your Pwnagotchi (USB/Ethernet/WiFi)
2. Open browser and navigate to the UI
3. Browse the plugin gallery
4. Click **[Install]** on any plugin
5. Wait for success notification
6. Restart Pwnagotchi

### From Mobile

1. Connect to Pwnagotchi's network
2. Open Safari/Chrome/Firefox
3. Visit the plugins page
4. **Tap [Install]** - touch optimized!
5. Get instant visual feedback
6. No SSH knowledge needed! 📱

---

## ✨ Web UI Features

### 🔍 Search & Filter
- **Live Search:** Type to filter plugins instantly
- **Category Filters:** Display, GPS, Social, Hardware, Attack, System
- **Real-time Results:** Updates as you type

### ✅ Status Indicators
- **Green ✓ Badge:** Plugin is installed
- **Install Button:** Plugin not installed
- **Version Number:** Shows plugin version

### 📋 Plugin Cards
Each card shows:
- Plugin name
- Author
- Category badge
- Version
- Description
- Install/Uninstall button

### 💬 Toast Notifications
Visual feedback for:
- ✅ Installation success
- ❌ Installation errors
- ℹ️ Status updates

---

## 🌍 GitHub Pages Gallery

Browse the complete plugin catalog from anywhere - no Pwnagotchi needed!

**URL:** **[https://pwnstore.org/](https://pwnstore.org/)**

### What You Can Do

- 📖 **Browse all 66+ plugins** with full descriptions
- 🔍 **Search by name** or filter by category
- 📋 **Copy install commands** - click any plugin
- 🔗 **View GitHub sources** - direct repo links
- 📱 **Access from anywhere** - desktop, tablet, phone

### How to Use It

1. Visit [pwnstore.org](https://pwnstore.org/)
2. Browse or search for plugins
3. Click on a plugin card
4. Copy the install command
5. SSH into your Pwnagotchi
6. Paste and run the command

**Perfect for:**
- Planning your plugin setup before buying hardware
- Discovering new plugins at work/home
- Sharing the catalog with friends
- Exploring without device access

---

## 🎨 Interface Features

### Retro Terminal Theme
- Classic Pwnagotchi green-on-black aesthetic
- VT323 monospace font
- Smooth animations
- Responsive design

### Mobile Optimization
- Touch-friendly buttons
- Swipe-friendly scrolling
- No tiny click targets
- Works on all screen sizes

### One-Click Actions
- Install plugins instantly
- Uninstall just as easily
- Copy commands with one tap
- No typing required

---

## 🔧 Web UI Troubleshooting

### Page Won't Load

**Check plugin is enabled:**
```bash
grep pwnstore_ui /etc/pwnagotchi/config.toml
```

**Check Pwnagotchi is running:**
```bash
sudo systemctl status pwnagotchi
```

**Check logs:**
```bash
sudo journalctl -u pwnagotchi | grep pwnstore_ui
```

### Install Button Doesn't Work

**Verify CLI tool is installed:**
```bash
which pwnstore
# Should show: /usr/local/bin/pwnstore
```

**Check browser console:**
- Press F12 (desktop) or long-press + Inspect (mobile)
- Look for JavaScript errors

**Clear browser cache:**
- Desktop: Ctrl + Shift + R
- Mobile: Settings → Clear cache

### CSRF Token Errors

Make sure you're running the latest version:
```bash
sudo wget -O /usr/local/share/pwnagotchi/custom-plugins/pwnstore_ui.py https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore_ui.py
sudo systemctl restart pwnagotchi
```

---

## 💡 Pro Tips

### Bookmark on Mobile
Add the UI to your home screen:
1. Visit the page in your browser
2. Tap Share → Add to Home Screen
3. Now you have a "PwnStore app"!

### Use Alongside CLI
- Browse visually in the UI
- Install complex plugins via CLI for better error messages
- Best of both worlds!

### Check Installation Status
The UI shows which plugins are installed with a green ✓ badge - super handy for keeping track!

---

## 📚 Related Guides

- [CLI Guide](CLI-GUIDE.md) - Command line usage
- [Troubleshooting](TROUBLESHOOTING.md) - Fix common issues
- [FAQ](FAQ.md) - Quick answers

---

**[← Back to Main README](../README.md)**
