import os
from idlelib.run import Executive

import models_comparer

# -----------------------COMMON----------------------#
# Исходный путь
path = os.getcwd()

# Удаление последнего элемента из пути
project_dir = os.path.dirname(path)

data_types = ["tmin", "tmax", "prec"]

models = ["GISS-E2-1-G", "GFDL-ESM4", "FIO-ESM-2-0", "EC-Earth3-Veg", "CMCC-ESM2",
          "BCC-CSM2-MR", "ACCESS-CM2", "MPI-ESM1-2-HR", "INM-CM5-0", "HadGEM3-GC31-LL",
          "MRI-ESM2-0", "MIROC6", "UKESM1-0-LL", "IPSL-CM6A-LR"]

ssp_types = [ "ssp245", "ssp370", "ssp585"]
start_year = 2021
end_year = 2040

output_dir = "common_model_stats_12-09-2024"
models_comparer_instance = models_comparer.ModelsComparer(models)

#input_dir = f"C:\\Users\\user\Downloads\\all_models_world_clim_{start_year}-{end_year}\\{data_type}\\wc2.1_2.5m_{data_type}_ssp245_2021-2040"

for ssp_type in ssp_types:
    for data_type in data_types:
        try:
            folder = f"GA\\{ssp_type}_{start_year}-{end_year}\\{data_type}"

            models_comparer_instance.models_compare(folder, project_dir, data_type, ssp_type, start_year, end_year)
            output = models_comparer_instance.get_result_df()

            output.to_csv(project_dir + "\\GA\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_{start_year}-{end_year}.csv")
            output.to_excel(project_dir +  "\\GA\\"  + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_{start_year}-{end_year}.xlsx")

            print(f"файл схранен: {project_dir}\\GA\\{output_dir}\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_{start_year}-{end_year}")

        except Exception as ex:
            print(f"Растр для {ssp_type} не найден: {ex}")