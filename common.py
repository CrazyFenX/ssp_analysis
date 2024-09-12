import geopandas as gpd
import pandas as pd
from rasterio import RasterioIOError
from tqdm import tqdm
from rasterstats import zonal_stats


def get_zonal_stats_std_mean_1(zones, directory, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name):
    # Инициализация пустого списка для хранения статистик
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    gdf = gpd.read_file(zones)

    gdf_out = pd.DataFrame()

    for month in tqdm(range(1, 13)):
        # Формирование строки с именем файла для текущего года и месяца
        # wc2.1_2.5m_tmin_GISS-E2-1-G_ssp126_2021-2040
        filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.tif'
        #filename = f'{directory}wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}/wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}_{month}.tif'

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

#--------------TEMPERATURE_TMIN----------------
#-----------------------------------------

# Путь к файлу с зонами
zones = "C:/Users/user/Downloads/GA/Regions_GA.shp"

new_order = ['model', 'years', 'NAME_EN', 'Temp_min_jan', 'Temp_min_jan_std', 'Temp_min_feb',	'Temp_min_feb_std',	'Temp_min_mar',	'Temp_min_mar_std',	'Temp_min_apr',	'Temp_min_apr_std',	'Temp_min_may',	'Temp_min_may_std',	'Temp_min_jun',	'Temp_min_jun_std',	'Temp_min_jul',	'Temp_min_jul_std',	'Temp_min_aug',	'Temp_min_aug_std',	'Temp_min_sep',	'Temp_min_sep_std',	'Temp_min_oct',	'Temp_min_oct_std',	'Temp_min_nov',	'Temp_min_nov_std',	'Temp_min_dec',	'Temp_min_dec_std']

# Название столбца для выходного DataFrame (Temp_Ann и Temp_Ann_std)
out_col_name = 'Temp_min'

# Название атрибута для каждого элемента Geometry из Shapefile
join_col_name = 'NAME_EN'

# Путь к растрам
#geotiff_folder = 'C:/Users/user/Downloads/all_models_world_clim_2021-2040/tmin/wc2.1_2.5m_tmin_ssp245_2021-2040/'
#geotiff_folder = 'C:/Users/user/Downloads/cmip_wc_ssp126_GA_tmin/'

#begin------------COMMON---------------------

# Начало и конец периода
start_year = 2021
end_year = 2040

#data_type = "tmin"
#data_type = "tmax"
data_type = "prec"

#ssp_type = "ssp126"
#ssp_type = "ssp245"
#ssp_type = "ssp370"
ssp_type = "ssp585"

# Путь к растрам
geotiff_folder = f'C:/Users/user/Downloads/all_models_world_clim_{start_year}-{end_year}/{data_type}/wc2.1_2.5m_{data_type}_{ssp_type}_{start_year}-{end_year}/'

print(geotiff_folder)

#models = ["GISS-E2-1-G", "GFDL-ESM4", "FIO-ESM-2-0", "EC-Earth3-Veg", "CMCC-ESM2",
#          "BCC-CSM2-MR", "ACCESS-CM2", "MPI-ESM1-2-HR", "INM-CM5-0", "HadGEM3-GC31-LL",
#          "MRI-ESM2-0", "MIROC6", "UKESM1-0-LL", "IPSL-CM6A-LR"]

models = ["IPSL-CM6A-LR"]

for model_type in models:
    print(f"{out_col_name} {zones} {start_year}-{end_year}")
    print("Вызов функции вычисления статистики")

    try:
        tmin_2021_2040 = get_zonal_stats_std_mean_1(zones, geotiff_folder, start_year, end_year, data_type, model_type, ssp_type, out_col_name, join_col_name)

        tmin_2021_2040 = tmin_2021_2040.reindex(columns=new_order)

        tmin_2021_2040.to_csv(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.csv', index=False)
        tmin_2021_2040.to_excel(f'wc2.1_2.5m_{data_type}_{model_type}_{ssp_type}_{start_year}-{end_year}.xlsx', index=False)

    except RasterioIOError as e:
        print(f"Растр для {model_type} не найден: {e}")

#end--------------COMMON---------------------
