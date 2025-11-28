import sys, json, subprocess, get
from utils import installed
from ids import distrosn as distros


if sys.argv[1] == "list":
    print(str(installed["installed-oses"]).replace("{", '').replace("}", '').replace(":", ", ID:"))

if sys.argv[1] == "get":
    try:
        sys.argv[2]
    except IndexError:
        raise ModuleNotFoundError("[X] No distro passed :(")
    get.get_os(sys.argv[2])

if sys.argv[1] == "list_download":
    for i in distros:
        print(i)

if sys.argv[1] == "remove":
    try:
        sys.argv[2]
    except IndexError:
        raise ModuleNotFoundError("[X] No distro passed :(")
    existing_container = subprocess.run(
            ["sudo", "docker", "ps", "-q", "-n", "1", "-f", f"ancestor={sys.argv[2].replace(":latest", '')}"],
            stdout=subprocess.PIPE
        )
    container_id = existing_container.stdout.decode().strip()
    subprocess.run(["docker", "rm", "-f", container_id])

if sys.argv[1] == "run":
    try:
        sys.argv[2]
    except IndexError:
        raise ModuleNotFoundError("[X] No distro passed :(")
    if sys.argv[2] not in distros or sys.argv[2] not in installed["installed-oses"]:
        raise NotImplementedError("[X] Distro passed either arent implemented in LSL or not installed!")
    try:
        existing_container = subprocess.run(
            ["sudo", "docker", "ps", "-q", "-n", "1", "-f", f"ancestor={sys.argv[2].replace(":latest", '')}"],
            stdout=subprocess.PIPE
        )
        container_id = existing_container.stdout.decode().strip()
        print(f"Container ID: {container_id}")
        subprocess.run(f"sudo docker start {container_id}", shell=True)
        subprocess.run(f"sudo docker exec -it {container_id} /bin/sh", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        print(f"Error output: {e.stderr}")