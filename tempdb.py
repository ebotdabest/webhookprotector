import json

def add_webhook(user, url, discord_id):
    with open("db.json", "r") as f:
        data = json.load(f)

    try:
        data[user].append({
            "url": url,
            "allowed_ips": [],
            "allowed_domains": [],
            "id": discord_id
        })
    except KeyError:
        data[user] = []
        data[user].append({
            "url": url,
            "allowed_ips": [],
            "allowed_domains": []
        })

    with open("db.json", "w") as f:
        json.dump(data, f)

def add_ip(user, url, ip):
    with open("db.json", "r") as f:
        data = json.load(f)

    hooks = data[user]

    for num in range(len(hooks)):
        if hooks[num]["url"] == url:
            hooks[num]["allowed_ips"].append(ip)

    with open("db.json", "w") as f:
        json.dump(data, f)

def add_domain(user, url, domain):
    with open("db.json", "r") as f:
        data = json.load(f)

    hooks = data[user]

    for num in range(len(hooks)):
        if hooks[num]["url"] == url:
            hooks[num]["allowed_domains"].append(domain)

    with open("db.json", "w") as f:
        json.dump(data, f)

def remove_webhook(user, url):

    with open("db.json", "r") as f:
        data = json.load(f)

    hooks = data[user]

    for num in range(len(hooks)):
        try:
            if hooks[num]["url"] == url:
                hooks.remove(hooks[num])
        except Exception:
            pass
    with open("db.json", "w") as f:
        json.dump(data, f)

def remove_ip(user, url, ip):
    with open("db.json", "r") as f:
        data = json.load(f)

    hooks = data[user]

    for num in range(len(hooks)):
        if hooks[num]["url"] == url:
            hooks[num]["allowed_ips"].remove(ip)

    with open("db.json", "w") as f:
        json.dump(data, f)


def remove_domain(user, url, domain):
    with open("db.json", "r") as f:
        data = json.load(f)

    hooks = data[user]

    for num in range(len(hooks)):
        if hooks[num]["url"] == url:
            hooks[num]["allowed_domains"].remove(domain)

    with open("db.json", "w") as f:
        json.dump(data, f)

def get_webhook(user, hookid):
    with open("db.json", "r") as f:
        data = json.load(f)
        hooks = data[user]

    for hook in hooks:
        if hook["id"] == hookid:
            return hook
#
# add_webhook("henry", "url", "psjja")