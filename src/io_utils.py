import csv

def load_csv(path):
    """
    Load a CSV file and return a list of tuples (word, score).
    """
    data = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                word = row[0].strip()
                try:
                    score = float(row[1])
                except ValueError:
                    continue
                data.append((word, score))
    return data


def save_csv(path, data):
    """
    Save a list of tuples (word, score) into a CSV file.
    """
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for word, score in data:
            writer.writerow([word, score])
