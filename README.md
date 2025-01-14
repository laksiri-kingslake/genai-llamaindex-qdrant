# GenAI Pipelines Leveraging LlamaIndex, Qdrant and MLflow for Advanced Indexing

## Configure your environment

```bash
# Linux
# Install python3-full
sudo apt-get install python3-full

# Create a virtual environment - Linux
python3 -m venv venv
source venv/bin/activate

# Create a virtual environment - Windows
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## Configure VS Code Remote SSH
1. Key pair
```bash
# Generate key pair in local machine - if not don already
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key to the remote host
ssh-copy-id -i ~/.ssh/id_ed25519.pub ubuntu@ai.devbits.click

# If aove doesn't work copy ~/.ssh/id_ed25519.pub manualy to the remote host and execute
cat id_ed25519.pub >> ~/.ssh/authorized_keys
```
2. VS Code setup
```bash
code ~/.ssh/config
```
```plaintext
Host ai.devbits.click
  HostName ai.devbits.click
  User ubuntu
  IdentityFile ~/.ssh/id_ed25519
```
3. Connect to Your EC2 Instance in VS Code
- Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
- Select Remote-SSH: Connect to Host.
- Choose ai.devbits.click from the list.

## References

- https://blog.stackademic.com/building-robust-genai-pipelines-leveraging-llamaindex-qdrant-and-mlflow-for-advanced-indexing-c3293be5735c
- https://blog.stackademic.com/building-robust-genai-pipelines-leveraging-llamaindex-qdrant-and-mlflow-for-advanced-indexing-08441e1c8809
