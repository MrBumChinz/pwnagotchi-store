# ❓ FAQ - Frequently Asked Questions

Quick answers to common questions about PwnStore.

---

## 📦 General Questions

### What is PwnStore?

PwnStore is a plugin manager for Pwnagotchi that lets you browse, install, and manage plugins without downloading massive ZIP files. It works via CLI (command line), Web UI (browser), and a public gallery.

### Do I need PwnStore to use Pwnagotchi?

No! PwnStore is optional. It just makes installing and managing plugins much easier than manual downloads.

### Is PwnStore official?

No, PwnStore is an unofficial community project. It's not affiliated with the official Pwnagotchi project, but it's widely used in the community.

### Does PwnStore cost money?

No! PwnStore is completely free and open source (GPL-3.0 license). If it helped you, consider [buying the creator a coffee](https://buymeacoffee.com/wpa2)! ☕

---

## 🚀 Installation Questions

### How do I install PwnStore?

```bash
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

See [CLI Guide](CLI-GUIDE.md) for full instructions.

### Do I need the Web UI?

No, it's optional! The Web UI makes it easier to browse on mobile, but the CLI works fine on its own.

### Can I use PwnStore offline?

You need internet to download plugins, but you can list already-installed plugins offline.

### What if my Pwnagotchi doesn't have internet?

You'll need to give it internet access (USB tethering, WiFi, Ethernet) to download plugins. After that, plugins work offline.

---

## 🔌 Plugin Questions

### How many plugins are available?

Currently **66+ plugins** from 8 different GitHub repositories. The list grows regularly!

### Are plugins safe?

PwnStore indexes community plugins from known repositories. Always review the plugin's code before installing if you're concerned about security.

### Can I install plugins manually without PwnStore?

Yes! PwnStore just makes it easier. You can always:
```bash
cd /usr/local/share/pwnagotchi/custom-plugins/
wget <plugin_url>
sudo chmod +x <plugin_name>.py
```

### Why doesn't my plugin work after installing?

Common causes:
1. Not enabled in `config.toml`
2. Missing dependencies (API keys, Python packages)
3. Syntax error in config
4. Didn't restart Pwnagotchi

See [Troubleshooting Guide](TROUBLESHOOTING.md) for solutions.

### How do I uninstall a plugin?

```bash
sudo pwnstore uninstall <plugin_name>
```

Or manually:
```bash
sudo rm /usr/local/share/pwnagotchi/custom-plugins/<plugin>.py
# Then remove from config.toml
```

---

## ⚙️ Configuration Questions

### Where is config.toml?

`/etc/pwnagotchi/config.toml`

Edit with: `sudo nano /etc/pwnagotchi/config.toml`

### Does PwnStore modify my config?

Yes, but safely! It adds an `enabled = true` line for each plugin. You can edit or remove these anytime.

### Can I disable PwnStore's auto-config?

PwnStore doesn't have a "disable auto-config" option, but you can always manually edit `config.toml` after installation.

### What's the difference between config.toml and default.toml?

- `default.toml` - Reference file, don't edit!
- `config.toml` - Your actual config (overrides defaults)

---

## 🔄 Update Questions

### How do I update the plugin list?

```bash
sudo pwnstore update
```

This refreshes the registry with any new plugins.

### How do I update PwnStore itself?

```bash
sudo pwnstore upgrade
```

### Do I need to update plugins individually?

Not yet - bulk plugin updates are on the roadmap! For now, reinstall plugins to get new versions.

### How often should I update?

- Plugin list: Weekly or when you want to see new plugins
- PwnStore itself: When notified of updates
- Individual plugins: When the developer releases updates

---

## 🐛 Troubleshooting Questions

### "pwnstore: command not found" - help!

Reinstall:
```bash
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore
```

### Web UI won't load!

Check [Troubleshooting Guide](TROUBLESHOOTING.md) or use the interactive wizard:  
👉 [pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)

### Can't connect to my Pwnagotchi!

Use the connection troubleshooter:  
👉 [pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html) → Connection Issues

### My display isn't working!

Use the display troubleshooter:  
👉 [pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html) → Display Issues

---

## 💻 CLI vs Web UI Questions

### Which should I use - CLI or Web UI?

**Use CLI if:**
- You're comfortable with SSH
- You want detailed output
- You're scripting/automating

**Use Web UI if:**
- You prefer visual browsing
- You're on mobile
- You don't want to SSH

**Both work great!** Use whichever fits your workflow.

### Can I use both?

Absolutely! They use the same backend, so you can mix and match.

### Does the Web UI require the CLI?

Yes, the Web UI calls the CLI tool under the hood.

---

## 🌐 GitHub Pages Gallery Questions

### What's the gallery for?

Browsing the full plugin catalog without connecting to your Pwnagotchi. Perfect for planning your setup!

### Can I install from the gallery?

No, the gallery is view-only. It generates install commands that you copy and run via SSH.

### Is the gallery always up to date?

Yes! It updates automatically when the registry rebuilds.

---

## 🤝 Contributing Questions

### How do I add my plugin to PwnStore?

See the [Contributing Guide](CONTRIBUTING.md)!

TL;DR:
1. Fork the repo
2. Add your GitHub URL to `repos.txt`
3. Submit PR

### How long until my plugin appears?

Usually within 5 minutes of PR merge! GitHub Actions rebuilds the registry automatically.

### Can I add plugins from other repos?

Yes! Anyone can add plugins from any public GitHub repository (with permission from the author, of course).

### What if my plugin doesn't fit a category?

It'll go in "System" by default. Add category keywords to your description for better categorization!

---

## ⚠️ Safety Questions

### Can I run "sudo apt-get upgrade"?

**🚨 NO! NEVER!** This breaks Pwnagotchi!

✅ **OK:** `sudo apt-get update` (updates package list only)  
❌ **BAD:** `sudo apt-get upgrade` (will break everything)

### Is it safe to use PwnStore?

Yes! PwnStore itself is open source. It only downloads plugins from public GitHub repos.

**As always:** Review code before running it on your device!

### Do plugins phone home?

Depends on the plugin! Some plugins (like wigle, wpa-sec) upload data to third-party services. Check the plugin's README before installing.

---

## 📱 Mobile Questions

### Can I use PwnStore on my phone?

Yes! The Web UI works great on mobile browsers.

### Do I need a special app?

No - just use Safari, Chrome, Firefox, etc. You can add the Web UI to your home screen like an app!

### Can I SSH from my phone?

Yes! Use apps like:
- **iOS:** Terminus, Blink
- **Android:** JuiceSSH, Termux

---

## 🔮 Feature Requests

### Will you add feature X?

Maybe! Check the [roadmap](../README.md#-roadmap) and open an issue on GitHub.

Current roadmap:
- [x] Interactive troubleshooting wizard
- [ ] Plugin dependency resolution
- [ ] Version pinning
- [ ] Local plugin dev mode
- [ ] Auto-backup before updates
- [ ] Plugin ratings/reviews

### Can I contribute code?

Absolutely! Pull requests welcome. See [Contributing Guide](CONTRIBUTING.md).

---

## 💬 Support Questions

### Where do I get help?

1. **Interactive Troubleshooter:** [pwnstore.org/troubleshoot.html](https://pwnstore.org/troubleshoot.html)
2. **Discord:** [discord.gg/jFasAGdTFm](https://discord.gg/jFasAGdTFm)
3. **Telegram:** [t.me/Pwnagotchi_UK_Chat](https://t.me/Pwnagotchi_UK_Chat/)
4. **Reddit:** [r/pwnagotchi](https://reddit.com/r/pwnagotchi)

### Can I contact the developer?

Yes! Via:
- GitHub Issues
- Discord
- Telegram
- Pwnmail (see main README)

### How do I report a bug?

Open an issue on GitHub with:
1. What you tried to do
2. What happened instead
3. Error messages
4. Your Pwnagotchi version

---

## 🎯 Quick Commands Reference

```bash
# Install PwnStore
sudo wget -O /usr/local/bin/pwnstore https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/pwnstore.py && sudo chmod +x /usr/local/bin/pwnstore

# List plugins
pwnstore list

# Search
pwnstore search discord

# Install
sudo pwnstore install <plugin>

# Uninstall
sudo pwnstore uninstall <plugin>

# Update registry
sudo pwnstore update

# Upgrade PwnStore
sudo pwnstore upgrade
```

---

## 📚 More Info

- [CLI Guide](CLI-GUIDE.md) - Detailed command reference
- [Web UI Guide](WEB-UI-GUIDE.md) - Browser interface
- [Troubleshooting](TROUBLESHOOTING.md) - Fix common issues
- [Contributing](CONTRIBUTING.md) - Add your plugins

---

**Still have questions? Ask on [Discord](https://discord.gg/jFasAGdTFm) or [Telegram](https://t.me/Pwnagotchi_UK_Chat/)!**

**[← Back to Main README](../README.md)**
