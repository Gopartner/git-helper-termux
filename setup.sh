#!/data/data/com.termux/files/usr/bin/bash

# Cari file Python utama (*.py) di folder ini
SOURCE_FILE=$(ls *.py | head -n 1)

# Validasi file Python ditemukan
if [[ -z "$SOURCE_FILE" ]]; then
    echo "Tidak ada file Python ditemukan di folder ini!"
    exit 1
fi

# Minta nama CLI dari user
read -p "Masukkan nama CLI yang ingin kamu gunakan (misal: git-helper): " CLI_NAME

if [[ -z "$CLI_NAME" ]]; then
    echo "Nama CLI tidak boleh kosong!"
    exit 1
fi

TARGET_PATH="$HOME/bin/$CLI_NAME"

# Buat ~/bin jika belum ada
if [ ! -d "$HOME/bin" ]; then
    echo "Membuat folder ~/bin..."
    mkdir -p "$HOME/bin"
fi

# Tambahkan ke PATH jika belum
if ! echo "$PATH" | grep -q "$HOME/bin"; then
    echo "Menambahkan ~/bin ke PATH..."
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc" 2>/dev/null
    export PATH="$HOME/bin:$PATH"
fi

# Bikin bisa dieksekusi
chmod +x "$SOURCE_FILE"

# Buat symlink ke ~/bin
ln -sf "$(pwd)/$SOURCE_FILE" "$TARGET_PATH"

# Info
echo -e "\nSukses! Sekarang kamu bisa jalankan CLI ini dengan perintah:"
echo -e "  \033[1;32m$CLI_NAME\033[0m"
echo -e "\nCek lokasi CLI:"
echo -e "  \033[1;34mwhich $CLI_NAME\033[0m => $(which $CLI_NAME 2>/dev/null)"

hash -r

