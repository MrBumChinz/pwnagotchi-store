# 🤝 Contributing - Add Your Plugin to PwnStore

Want your plugin in PwnStore? Here's how.

---

## 🚀 Quick Start

1. Fork this repo
2. Add your URL to `repos.txt` (see format below)
3. Submit a Pull Request
4. Wait for merge — registry auto-updates!

---

## 📋 Your Plugin Must

- ✅ Be hosted on GitHub
- ✅ Be a valid Pwnagotchi plugin (`.py` file with `__version__`, `__author__`, `__description__`)
- ✅ Work with current Pwnagotchi versions
- ✅ Not contain malicious code
- ✅ Have a README (recommended)

**Minimum plugin structure:**
```python
import pwnagotchi.plugins as plugins
import logging

class YourPlugin(plugins.Plugin):
    __author__ = 'your_name'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Brief description of what it does'

    def on_loaded(self):
        logging.info("YourPlugin loaded")
```

---

## 📝 URL Format for repos.txt

The builder reads `repos.txt` and needs one of two URL formats:

### Multi-plugin repo (ZIP archive)
If your repo contains one or more plugin `.py` files, add a ZIP archive URL:

```
https://github.com/YOUR_USERNAME/YOUR_REPO/archive/main.zip
```

Or if your default branch is `master`:
```
https://github.com/YOUR_USERNAME/YOUR_REPO/archive/master.zip
```

The builder automatically finds all valid `.py` plugin files inside the ZIP.

**Examples from the current repos.txt:**
```
https://github.com/AlienMajik/pwnagotchi_plugins/archive/refs/heads/main.zip
https://github.com/Sniffleupagus/pwnagotchi_plugins/archive/master.zip
```

### Single plugin file (raw URL)
If you just want to add one specific `.py` file:

```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/your_plugin.py
```

**Example:**
```
https://raw.githubusercontent.com/MrBumChinz/community-quickdic/refs/heads/main/community_quickdic.py
```

### ❌ These formats will NOT work
```
https://github.com/username/repo                    ← just a repo URL, builder can't use this
https://github.com/username/repo/blob/main/plugin.py ← blob URL, not raw content
```

---

## 📤 How to Submit

1. **Fork** [github.com/wpa-2/pwnagotchi-store](https://github.com/wpa-2/pwnagotchi-store)
2. **Edit `repos.txt`** — add your URL on a new line
3. **Test locally** (optional):
   ```bash
   python3 builder.py
   ```
   Check `plugins.json` was updated with your plugin.
4. **Commit and push:**
   ```bash
   git add repos.txt
   git commit -m "Add: your-plugin-name"
   git push origin main
   ```
5. **Open a Pull Request** with a brief description of your plugin

---

## 🎯 Auto-Categorization

PwnStore auto-categorizes based on keywords in your plugin name, description, and code:

| Category | Keywords |
|----------|----------|
| **Display** | display, screen, ui, theme, oled, face, clock, weather |
| **GPS** | gps, location, coordinates, wigle, wardrive |
| **Social** | discord, telegram, slack, webhook, notify |
| **Hardware** | ups, battery, gpio, bluetooth, power |
| **Attack** | handshake, deauth, crack, pmkid, sniff |
| **System** | backup, ssh, log, update, config, wifi |

Include relevant keywords in your `__description__` for accurate categorization.

---

## 🔄 After Merge

1. **GitHub Actions** rebuilds the registry automatically
2. Your plugin appears in CLI, Web UI, and Gallery within minutes
3. The registry also rebuilds daily at midnight UTC

**Verify it's live:**
```bash
pwnstore search your-plugin
pwnstore info your-plugin
```

Or check [pwnstore.org](https://pwnstore.org/) and search.

### Updating Your Plugin

Just push changes to your repository. The registry rebuilds daily, picking up new versions automatically.

---

## 💬 Need Help?

- **Discord:** [discord.gg/jFasAGdTFm](https://discord.gg/jFasAGdTFm)
- **Telegram:** [t.me/Pwnagotchi_UK_Chat](https://t.me/Pwnagotchi_UK_Chat/)
- **GitHub Issues:** Open an issue on the repo

---

**[← Back to Main README](../README.md)**
