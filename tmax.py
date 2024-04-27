import geopandas as gpd
import pandas as pd
from tqdm import tqdm
from rasterstats import zonal_stats


def get_zonal_stats_std_mean(zones, directory, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name):
    # Инициализация пустого списка для хранения статистик
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    gdf = gpd.read_file(zones)

    gdf_out = pd.DataFrame()

    for month in tqdm(range(1, 13)):
        # Формирование строки с именем файла для текущего года и месяца
        # wc2.1_2.5m_tmin_GISS-E2-1-G_ssp126_2021-2040
        filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'

        # Вычисление статистик для среза данных
        stats_year = zonal_stats(gdf, filename, stats=["std", "mean"])
        stats = []

        # Добавление года в статистики
        for stat in stats_year:
            stat["years"] = f"{start_year} - {end_year}"

        # Добавление статистик в список
        stats.extend(stats_year)

        # Создание DataFrame из списка статистик
        gdf_stats = pd.DataFrame(stats)

        # Присоединение столбца с годом к DataFrame со статистиками
        #gdf_stats["year"] = gdf_stats["year"].astype(int)
        gdf_stats[join_col_name] = list(gdf[join_col_name]) * int(len(gdf_stats) / len(gdf))
        # Присоединение статистик к исходному DataFrame
        gdf_stats[join_col_name] = gdf_stats[join_col_name].astype(int)
        gdf_stats = gdf_stats.rename(columns={'std': f'{out_col_name}_{months[month - 1]}_std',
                                              'mean': f"{out_col_name}_{months[month - 1]}"})

        if month == 1:
            gdf_out = gdf_stats
        else:
            # Присоединение статистик к исходному DataFrame с использованием join_col_name
            gdf_out = gdf_out.merge(gdf_stats, on=["years", join_col_name], how="outer")

    return gdf_out


def get_zonal_stats_std_mean_1(zones, directory, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name):
    # Инициализация пустого списка для хранения статистик
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    gdf = gpd.read_file(zones)

    gdf_out = pd.DataFrame()

    for month in tqdm(range(1, 13)):
        # Формирование строки с именем файла для текущего года и месяца
        # wc2.1_2.5m_tmin_GISS-E2-1-G_ssp126_2021-2040
        #filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
        filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}_{month}.tif'

        # Вычисление статистик для среза данных
        stats_year = zonal_stats(gdf, filename, stats=["std", "mean"])
        stats = []

        # Добавление года в статистики
        for stat in stats_year:
            stat["model"] = f"{model_type}"
            stat["years"] = f"{start_year} - {end_year}"

        # Добавление статистик в список
        stats.extend(stats_year)

        # Создание DataFrame из списка статистик
        gdf_stats = pd.DataFrame(stats)

        # Присоединение столбца с годом к DataFrame со статистиками
        #gdf_stats["year"] = gdf_stats["year"].astype(int)
        gdf_stats[join_col_name] = list(gdf[join_col_name]) * int(len(gdf_stats) / len(gdf))
        # Присоединение статистик к исходному DataFrame
        gdf_stats[join_col_name] = gdf_stats[join_col_name]#.astype(int)
        gdf_stats = gdf_stats.rename(columns={'std': f'{out_col_name}_{months[month - 1]}_std',
                                              'mean': f"{out_col_name}_{months[month - 1]}"})

        if month == 1:
            gdf_out = gdf_stats
        else:
            # Присоединение статистик к исходному DataFrame с использованием join_col_name
            gdf_out = gdf_out.merge(gdf_stats, on=["model", "years", join_col_name], how="outer")

    return gdf_out

