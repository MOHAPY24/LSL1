import json

try:
    with open("src/linsubsys/installed.json", 'r') as f:
        installed = json.loads(f.read())
except FileNotFoundError:
    with open("src/linsubsys/installed.json", 'w') as f:
        f.write("""
{
    "installed-oses": []
}
""")
    with open("src/linsubsys/installed.json", 'r') as f:
        installed = json.loads(f.read())
    
except json.JSONDecodeError:
    with open("src/linsubsys/installed.json", 'w') as f:
        f.write("""
{
    "installed-oses": []
}
""")
    with open("src/linsubsys/installed.json", 'r') as f:
        installed = json.loads(f.read())