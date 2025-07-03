import requests

# 🔧 Configurație
GITHUB_USER = "Put-your-GitHub-Username"
TOKEN = "Put-your-Token"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_all_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Eroare la pagina {page}: {r.status_code} – {r.text}")
            break
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def delete_repo(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}"
    r = requests.delete(url, headers=headers)
    if r.status_code == 204:
        print(f"[✔] Șters: {repo_name}")
    else:
        print(f"[✘] Eșec la: {repo_name} – {r.status_code} – {r.text}")

def main():
    print("🔍 Caut toate repository-urile...")
    repos = get_all_repos()
    print(f"➡️ Am găsit {len(repos)} repo-uri.")

    for repo in repos:
        print(f" - {repo['name']}")

    confirm = input(" Ești ABSOLUT SIGUR că vrei să le ștergi pe toate? Scrie exact: STERGE TOT\n> ").strip()
    if confirm != "STERGE TOT":
        print(" Operațiune anulată.")
        return

    print(" Încep ștergerea...")
    for repo in repos:
        delete_repo(repo["name"])

if __name__ == "__main__":
    main()
