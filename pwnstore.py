#!/usr/bin/env python3
'''
PwnStore - The Unofficial Pwnagotchi App Store
Author: WPA2
Donations: https://buymeacoffee.com/wpa2
v3.2.6 - Scanning Noise Reduced
'''

import requests
import json
import argparse
import os
import sys
import zipfile
import io
import shutil
import re

# --- CONFIGURATION ---
DEFAULT_REGISTRY = "https://raw.githubusercontent.com/wpa-2/pwnagotchi-store/main/plugins.json"

CUSTOM_PLUGIN_DIR = "/usr/local/share/pwnagotchi/custom-plugins/"
CONFIG_FILE = "/etc/pwnagotchi/config.toml"

# ANSI Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def banner():
    print(f"{CYAN}")
    print(r"    ____                 _____ __                 ")
    print(r"   / __ \_      ______  / ___// /_____  ________  ")
    print(r"  / /_/ / | /| / / __ \ \__ \/ __/ __ \/ ___/ _ \ ")
    print(r" / ____/| |/ |/ / / / /___/ / /_/ /_/ / /  /  __/ ")
    print(r"/_/     |__/|__/_/ /_//____/\__/\____/_/    \___/  ")
    print(f"{RESET}")
    print(f"  {CYAN}v3.2.6{RESET} - Final Build")
    print(f"  Support the dev: {GREEN}https://buymeacoffee.com/wpa2{RESET}\n")

def check_sudo():
    if os.geteuid() != 0:
        print(f"{RED}[!] Error: You must run this command with sudo.{RESET}")
        sys.exit(1)

def is_safe_name(name):
    """Security: Prevents Path Traversal"""
    return re.match(r'^[a-zA-Z0-9_-]+$', name) is not None

def compare_versions(v1, v2):
    """Compare semantic versions properly"""
    try:
        v1_parts = [int(x) for x in v1.lstrip('v').split('.')]
        v2_parts = [int(x) for x in v2.lstrip('v').split('.')]
        while len(v1_parts) < len(v2_parts): v1_parts.append(0)
        while len(v2_parts) < len(v1_parts): v2_parts.append(0)
        for a, b in zip(v1_parts, v2_parts):
            if a > b: return 1
            elif a < b: return -1
        return 0
    except:
        if v1 > v2: return 1
        elif v1 < v2: return -1
        return 0

def get_local_version(file_path):
    """Reads the __version__ string from a local file."""
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            match = re.search(r"__version__\s*=\s*[\"'](.+?)[\"']", content)
            if match: return match.group(1)
    except: pass
    return "0.0.0"

def get_installed_plugins():
    if not os.path.exists(CUSTOM_PLUGIN_DIR): return []
    return [f.replace(".py", "") for f in os.listdir(CUSTOM_PLUGIN_DIR) if f.endswith(".py")]

def get_registry_url():
    """Checks config.toml for a developer override"""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                content = f.read()
                match = re.search(r'main\.pwnstore_url\s*=\s*["\'](http.+?)["\']', content)
                if match: return match.group(1)
    except: pass
    return DEFAULT_REGISTRY

def fetch_registry():
    url = get_registry_url()
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            print(f"{RED}[!] Store error (Status: {r.status_code}){RESET}")
            sys.exit(1)
        return r.json()
    except:
        print(f"{RED}[!] Connection failed.{RESET}")
        sys.exit(1)

def clean_author_name(author):
    if not author or author == 'Unknown': return 'Unknown'
    cleaned = re.sub(r'\s*<?[\w\.-]+@[\w\.-]+>?', '', author).strip()
    cleaned = re.sub(r'https?://[^\s]+', '', cleaned).strip()
    cleaned = re.sub(r'^[0-9]+\+\s*', '', cleaned).strip()
    cleaned = re.sub(r'^@', '', cleaned).strip()
    if not cleaned or cleaned.lower() == 'by':
        return author.split(',')[0].strip() or 'Unknown'
    return cleaned.replace(',', '').strip()

def list_plugins(args):
    print(f"[*] Fetching plugin list...")
    registry = fetch_registry()
    installed = get_installed_plugins()
    print(f"{'NAME':<25} | {'VERSION':<10} | {'AUTHOR':<20} | {'STATUS'}")
    print("-" * 80)
    for p in registry:
        name = p['name']
        if len(name) > 24: name = name[:21] + "..."
        status = f"{GREEN}INSTALLED{RESET}" if name in installed else "Available"
        author = clean_author_name(p.get('author', 'Unknown'))
        if len(author) > 19: author = author[:17] + "..."
        print(f"{name:<25} | {p['version']:<10} | {author:<20} | {status}")
    print("-" * 80)

