import os
import platform
import time

def ping(host: str, count: int = 2) -> bool:
    system = platform.system().lower()
    # Windows usa -n, Linux/macOS usa -c
    flag = "-n" if system.startswith("win") else "-c"
    cmd = f"ping {flag} {count} {host}"
    return os.system(cmd) == 0

def read_hosts(file_path: str) -> list[str]:
    hosts = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            h = line.strip()
            if h and not h.startswith("#"):
                hosts.append(h)
    return hosts

def main():
    print("🔧 Network Diagnostic Tool (v2) - Multi-host Ping\n")

    file_path = "hosts.txt"
    try:
        hosts = read_hosts(file_path)
    except FileNotFoundError:
        print(f"❌ Arquivo '{file_path}' não encontrado. Crie ele com um host por linha.")
        return

    if not hosts:
        print(f"❌ O arquivo '{file_path}' está vazio. Adicione pelo menos 1 host.")
        return

    start = time.time()
    ok_count = 0

    for host in hosts:
        print(f"➡️  Testando: {host}")
        ok = ping(host, count=2)
        if ok:
            print("   ✅ OK\n")
            ok_count += 1
        else:
            print("   ❌ FALHA\n")

    total = time.time() - start
    print("📌 Resumo")
    print(f"- Hosts testados: {len(hosts)}")
    print(f"- Sucesso: {ok_count}")
    print(f"- Falha: {len(hosts) - ok_count}")
    print(f"- Tempo total: {total:.2f}s")

if __name__ == "__main__":
    main()