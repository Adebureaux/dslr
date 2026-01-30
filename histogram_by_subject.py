import matplotlib.pyplot as plt
import pandas as pd


def histogramOfHogwartsSubjects():
    """
    Histogram of every subject and the frequency of their grades
        depending on their houses
    """
    df = pd.read_csv('datasets/dataset_train.csv')

    house_colors = {
        'Gryffindor': '#a6332e',
        'Slytherin': '#366447',
        'Ravenclaw': '#3c4e91',
        'Hufflepuff': '#efbc2f'
    }

    subject_columns = df.columns[6:]
    n_subjects = len(subject_columns)
    n_cols = 5
    n_rows = (n_subjects + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 4*n_rows))
    axes = axes.flatten()

    for idx, subject in enumerate(subject_columns):
        ax = axes[idx]
        data_to_plot = df[['Hogwarts House', subject]].dropna()

        for house in ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']:
            house_data = data_to_plot[data_to_plot['Hogwarts House']
                                      == house][subject]
            if len(house_data) > 0:
                ax.hist(house_data,
                        bins=30,
                        alpha=0.6,
                        label=house,
                        color=house_colors.get(house, 'gray')
                        )

        ax.set_xlabel('Score')
        ax.set_ylabel('Frequency')
        ax.set_title(subject)
        ax.legend()
        ax.grid(True, alpha=0.3)

    for idx in range(n_subjects, len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    plt.show()


def main():
    histogramOfHogwartsSubjects()


if __name__ == "__main__":
    main()