def list_sources(args):
    print(f"[*] Analyzing repository sources...")
    registry = fetch_registry()
    sources = {} 
    for p in registry:
        url = p.get('download_url', '')
        repo_name = "Unknown Source"
        if 'github.com' in url or 'githubusercontent.com' in url:
            parts = url.split('/')
            try: repo_name = f"github.com/{parts[3]}/{parts[4]}"
            except: repo_name = url[:40]
        else: repo_name = "Other/Local"
        sources[repo_name] = sources.get(repo_name, 0) + 1
    print(f"\n{'REPOSITORY / SOURCE':<50} | {'PLUGINS'}")
    print("-" * 65)
    for source, count in sorted(sources.items()):
        print(f"{source:<50} | {count}")
    print("-" * 65)
    print(f"Total indexed: {len(registry)}\n")

def search_plugins(args):
    registry = fetch_registry()
    installed = get_installed_plugins()
    query = args.query.lower()
    results = [p for p in registry if query in p['name'].lower() or query in p['description'].lower()]
    if not results: return print(f"{YELLOW}[!] No results for '{args.query}'{RESET}")
    print(f"{'NAME':<25} | {'VERSION':<10} | {'AUTHOR':<20} | {'STATUS'}")
    print("-" * 80)
    for p in results:
        name = p['name']
        if len(name) > 24: name = name[:21] + "..."
        status = f"{GREEN}INSTALLED{RESET}" if name in installed else "Available"
        author = clean_author_name(p.get('author', 'Unknown'))
        if len(author) > 19: author = author[:17] + "..."
        print(f"{name:<25} | {p['version']:<10} | {author:<20} | {status}")
    print("-" * 80)

def show_info(args):
    if not is_safe_name(args.name): return
    registry = fetch_registry()
    plugin_data = next((p for p in registry if p['name'] == args.name), None)
    if not plugin_data: return print(f"{RED}[!] Not found.{RESET}")
    print(f"\n{CYAN}--- {plugin_data['name']} ---{RESET}")
    print(f"Author:      {plugin_data['author']}")
    print(f"Version:     {plugin_data['version']}")
    print(f"Category:    {plugin_data.get('category', 'General')}")
    print(f"\n{YELLOW}Description:{RESET}\n{plugin_data['description']}")
    print(f"\n{YELLOW}Download URL:{RESET}\n{plugin_data['download_url']}\n")

def scan_for_config_params(file_path, plugin_name):
    """Refined scanner to ignore noise keywords."""
    params = []
    ignore = [
        'main', 'plugins', 'enabled', 'name', 'whitelist', 'screen', 'display', 
        'none', 'false', 'true', 'self', 'options', 'kwargs', 'args', 'data',
        'result', 'logging', 'status', 'json', 'requests', 'path', 'file', 'time', plugin_name
    ]
    try:
        with open(file_path, 'r', errors='ignore') as f:
            for line in f:
                if any(bad in line for bad in ['requests.', 'logging.', 'json.', 'print(', 'os.', 'time.']):
                    continue
                matches = re.findall(r"self\.options\s*\[\s*['\"]([^'\"]+)['\"]\s*\]", line)
                if 'config' in line or 'options' in line:
                    matches += re.findall(r"\.get\(\s*['\"]([^'\"]+)['\"]", line)
                for m in matches:
                    clean = m.strip()
                    if clean.lower() not in ignore and len(clean) > 1 and '/' not in clean:
                        params.append(clean)
    except: pass
    return sorted(list(set(params)))

def upgrade_tool(args):
    check_sudo()
    print(f"[*] Updating PwnStore...")
    current_registry = get_registry_url()
    script_url = current_registry.replace("plugins.json", "pwnstore.py")
    try:
        r = requests.get(script_url, timeout=15)
        if r.status_code != 200 or "#!/usr/bin/env python3" not in r.text: return
        current_file = os.path.realpath(__file__)
        with open(current_file, 'w') as f: f.write(r.text)
        os.chmod(current_file, 0o755)
        print(f"{GREEN}[+] Updated!{RESET}")
    except: print(f"{RED}[!] Update failed.{RESET}")

def update_plugins(args):
    check_sudo()
    print(f"[*] Checking for updates...")
    registry = fetch_registry()
    installed_files = [f for f in os.listdir(CUSTOM_PLUGIN_DIR) if f.endswith(".py")]
    updates_found = []
    for filename in installed_files:
        plugin_name = filename.replace(".py", "")
        remote_data = next((p for p in registry if p['name'] == plugin_name), None)
        if remote_data:
            local_ver = get_local_version(os.path.join(CUSTOM_PLUGIN_DIR, filename))
            remote_ver = remote_data['version']
            if compare_versions(remote_ver, local_ver) > 0:
                updates_found.append({"name": plugin_name, "local": local_ver, "remote": remote_ver})
    if not updates_found:
        print(f"{GREEN}[+] Everything current.{RESET}")
        return
    print(f"\n{YELLOW}Updates available:{RESET}")
    for u in updates_found: print(f"  • {CYAN}{u['name']}{RESET}: v{u['local']} -> v{u['remote']}")
    print(f"\n{YELLOW}Upgrade these {len(updates_found)} plugins? (Y/n){RESET}")
    try: choice = input().lower()
    except: return
    if choice == 'y' or choice == '':
        for u in updates_found:
            class MockArgs: name = u['name']
            install_plugin(MockArgs())
        print(f"\n{GREEN}[+] Complete! Restart Pwnagotchi.{RESET}")

