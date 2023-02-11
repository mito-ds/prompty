# prompty
Find me a prompt, why don't you.

# Usage

Setup with:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, export your Open AI key with:
```
export OPENAI_API_KEY="sk-..."
```

Then, tun with:
```
python -m prompty eval
```

See the results of that evaluation with
```
python -m prompty load
```