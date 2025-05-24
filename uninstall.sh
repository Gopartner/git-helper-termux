#!/data/data/com.termux/files/usr/bin/bash

echo -e "\n=== UNINSTALLER GIT CLI ==="

# Minta nama CLI yang ingin dihapus
read -p "Masukkan nama CLI yang ingin dihapus (contoh: git-helper): " CLI_NAME

if [[ -z "$CLI_NAME" ]]; then
    echo "Nama CLI tidak boleh kosong!"
    exit 1
fi

# Path target symlink
TARGET_PATH="$HOME/bin/$CLI_NAME"

# Hapus symlink jika ada
if [[ -L "$TARGET_PATH" ]]; then
    echo "Menghapus symlink: $TARGET_PATH"
    rm "$TARGET_PATH"
    echo "Berhasil dihapus."
else
    echo "Tidak ditemukan symlink dengan nama '$CLI_NAME' di ~/bin"
fi

# Opsional: hapus file python utama juga?
read -p "Sekalian hapus file program aslinya juga? (y/n): " DELETE_SOURCE
if [[ "$DELETE_SOURCE" == "y" ]]; then
    SOURCE_FILE="$(ls *.py | grep -i "$CLI_NAME" | head -n1)"
    if [[ -f "$SOURCE_FILE" ]]; then
        echo "Menghapus file asli: $SOURCE_FILE"
        rm "$SOURCE_FILE"
    else
        echo "File asli tidak ditemukan."
    fi
fi

echo -e "\nUninstall selesai."