def install_plugin(args):
    check_sudo()
    if not is_safe_name(args.name): return
    registry = fetch_registry()
    plugin_data = next((p for p in registry if p['name'] == args.name), None)
    if not plugin_data: return print(f"{RED}[!] Not found.{RESET}")

    final_file_path = os.path.join(CUSTOM_PLUGIN_DIR, f"{args.name}.py")
    already_installed = os.path.exists(final_file_path)
    print(f"[*] Installing {CYAN}{args.name}{RESET}...")

    try:
        if plugin_data.get('origin_type') == 'zip':
            r = requests.get(plugin_data['download_url'], timeout=30)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            with z.open(plugin_data['path_inside_zip']) as source, open(final_file_path, "wb") as dest:
                shutil.copyfileobj(source, dest)
        else:
            r = requests.get(plugin_data['download_url'], timeout=30)
            if not os.path.exists(CUSTOM_PLUGIN_DIR): os.makedirs(CUSTOM_PLUGIN_DIR)
            with open(final_file_path, "wb") as f: f.write(r.content)

        print(f"{GREEN}[+] Installed to {final_file_path}{RESET}")
        update_config(args.name, enable=True)
        if not already_installed:
            params = scan_for_config_params(final_file_path, args.name)
            if params:
                print(f"\n{YELLOW}[!] CONFIG REQUIRED:{RESET}")
                for p in params:
                    val = "['mem', 'cpu']" if p == 'fields' else "value"
                    print(f"  main.plugins.{args.name}.{p} = {val}")
    except Exception as e: print(f"{RED}[!] Failed: {e}{RESET}")

def uninstall_plugin(args):
    check_sudo()
    if not is_safe_name(args.name): return
    file_path = os.path.join(CUSTOM_PLUGIN_DIR, f"{args.name}.py")
    if not os.path.exists(file_path): return
    try:
        os.remove(file_path)
        print(f"{GREEN}[+] File removed.{RESET}")
        remove_plugin_config(args.name)
    except: pass

def update_config(plugin_name, enable=True):
    """Prevents duplicates by cleaning the plugin's block."""
    try:
        if not os.path.exists(CONFIG_FILE): return
        with open(CONFIG_FILE, "r") as f: lines = f.readlines()
        prefix = f"main.plugins.{plugin_name}."
        new_lines = [l for l in lines if not l.strip().startswith(prefix)]
        if enable:
            if new_lines and not new_lines[-1].endswith('\n'): new_lines[-1] += '\n'
            new_lines.append(f"\n{prefix}enabled = true\n")
        with open(CONFIG_FILE, "w") as f: f.writelines(new_lines)
    except: pass

def remove_plugin_config(plugin_name):
    try:
        with open(CONFIG_FILE, "r") as f: lines = f.readlines()
        prefix = f"main.plugins.{plugin_name}."
        new_lines = [l for l in lines if not l.strip().startswith(prefix)]
        with open(CONFIG_FILE, "w") as f: f.writelines(new_lines)
    except: pass

def main():
    banner()
    parser = argparse.ArgumentParser(description="Pwnagotchi Plugin Manager")
    subparsers = parser.add_subparsers()
    p_list = subparsers.add_parser('list'); p_list.set_defaults(func=list_plugins)
    p_src = subparsers.add_parser('sources'); p_src.set_defaults(func=list_sources)
    p_sch = subparsers.add_parser('search'); p_sch.add_argument('query'); p_sch.set_defaults(func=search_plugins)
    p_inf = subparsers.add_parser('info'); p_inf.add_argument('name'); p_inf.set_defaults(func=show_info)
    p_ins = subparsers.add_parser('install'); p_ins.add_argument('name'); p_ins.set_defaults(func=install_plugin)
    p_uni = subparsers.add_parser('uninstall'); p_uni.add_argument('name'); p_uni.set_defaults(func=uninstall_plugin)
    p_upg = subparsers.add_parser('upgrade'); p_upg.set_defaults(func=upgrade_tool)
    p_upd = subparsers.add_parser('update'); p_upd.set_defaults(func=update_plugins)
    args = parser.parse_args()
    if hasattr(args, 'func'): args.func(args)
    else: parser.print_help()

if __name__ == "__main__":
    main()
