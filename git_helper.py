#!/usr/bin/env python3
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)

commands = [
    ("0", "Keluar", "Keluar dari program", []),
    ("1", "git status", "Lihat status file", []),
    ("2", "git add", "Tambah file ke staging", ["<file>"]),
    ("3", "git commit -m", "Commit perubahan", ["<pesan>"]),
    ("4", "git push", "Kirim ke remote (kerja tim)", []),
    ("5", "git pull", "Tarik perubahan dari remote", []),
    ("6", "git log", "Lihat riwayat commit", []),
    ("7", "git diff", "Lihat perbedaan file yang diubah", []),
    ("8", "git checkout", "Pindah cabang", ["<branch>"]),
    ("9", "git checkout -b", "Buat & pindah ke cabang baru", ["<branch>"]),
    ("10", "git branch", "Lihat semua cabang", []),
    ("11", "git merge", "Gabungkan cabang", ["<branch>"]),
    ("12", "git clone", "Clone repo dari remote", ["<url>"]),
    ("13", "git remote -v", "Lihat daftar remote", []),
    ("14", "git remote add origin", "Tambahkan remote baru", ["<url>"]),
    ("15", "git fetch", "Ambil update tanpa merge", []),
    ("16", "git rebase", "Susun ulang commit", ["<branch>"]),
    ("17", "git reset --hard HEAD~1", "Hapus commit terakhir", []),
    ("18", "git revert", "Balikkan commit", ["<commit>"]),
    ("19", "git stash", "Simpan sementara perubahan", []),
    ("20", "git stash apply", "Terapkan perubahan dari stash", []),
    ("21", "git cherry-pick", "Ambil commit dari branch lain", ["<commit>"]),
    ("22", "git tag", "Tandai commit", ["<tag>"]),
    ("23", "git show", "Lihat detail commit", ["<commit>"]),
    ("24", "git clean -fd", "Hapus file untracked", []),
    ("25", "git archive", "Export project jadi zip/tar", []),
    ("26", "git switch", "Pindah cabang (alternatif)", ["<branch>"]),
    ("27", "git switch -c", "Buat cabang baru (alternatif)", ["<branch>"]),
    ("28", "git restore", "Kembalikan file", ["<file>"]),
    ("29", "git checkout --", "Restore versi lama", ["<file>"]),
    ("30", "git log --oneline --graph", "Riwayat commit grafis", []),
]

def tampilkan_header():
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "  CLI Git Tool - by Yudibilly")
    print(Fore.GREEN + "  YouTube: https://youtube.com/@newbiegan3909")
    print(Fore.GREEN + "  Facebook: https://www.facebook.com/yudibilly")
    print(Fore.GREEN + "  GitHub: https://github.com/Gopartner")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)

def run_git_command(base_cmd, args):
    cmd = base_cmd.split() + args
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(Fore.GREEN + result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "\nError:")
        print(e.stderr or str(e))

def input_args(params):
    args = []
    for p in params:
        v = input(Fore.CYAN + f"Masukkan {p.strip('<>')}: ").strip()
        if not v:
            print(Fore.RED + f"Input {p} wajib diisi!")
            return None
        args.append(v)
    return args

def keluar_program():
    print(Fore.MAGENTA + "\nKeluar dari program. Sampai jumpa!\n")
    tampilkan_header()

def main():
    tampilkan_header()
    while True:
        print(Fore.YELLOW + "\nPilih perintah Git yang ingin dijalankan:")
        for num, cmd, desc, params in commands:
            print(f"{Fore.LIGHTYELLOW_EX}{num}. {Fore.GREEN}{cmd} {' '.join(params)} {Fore.WHITE}- {desc}")
        pilih = input(Fore.CYAN + "\nNomor perintah: ").strip()

        if pilih == "0":
            keluar_program()
            break

        cmd_data = next((c for c in commands if c[0] == pilih), None)
        if not cmd_data:
            print(Fore.RED + "Pilihan tidak valid!")
            continue

        base_cmd, params = cmd_data[1], cmd_data[3]
        args = []
        if params:
            args = input_args(params)
            if args is None:
                print(Fore.RED + "Perintah dibatalkan karena input tidak lengkap.")
                continue

        run_git_command(base_cmd, args)

        kembali = input(Fore.YELLOW + "\nkembali ke menu (y/n): ").strip().lower()
        if kembali != "y":
            keluar_program()
            break

if __name__ == "__main__":
    main()

