import yaml, os

for file in os.listdir("../configs"):
    if file.endswith(".yml"):
        with open(f"../configs/{file}") as f:
            yaml.safe_load(f)

print("Tous les fichiers YAML sont valides.")
