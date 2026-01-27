import pandas as pd
import matplotlib.pyplot as plt

DATASET_FILE = "datasets/dataset_train.csv"

def parse_dataset(filename):
    dataset = pd.read_csv(filename)
    if dataset.shape[0] == 0 or dataset.shape[1] == 0:
        raise ValueError("Empty or invalid CSV")
    if 'Hogwarts House' not in dataset.columns:
        raise ValueError("CSV must contain 'Hogwarts House' column")
    return dataset

def find_homogeneous_course(dataset):
    courses = dataset.select_dtypes(include=['int', 'float']).columns
    courses = [c for c in courses if c != 'Index']

    houses = dataset['Hogwarts House'].unique()
    homogeneity = {}

    for course in courses:
        means = []
        for house in houses:
            scores = dataset[dataset['Hogwarts House'] == house][course].dropna()
            means.append(scores.mean())
        homogeneity[course] = pd.Series(means).std()

    best_course = min(homogeneity, key=homogeneity.get)
    return best_course, homogeneity

def plot_homogeneity(homogeneity):
    courses = list(homogeneity.keys())
    stds = list(homogeneity.values())

    plt.figure(figsize=(12,6))
    plt.bar(courses, stds, color='skyblue', edgecolor='black')
    plt.ylabel("Std of mean scores across houses")
    plt.title("Homogeneity of Hogwarts courses (lower = more homogeneous)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    try:
        dataset = parse_dataset(DATASET_FILE)
        best_course, homogeneity = find_homogeneous_course(dataset)
        print(f"The most homogeneous Hogwarts course is: {best_course}")
        plot_homogeneity(homogeneity)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
