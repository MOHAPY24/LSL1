import subprocess, json
from utils import installed
from ids import *

def get_os(name):
    if name not in distros:
        raise NotImplementedError(f"[X] OS '{name}' is not a valid LSL OS, or it hasnt been implemented yet.")
    print(f"[+] Installing '{name}'")
    subprocess.run(f"{distros[name]}", shell=True)
    try:
        with open(f"src/linsubsys/{name.lower()}/Dockerfile", 'w') as f:
            f.write(f"""FROM {distrosn[name]}

CMD ["/bin/sh"]
            """)
            # Check if the file was written correctly
            f.seek(0)
            r = open(f"src/linsubsys/{name.lower()}/Dockerfile", 'r')
            content = r.read()
            r.close()
            if not content.strip():
                print(f"[X] Dockerfile for {name} is empty!")
            else:
                print(f"[+] Dockerfile for {name} written successfully.")
        try:
            subprocess.run(["bash", "src/build_docker.sh", name.lower()], check=True)
            with open("src/linsubsys/installed.json", 'w') as g:
                installed["installed-oses"].append(name.lower())
                g.write(json.dumps(installed, indent=4))
        except subprocess.CalledProcessError as e:
            print(f"[X] Error in building Dockerfile: {e}")

    except FileNotFoundError:
        subprocess.run(f"mkdir src/linsubsys/{name.lower()}", shell=True)
        with open(f"src/linsubsys/{name.lower()}/Dockerfile", 'w') as f:
            f.write(f"""FROM {distrosn[name]}

CMD ["/bin/sh"]
            """)
            f.seek(0)
            r = open(f"src/linsubsys/{name.lower()}/Dockerfile", 'r')
            content = r.read()
            r.close()
            if not content.strip():
                print(f"[X] Dockerfile for {name} is empty!")
            else:
                print(f"[+] Dockerfile for {name} written successfully.")
        try:
            subprocess.run(["bash", "src/build_docker.sh", name.lower()], check=True)
            with open("src/linsubsys/installed.json", 'w') as g:
                installed["installed-oses"].append(name.lower())
                g.write(json.dumps(installed, indent=4))
        except subprocess.CalledProcessError as e:
            print(f"[X] Error in building Dockerfile: {e}")
