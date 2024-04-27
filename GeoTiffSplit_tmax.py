import rasterio
from tqdm import tqdm

def split_multiband_geotiff(input_file, output_prefix):
    with rasterio.open(input_file) as src:
        for i in tqdm(range(src.count)):
            output_file = f"{output_prefix}_{i + 1}.tif"

            profile = src.profile
            profile.update(count=1, dtype=src.dtypes[i])

            with rasterio.open(output_file, 'w', **profile) as dst:
                dst.write(src.read(i + 1), 1)


# Пример использования

# Путь к растрам
geotiff_folder = 'C:/Users/user/Downloads/cmip_wc_ssp126_GA_tmax/'

#--------------GISS-E2-1-G---------------------
# Начало и конец периода
start_year = 2021
end_year = 2040

data_type = "tmax"
ssp_type = "ssp126"

# Параметры модели
model_type = "GISS-E2-1-G"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------GFDL-ESM4---------------------
# Параметры модели
model_type = "GFDL-ESM4"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------FIO-ESM-2-0---------------------
# Параметры модели
model_type = "FIO-ESM-2-0"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------EC-Earth3-Veg---------------------
# Параметры модели
model_type = "EC-Earth3-Veg"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------CMCC-ESM2---------------------
# Параметры модели
model_type = "CMCC-ESM2"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------BCC-CSM2-MR---------------------
# Параметры модели
model_type = "BCC-CSM2-MR"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------ACCESS-CM2---------------------
# Параметры модели
model_type = "ACCESS-CM2"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------MPI-ESM1-2-HR---------------------
# Параметры модели
model_type = "MPI-ESM1-2-HR"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------INM-CM5-0---------------------
# Параметры модели
model_type = "INM-CM5-0"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------HadGEM3-GC31-LL---------------------
# Параметры модели
model_type = "HadGEM3-GC31-LL"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------MRI-ESM2-0---------------------
# Параметры модели
model_type = "MRI-ESM2-0"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#--------------MIROC6---------------------
# Параметры модели
model_type = "MIROC6"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)

#-------------UKESM1-0-LL---------------------
# Параметры модели
model_type = "UKESM1-0-LL"
print(f"{data_type} {model_type} {ssp_type} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

input_file = f'{geotiff_folder}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
output_prefix = f'{geotiff_folder}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}'

split_multiband_geotiff(input_file, output_prefix)
