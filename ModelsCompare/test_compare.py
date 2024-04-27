import os
import pandas as pd
import glob
import numpy as np
from scipy import stats

max_values = []
min_values = []
max_models = []
min_models = []
confidence_intervals = []
months = []
zones = []

# Получение текущей директории проекта
# project_dir = os.getcwd()

# Исходный путь
path = os.getcwd()

# Удаление последнего элемента из пути
project_dir = os.path.dirname(path)

folder = "GA"

data_type = "prec"

models = ["GISS-E2-1-G", "GFDL-ESM4", "FIO-ESM-2-0", "EC-Earth3-Veg", "CMCC-ESM2",
          "BCC-CSM2-MR", "ACCESS-CM2", "MPI-ESM1-2-HR", "INM-CM5-0", "HadGEM3-GC31-LL",
          "MRI-ESM2-0", "MIROC6", "UKESM1-0-LL"]

ssp_type = "ssp126"
start_year = 2021
end_year = 2040

folder_path = os.path.abspath(folder)  # Получение абсолютного пути к папке

full_df = pd.DataFrame()

for model in models:
    tmp_df = pd.read_csv(project_dir + "\\" + folder + f"\\wc2.1_2.5m_{data_type}_{model}_{ssp_type}_2021-2040.csv")
    # Слияние DataFrame
    full_df = pd.concat([full_df, tmp_df])

for month in full_df.columns[3:]:
    print("-", month)
    for zone_name in full_df['NAME_EN'].unique():
        print("---", zone_name)
        values = []
        values.extend(full_df[month][full_df['NAME_EN'] == zone_name].dropna().values)

        print(values)

        max_value = np.max(values)
        min_value = np.min(values)
        if len(full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == max_value)]["model"].values) > 1:
            model_max = full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == max_value)]["model"].values
        else:
            model_max = full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == max_value)]["model"].values[0]

        if len(full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == min_value)]["model"].values) > 1:
            model_min = full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == min_value)]["model"].values
        else:
            model_min = full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == min_value)]["model"].values[0]

        #model_min = full_df[(full_df['NAME_EN'] == zone_name) & (full_df[month] == min_value)]["model"].values[0]
        confidence_interval = stats.t.interval(0.95, len(values) - 1, loc=np.mean(values),
                                               scale=stats.sem(values))

        max_values.append(max_value)
        min_values.append(min_value)
        max_models.append(model_max)
        min_models.append(model_min)
        confidence_intervals.append(confidence_interval)
        months.append(month)
        zones.append(zone_name)


for i in range(len(full_df.columns[3:])):
    print(f"Столбец {full_df.columns[3:][i]}:")
    print(f"Максимальное значение: {max_values[i]} {max_models[i]}")
    print(f"Минимальное значение: {min_values[i]} {min_models[i]}")
    print(f"Доверительный интервал (95%): {confidence_intervals[i]}")

output = pd.DataFrame({'zone': zones, 'month': months, 'max_value': max_values, 'max_model': max_models, 'min_value': min_values, 'min_model': min_models, 'confidence_intervals': confidence_intervals})

print(output)

output_dir = "common_model_stats"

output.to_csv(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.csv")
output.to_excel(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.xlsx")