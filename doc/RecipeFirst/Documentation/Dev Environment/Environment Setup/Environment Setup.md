Setting up a Lightweight AWS Environment

For a clean, simple dev setup using FastAPI and SQLite, here’s a high-level approach. I'd recommend sticking to On-Demand instances to avoid interruptions and saving costs with auto-stop features. Security is key—restrict inbound ports and use SSH tunnels when possible. For storage, EBS works well with snapshot backups. Regarding connections, optimal performance comes with tmux, but systemd could also manage the server. I’d suggest keeping things practical with basic AWS CLI setup, using the default Python version and keeping things flexible with backup strategies like cron jobs.

I’m curious—how hands-on do you want to get with your setup: fast iterations or more robust setups?

Best-practices blueprint for your AWS dev environment (FastAPI + SQLite)

You want smooth, cheap, and safe. Here’s a focused setup that balances speed with sanity—no domain, SSH-driven, and easy to pause.

The big picture

- Keep it simple: One small EC2 instance, a single attached EBS volume, SSH tunnels for access, and strict security groups.
- Keep it cheap: Stop the instance when idle; add an auto-stop schedule so you don’t forget.
- Keep it safe: Put all state on EBS and in Git. Assume the instance can vanish and you’ll be fine.

Compute options (what to choose and why)

|   |   |   |   |   |
|---|---|---|---|---|
|Option|Pros|Cons|Best when|My take for you|
|On-Demand EC2 + stop/hibernate|Predictable, no interruptions; you only pay for EBS when stopped|Slightly higher hourly cost than Spot|Solo development with sporadic usage|✅ Start here. It’s simple and reliable. Add auto-stop.|
|Spot EC2|Much cheaper|Can be interrupted; you must handle it|You enjoy cost-tuning and don’t mind disruptions|Only if you’re disciplined with Git, EBS, and interruption handling|
|Lightsail|Simpler UI/billing|Less flexible than EC2|You want minimal AWS complexity|Optional alternative, but EC2 fits your plan better|

If you’re building alone and shutting down frequently, On-Demand with auto-stop is the least-friction path. You can always switch to Spot once everything’s scripted and resilient.

🧠 Development-first EC2 setup

•         Use Spot Instance for savings.

•         Attach an encrypted gp3 EBS volume for project data (code + SQLite).

•         Store everything important in Git and EBS.

•         Tag instance for auto-shutdown, use a Lambda + EventBridge rule for evening stop.

•         Boot with cloud-init, install Python + tools + Node (ready for Vue/Tailwind later).

•         SSH from your IP only, forward ports locally for FastAPI/Vite dev.

•         Use tmux for session persistence, or VS Code Remote SSH for full editing.

•         Back up your SQLite DB with a cron job or occasional S3 sync.

Instance sizing and storage

- AMI: Ubuntu LTS (22.04 or 24.04) for a broad ecosystem and quick setup.
- Size: Start small. A general-purpose burstable (e.g., t-series) with 2 CPU / 2–4 GB RAM is usually enough for FastAPI + Vite dev.
- Storage:

- EBS gp3 volume, 20–30 GB to start; encrypt by default.
- Put your project and SQLite DB on this volume.
- Take EBS snapshots before major changes.

Networking and access (secure by default)

- Security Group:

- Inbound: allow SSH (22) from your IP only.
- Avoid opening dev ports to the Internet.

- Use SSH tunnels to reach your dev servers:

- Forward FastAPI and Vite locally:

- ssh -i ~/.ssh/your-key.pem -L 8000:localhost:8000 -L 5173:localhost:5173 ubuntu@YOUR_PUBLIC_DNS

