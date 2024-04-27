import os
import models_comparer

# -----------------------PRECIPITATION----------------------#
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

output_dir = "common_model_stats"
models_comparer_instance = models_comparer.ModelsComparer(models)

models_comparer_instance.models_compare(folder, project_dir, data_type, ssp_type, start_year, end_year)
output = models_comparer_instance.get_result_df()

output.to_csv(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.csv")
output.to_excel(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.xlsx")


# -----------------------TEMPERATURE MAX----------------------#
# Исходный путь
path = os.getcwd()

# Удаление последнего элемента из пути
project_dir = os.path.dirname(path)

folder = "GA"

data_type = "tmax"

models = ["GISS-E2-1-G", "GFDL-ESM4", "FIO-ESM-2-0", "EC-Earth3-Veg", "CMCC-ESM2",
          "BCC-CSM2-MR", "ACCESS-CM2", "MPI-ESM1-2-HR", "INM-CM5-0", "HadGEM3-GC31-LL",
          "MRI-ESM2-0", "MIROC6", "UKESM1-0-LL"]

ssp_type = "ssp126"
start_year = 2021
end_year = 2040

output_dir = "common_model_stats"
models_comparer_instance = models_comparer.ModelsComparer(models)

models_comparer_instance.models_compare(folder, project_dir, data_type, ssp_type, start_year, end_year)
output = models_comparer_instance.get_result_df()

output.to_csv(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.csv")
output.to_excel(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.xlsx")


# -----------------------TEMPERATURE MIN----------------------#
# Исходный путь
path = os.getcwd()

# Удаление последнего элемента из пути
project_dir = os.path.dirname(path)

folder = "GA"

data_type = "tmin"

models = ["GISS-E2-1-G", "GFDL-ESM4", "FIO-ESM-2-0", "EC-Earth3-Veg", "CMCC-ESM2",
          "BCC-CSM2-MR", "ACCESS-CM2", "MPI-ESM1-2-HR", "INM-CM5-0", "HadGEM3-GC31-LL",
          "MRI-ESM2-0", "MIROC6", "UKESM1-0-LL"]

ssp_type = "ssp126"
start_year = 2021
end_year = 2040

output_dir = "common_model_stats"
models_comparer_instance = models_comparer.ModelsComparer(models)

models_comparer_instance.models_compare(folder, project_dir, data_type, ssp_type, start_year, end_year)
output = models_comparer_instance.get_result_df()

output.to_csv(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.csv")
output.to_excel(project_dir + "\\" + folder + "\\" + output_dir + f"\\common_stats_wc2.1_2.5m_{data_type}_{ssp_type}_2021-2040.xlsx")
