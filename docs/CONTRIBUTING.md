# 🤝 Contributing - Add Your Plugin to PwnStore

Want to see your plugin in PwnStore? It's easy!

---

## 🚀 Quick Start

1. **Fork this repository**
2. **Add your plugin's GitHub URL** to `repos.txt`
3. **Submit a Pull Request**
4. **Wait for merge** - registry auto-updates!

That's it! No manual JSON editing needed.

---

## 📋 Requirements

Your plugin must:
- ✅ Be hosted on GitHub
- ✅ Have a `.py` file (Pwnagotchi plugin format)
- ✅ Include basic documentation (README recommended)
- ✅ Work with current Pwnagotchi versions
- ✅ Not contain malicious code

---

## 📝 Step-by-Step Guide

### 1. Prepare Your Plugin

Make sure your plugin repository has:
- A clear README with description and usage
- A valid Python file (`.py`)
- Proper Pwnagotchi plugin structure

**Example plugin structure:**
```python
import pwnagotchi.plugins as plugins
import logging

class YourPlugin(plugins.Plugin):
    __author__ = 'your_name'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Brief description'

    def on_loaded(self):
        logging.info("YourPlugin loaded")
```

### 2. Fork PwnStore Repository

1. Go to [github.com/wpa-2/pwnagotchi-store](https://github.com/wpa-2/pwnagotchi-store)
2. Click **Fork** (top right)
3. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pwnagotchi-store
   cd pwnagotchi-store
   ```

### 3. Add Your Plugin URL

Edit `repos.txt` and add your repository URL:

```bash
echo "https://github.com/YOUR_USERNAME/your-plugin-repo" >> repos.txt
```

**Example repos.txt entry:**
```
https://github.com/username/pwnagotchi-plugin-awesome
```

**Supported formats:**
- Full repository URL: `https://github.com/user/repo`
- Organization repos: `https://github.com/org/repo`
- Multiple plugins in one repo: Add the repo once, all plugins auto-detected

### 4. Test Locally (Optional)

Run the builder to verify it works:

```bash
python3 builder.py
```

Check `plugins.json` was updated with your plugin.

### 5. Commit and Push

```bash
git add repos.txt
git commit -m "Add: your-plugin-name"
git push origin main
```

### 6. Submit Pull Request

1. Go to your fork on GitHub
2. Click **Pull Request**
3. Click **New Pull Request**
4. Add description:
   ```
   Adding: YourPluginName
   
   Plugin description: Brief description of what it does
   Repository: https://github.com/username/your-plugin
   ```
5. Click **Create Pull Request**

---

## 🎯 Auto-Categorization

PwnStore automatically categorizes your plugin based on keywords in:
- Plugin filename
- Description
- Repository name

**Categories:**
- **Display** - `display`, `screen`, `ui`, `waveshare`, `eink`
- **GPS** - `gps`, `location`, `coordinates`
- **Social** - `discord`, `telegram`, `slack`, `twitter`, `notification`
- **Hardware** - `hardware`, `ups`, `battery`, `sensor`, `gpio`
- **Attack** - `attack`, `deauth`, `crack`, `handshake`, `scan`
- **System** - Everything else

**Want a specific category?**  
Include the category keyword in your plugin description!

---

## 🔄 How the Registry Updates

1. **You submit PR** with your repo URL in `repos.txt`
2. **Maintainer reviews** (usually within 24-48 hours)
3. **PR gets merged** to main branch
4. **GitHub Actions triggers** automatically
5. **Builder scans** your repository
6. **Registry updates** with your plugin metadata
7. **Plugin appears** in CLI, Web UI, and Gallery!

**Total time:** Usually live within 5 minutes of PR merge!

---

## ✅ Checklist Before Submitting

- [ ] Plugin is on GitHub
- [ ] Plugin follows Pwnagotchi plugin structure
- [ ] README exists with clear description
- [ ] Tested on actual Pwnagotchi
- [ ] No malicious code
- [ ] Repository URL added to `repos.txt`
- [ ] Committed and pushed to your fork
- [ ] Pull request submitted with description

---

## 🎨 Best Practices

### Documentation
- Include clear README with:
  - What the plugin does
  - Required dependencies
  - Configuration options
  - Examples

### Versioning
- Use semantic versioning: `1.0.0`
- Update `__version__` in your plugin code

### Dependencies
- List any Python packages needed
- Include installation commands in README

### Configuration
- Document all config.toml options
- Provide example config snippet

### Example README Template

```markdown
# Your Plugin Name

Brief description of what it does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation

Via PwnStore:
\`\`\`bash
sudo pwnstore install your-plugin
\`\`\`

Manual:
\`\`\`bash
cd /usr/local/share/pwnagotchi/custom-plugins/
wget https://raw.githubusercontent.com/username/repo/main/your-plugin.py
\`\`\`

## Configuration

Add to `/etc/pwnagotchi/config.toml`:
\`\`\`toml
[main.plugins.your-plugin]
enabled = true
option1 = "value"
option2 = 123
\`\`\`

## Usage

Explain how it works...

## Requirements
- Python package1
- Python package2

## License
GPL3
```

---

## 🔍 After Your Plugin is Added

### Verify It's Live

**Check CLI:**
```bash
pwnstore list | grep your-plugin
```

**Check Web UI:**
Visit [pwnstore.org](https://pwnstore.org/) and search

**Get plugin info:**
```bash
pwnstore info your-plugin
```

### Updating Your Plugin

Just push changes to your repository!

The registry rebuilds daily, or request a manual rebuild by:
1. Opening an issue
2. Mentioning `@wpa-2`

---

## 🐛 Troubleshooting

### Plugin Not Showing Up

**Check the registry:**
Look in `plugins.json` for your plugin entry

**Verify URL format:**
Should be: `https://github.com/username/repo` (no trailing slash)

**Check builder logs:**
GitHub Actions tab shows build output

### Wrong Category

Add category keywords to your:
- Plugin filename
- Description
- Repository name

### Multiple Plugins in One Repo

All `.py` files are detected automatically!  
Each gets a separate entry in the store.

---

## 💬 Need Help?

- **Discord:** [discord.gg/jFasAGdTFm](https://discord.gg/jFasAGdTFm)
- **Telegram:** [t.me/Pwnagotchi_UK_Chat](https://t.me/Pwnagotchi_UK_Chat/)
- **GitHub Issues:** Open an issue on the repo

---

## 🙏 Thanks!

Thank you for contributing to the Pwnagotchi ecosystem! Every plugin makes the community stronger.

---

**[← Back to Main README](../README.md)**