- Then hit [http://localhost:8000](http://localhost:8000) (FastAPI) and [http://localhost:5173](http://localhost:5173) (Vite).

- Optional: use a bastion or Session Manager later; SSH is fine for now.

First-boot bootstrap (cloud-init)

When launching the instance, paste this into “user data” (cloud-init) to prep the box.

#!/bin/bash  
set -eux

# System base  
apt-get update -y  
apt-get upgrade -y  
apt-get install -y build-essential git curl unzip ca-certificates ufw fail2ban

# Python & tooling  
apt-get install -y python3 python3-venv python3-pip pipx  
pipx ensurepath || true

# Optional: Node.js LTS (for Vue/Vite later)  
curl -fsSL [https://deb.nodesource.com/setup_lts.x](https://deb.nodesource.com/setup_lts.x) | bash -  
apt-get install -y nodejs

# Firewall (defense in depth; SG does most heavy lifting)  
ufw default deny incoming  
ufw default allow outgoing  
ufw allow OpenSSH  
yes | ufw enable

# Unattended security updates  
apt-get install -y unattended-upgrades  
dpkg-reconfigure -f noninteractive unattended-upgrades

# Timezone (adjust if you like)  
timedatectl set-timezone America/Halifax

Project layout and Python environment

- Repo structure (example):

- app/

- main.py (FastAPI entry)
- api/, models/, deps/

- tests/
- pyproject.toml (or requirements.txt)
- .env (exclude from Git)

- Virtual env:

- python3 -m venv ~/.venvs/yourapp
- source ~/.venvs/yourapp/bin/activate
- pip install --upgrade pip

- Dev server (SQLite-friendly):

- uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
- For SQLite, avoid multiple workers; stick to single-process in dev.

SQLite tips:

- Use a single writer process; FastAPI with one uvicorn process is fine.
- If using SQLAlchemy, set check_same_thread=False for SQLite if needed.
- Back up the DB file regularly (see “Backups” below).

Process management for dev

- tmux (simple and reliable):

- tmux new -s dev
- Run uvicorn inside it, detach with Ctrl-b d, reattach with tmux a -t dev

- Optional systemd unit if you want auto-start on boot:

- /etc/systemd/system/fastapi-dev.service  
    [Unit]  
    Description=FastAPI dev server  
    After=network-online.target  
      
    [Service]  
    User=ubuntu  
    WorkingDirectory=/home/ubuntu/app  
    EnvironmentFile=/home/ubuntu/app/.env  
    ExecStart=/home/ubuntu/.venvs/yourapp/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload  
    Restart=on-failure  
      
    [Install]  
    WantedBy=multi-user.target
- sudo systemctl daemon-reload && sudo systemctl enable --now fastapi-dev

Secrets, env, and Git hygiene

- .env for local dev (never commit). Use python-dotenv or Pydantic Settings.
- IAM role on EC2 (not static keys) if you need S3/ECR/etc.
- For anything non-trivial, stash secrets in SSM Parameter Store and load at runtime.
- Keep all code in Git remote (GitHub/GitLab). Assume the instance is disposable.

Backups and persistence

- Code in Git = instant recovery.
- SQLite backups (optional but smart):

- Install AWS CLI if you’ll push to S3.
- Cron job to snapshot the DB daily:  
    #!/bin/bash  
    set -e  
    TS=$(date +'%Y%m%d-%H%M%S')  
    cp /home/ubuntu/app/db.sqlite3 /home/ubuntu/app/db-$TS.sqlite3  
    # Optional compress: gzip /home/ubuntu/app/db-$TS.sqlite3  
    # Optional S3 push (requires IAM role or creds):  
    # aws s3 cp /home/ubuntu/app/db-$TS.sqlite3 s3://your-bucket/backups/  
    find /home/ubuntu/app -name 'db-*.sqlite3' -mtime +7 -delete
- Add to crontab: crontab -e → 0 3 * * * /home/ubuntu/app/backup_sqlite.sh

- EBS snapshots before risky changes.

Auto-stop so you don’t burn money

Easiest: schedule a daily stop with a tiny Lambda and an EventBridge rule.

1. Tag your instance: AutoStop=true
2. Create a Lambda (Python) with this code:  
    import boto3, os  
    ec2 = boto3.client('ec2')  
    TAG_KEY = os.getenv('TAG_KEY','AutoStop')  
    TAG_VALUE = os.getenv('TAG_VALUE','true')  
      
    def lambda_handler(event, context):  
        resp = ec2.describe_instances(Filters=[  
            {'Name': f'tag:{TAG_KEY}', 'Values': [TAG_VALUE]},  
            {'Name': 'instance-state-name', 'Values': ['running']}  
        ])  
        ids = [i['InstanceId'] for r in resp['Reservations'] for i in r['Instances']]  
        if ids:  
            ec2.stop_instances(InstanceIds=ids)  
        return {'stopped': ids}
3. Add an EventBridge schedule (e.g., 10pm local) to trigger the Lambda.
4. Optional: a morning “start” rule if you want it to boot before you sit down.

Note: stopping preserves your EBS data; you only pay for storage while stopped. Hibernation can speed resume if supported, but stopping is usually enough.

Security hardening (light but meaningful)

- Keep the Security Group tight (SSH from your IP only).
- UFW enabled (OpenSSH only).
- Fail2ban for SSH brute-force protection.
- Unattended-upgrades for security patches.
- Disable SSH password auth; use keys only (Ubuntu does this by default).

Dev ergonomics

- VS Code Remote SSH: edit/run/debug as if local.
- Pre-commit: ruff, black, isort, mypy for clean diffs and fewer footguns.
- pytest + coverage for fast feedback loops.
- Makefile (or task runner) to codify common commands:  
    .PHONY: dev test fmt lint  
    dev:  
      uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload  
    test:  
      pytest -q  
    fmt:  
      black . && isort .  
    lint:  
      ruff check .

About Vue + Tailwind (only if/when you want)

- Install Node LTS (already in bootstrap).
- Run the Vite dev server and forward port 5173 over SSH.
- Keep it separate from FastAPI during dev for fastest reload cycles.

When to evolve this setup

- Concurrent traffic / multiple devs: move from SQLite to Postgres, switch to Gunicorn with >1 worker, add Nginx.
- Reproducibility: containerize (Dockerfile + docker-compose) and push to ECR later.
- Secrets/permissions growth: standardize with SSM Parameter Store and scoped IAM roles.

Quick start checklist

1. Launch small On-Demand EC2 (Ubuntu LTS), attach 20–30 GB encrypted gp3 EBS.
2. Paste the cloud-init script; add key pair; restrict SG to SSH from your IP.
3. SSH in, create venv, clone repo, install deps.
4. Run FastAPI with uvicorn in tmux; use SSH tunnels for ports 8000/5173.
5. Tag instance AutoStop=true; add the stop-scheduler Lambda + EventBridge.
6. Set up Git remote, .env (untracked), and optional SQLite backup cron.

One more thing

How much interruption pain are you actually willing to tolerate to save a few dollars? If the honest answer is “not much,” let’s stick with On-Demand + auto-stop. If you want Spot, say the word and I’ll give you a resilient Spot recipe (launch template, interruption handling, and data safety playbook).