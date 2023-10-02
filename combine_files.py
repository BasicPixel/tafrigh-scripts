import os


# TODO: fix files sort, see: natsort package

# Assign directory
directory = "./text/"

# Create file
file = open("./output/result.txt", "w", encoding="utf-8")

# Init result variable
text = ""

# Iterate over files in directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        f = open(os.path.join(root, filename), "r", encoding="utf-8")
        content = f.read()
        filename_without_ext = os.path.splitext(filename)[0]

        text = text + filename_without_ext + "\n\n" + content + "\n\n---\n\n"

file.write(text)
