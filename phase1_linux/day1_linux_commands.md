# Day 1 — Essential Linux Commands for Robotics

## Filesystem navigation
- `ls /` — See top-level folders.
- `ls /home` — View home directories.
- `ls /etc` — View system configuration.
- `ls /var/log` — View system logs.
- `cd robotics_ws` — Enter a workspace directory.

## Creating files and directories
- `mkdir robotics_ws` — Create a directory.
- `mkdir -p robotics_ws/src/my_robot` — Create nested directories.
- `touch README.md` — Create an empty file.
- `touch src/my_robot/main.py` — Create a Python file.

## Reading and editing files
- `echo "Hello Robotics" > README.md` — Write or overwrite a file.
- `echo "Line 2" >> README.md` — Append a line.
- `cat README.md` — Display file contents.
- `nano README.md` — Edit a file.

## Copying, moving and deleting
- `cp README.md README_backup.md` — Copy a file.
- `mv README_backup.md docs/` — Move a file.
- `rm README_backup.md` — Delete a file.
- `rm -rf old_folder/` — Recursively delete a folder. **Dangerous: verify the target carefully before use.**

## Permissions
- `ls -la` — Display permissions.
- `chmod +x main.py` — Make a file executable.
- `chmod 755 main.py` — Set file permissions.
- `sudo chown "$USER" file` — Change file ownership.

## Searching
- `find . -name "*.py"` — Find Python files.
- `find /home -type d -name "src"` — Find directories named src.
- `grep "Hello" README.md` — Search inside a file.
- `grep -r "import" src/` — Search recursively.

## System monitoring and hardware
- `top` — Monitor running processes.
- `htop` — Interactive process monitor.
- `df -h` — Check disk usage.
- `free -h` — Check memory usage.
- `lsusb` — List USB devices.
- `dmesg | tail -20` — View recent kernel messages.
