import os
import csv

# CHANGE THIS to your folder path
base_path = "products"

output_file = "output.csv"

def collect_files(base_path):
    data = []

    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)

        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)

                if os.path.isfile(file_path):
                    data.append([filename, category])

    return data


def save_to_csv(data, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Category"])

        for row in data:
            writer.writerow(row)


def main():
    print("Processing files...")

    data = collect_files(base_path)
    save_to_csv(data, output_file)

    print(f"Done! {len(data)} files saved to {output_file}")


if __name__ == "__main__":
    main()