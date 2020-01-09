
import pytesseract
import cv2
import os
import pandas as pd
import numpy as np


def get_top_10_words():
    top_10_words = np.array()
    return top_10_words


def get_tagged_values():
    tagged_values = pd.DataFrame(columns=['text', 'x1', 'y1', 'x2', 'y2'])
    return tagged_values


def calculate_coordinate(u, v):
    return u+v


def get_data_coordinates(filepath, filename):
    img = cv2.imread(os.path.join(filepath, filename))
    df = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)
    output_df = pd.DataFrame(columns=['text', 'x1', 'y1', 'x2', 'y2'])
    output_df[['text', 'x1', 'y1']] = df[['text', 'left', 'top']]
    output_df['x2'] = calculate_coordinate(df['left'], df['width'])
    output_df['y2'] = calculate_coordinate(df['top'], df['height'])
    return output_df


def filter_top_10_words(top_10_words, data_df):
    return data_df[data_df.text in top_10_words]


def filter_tagged_values(tagged_values, data_df):
    return data_df[data_df.text in tagged_values.text]


def join_filtered_df_by_row(filtered_top_10, filtered_tagged_value):
    return pd.concat([filtered_top_10, filter_tagged_values], axis=0)