def get_zonal_stats_std_mean_3(zones, directory, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name):
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    gdf = gpd.read_file(zones)
    gdf_out = pd.DataFrame()

    for month in tqdm(range(1, 13)):
        filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}_{month}.tif'

        stats_year = zonal_stats(gdf, filename, stats=["std", "mean"])
        stats = []

        for stat in stats_year:
            stat["model"] = f"{model_type}"
            stat["years"] = f"{start_year} - {end_year}"
            stats.append(stat)

        gdf_stats = pd.DataFrame(stats)

        join_col_values = gdf[join_col_name].tolist()
        join_col_values_repeated = [join_col_values[i % len(join_col_values)] for i in range(len(gdf_stats))]
        gdf_stats[join_col_name] = join_col_values_repeated
        gdf_stats[join_col_name] = gdf_stats[join_col_name].astype(int)
        gdf_stats = gdf_stats.rename(columns={'std': f'{out_col_name}_{months[month - 1]}_std',
                                              'mean': f"{out_col_name}_{months[month - 1]}"})

        if month == 1:
            gdf_out = gdf_stats
        else:
            gdf_out = gdf_out.merge(gdf_stats, on=["years", join_col_name], how="outer")

    return gdf_out

#--------------TEMPERATURE_TMIN----------------
#-----------------------------------------

#--------------1960_1969---------------------
# Путь к файлу с зонами
#zones = "C:/Users/user/Downloads/SHP/MNG/BND_soum.shp"
zones = "C:/Users/user/Downloads/SHP/GA/Regions_GA.shp"

new_order = ['model', 'years', 'NAME_EN', 'Temp_max_jan', 'Temp_max_jan_std', 'Temp_max_feb',	'Temp_max_feb_std',	'Temp_max_mar',	'Temp_max_mar_std',	'Temp_max_apr',	'Temp_max_apr_std',	'Temp_max_may',	'Temp_max_may_std',	'Temp_max_jun',	'Temp_max_jun_std',	'Temp_max_jul',	'Temp_max_jul_std',	'Temp_max_aug',	'Temp_max_aug_std',	'Temp_max_sep',	'Temp_max_sep_std',	'Temp_max_oct',	'Temp_max_oct_std',	'Temp_max_nov',	'Temp_max_nov_std',	'Temp_max_dec',	'Temp_max_dec_std']


# Название столбца для выходного DataFrame (Temp_Ann и Temp_Ann_std)
out_col_name = 'Temp_max'

# Название атрибута для каждого элемента Geometry из Shapefile
join_col_name = 'NAME_EN'

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
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------GISS-E2-1-G---------------------

#--------------GFDL-ESM4---------------------
# Параметры модели
model_type = "GFDL-ESM4"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------GFDL-ESM4---------------------

#--------------FIO-ESM-2-0---------------------
# Параметры модели
model_type = "FIO-ESM-2-0"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------FIO-ESM-2-0---------------------

#--------------EC-Earth3-Veg---------------------
# Параметры модели
model_type = "EC-Earth3-Veg"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------EC-Earth3-Veg---------------------

#--------------CMCC-ESM2---------------------
# Параметры модели
model_type = "CMCC-ESM2"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------CMCC-ESM2---------------------

#--------------BCC-CSM2-MR---------------------
# Параметры модели
model_type = "BCC-CSM2-MR"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)
#--------------BCC-CSM2-MR---------------------

#--------------ACCESS-CM2---------------------
# Параметры модели
model_type = "ACCESS-CM2"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------MPI-ESM1-2-HR---------------------
# Параметры модели
model_type = "MPI-ESM1-2-HR"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------INM-CM5-0---------------------
# Параметры модели
model_type = "INM-CM5-0"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------HadGEM3-GC31-LL---------------------
# Параметры модели
model_type = "HadGEM3-GC31-LL"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------MRI-ESM2-0---------------------
# Параметры модели
model_type = "MRI-ESM2-0"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------MIROC6---------------------
# Параметры модели
model_type = "MIROC6"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

#--------------UKESM1-0-LL---------------------
# Параметры модели
model_type = "UKESM1-0-LL"
print(f"{out_col_name} {zones} {start_year}-{end_year}")
print("Вызов функции вычисления статистики")

tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)
tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)