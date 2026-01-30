import matplotlib.pyplot as plt

from src.config.constants import LABELED_DATASET_FILE
from src.utils.parser import parse_dataset
from src.stats.descriptive import mean, std, min_value


def find_homogeneous_course(dataset):
    courses = dataset.select_dtypes(include=['int', 'float']).columns
    courses = [c for c in courses if c != 'Index']

    houses = dataset['Hogwarts House'].unique()
    homogeneity = {}

    for course in courses:
        means = []

        for house in houses:
            values = []
            for v in dataset[dataset['Hogwarts House'] == house][course]:
                if isinstance(v, (int, float)) and v == v:
                    values.append(v)

            if len(values) > 0:
                means.append(mean(values))

        if len(means) > 1:
            homogeneity[course] = std(means)
        else:
            homogeneity[course] = float("inf")

    best_course = min_value(homogeneity, key=homogeneity.get)
    return best_course, homogeneity

def plot_homogeneity(homogeneity):
    courses = list(homogeneity.keys())
    stds = list(homogeneity.values())

    plt.figure(figsize=(12,6))
    plt.bar(courses, stds, edgecolor='black')
    plt.ylabel("Std of mean scores across houses")
    plt.title("Homogeneity of Hogwarts courses (lower = more homogeneous)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    try:
        dataset = parse_dataset(LABELED_DATASET_FILE)
        best_course, homogeneity = find_homogeneous_course(dataset)
        print(f"The most homogeneous Hogwarts course is: {best_course}")
        plot_homogeneity(homogeneity)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
