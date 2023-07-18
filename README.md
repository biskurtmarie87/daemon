# Generic Daemon Process
```
To check FS or file exist before executing sub process
```

# Enable / Start /  Status / Disable
```
systemctl enable <daemon_name.service>
systemctl start <daemon_name.service>
systemctl status <daemon_name.service>
systemctl stop <daemon_name.service>
systemctl disable <daemon_name.service>

```

# Install
```
1) Used normal user and go to home directory
2) clone the repository
3) execute "python -m venv venv"
4) source venv/bin/activate
5) pip install upgrade pip
```

# Update
```
1) Used normal user
2) Go to directory "daemon"
3) git reset --hard
4) git checkout main
5) git pull
```

# Test
```
python exec_daemon.py
```

