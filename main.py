import pandas as pd

from src.data_table import *
from src.analyse_image import *
from src.extract_image import *


def main():
    data_dict = create_empty_table()

    extract_images_from_pdf()

    for image_name in os.listdir('images'):
        analyse_image(data_dict, image_name)
        print("Analysed " + image_name + " ...")

    data = pd.DataFrame.from_dict(data_dict)
    data.to_csv('data.csv')


if __name__ == "__main__":
    main()
