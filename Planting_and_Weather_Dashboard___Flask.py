from flask import Flask, render_template, request, redirect
from plant_dashboard import crops_stream_SQL_output
from noaa_weather_api import get_noaa_weather
from noaa_weather_api import forecast_image
from plant_dashboard import epsom_update_button
from plant_dashboard import neem_oil_update_button
from plant_dashboard import fertilizer_update_button
from plant_dashboard import neem_oil_result
from plant_dashboard import epsom_salt_result
from plant_dashboard import fertilizer_result
from localnewsrss import news_feed
from recipiesrss import food_news_feed

import pandas as pd
dfcrop = pd.DataFrame(crops_stream_SQL_output(), columns =['Crop', 'Planting Start', 'Planting End'])
dfweather = pd.DataFrame(get_noaa_weather())
curr_forecast_df = get_noaa_weather()
forecast_text = str(curr_forecast_df.iloc[0, 2])
lower_forecast_text = str.lower(forecast_text)

app = Flask(__name__, template_folder='Templates')

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form.get('neemaction') == 'Neem Oil Applied':
            neem_oil_update_button()
            return redirect('/')
        elif request.form.get('epsomaction') == 'Epsom Salt Applied':
            epsom_update_button()
        elif request.form.get('fertaction') == 'Fertilizer Applied':
            fertilizer_update_button()
        else:
            dfcrop = pd.DataFrame(crops_stream_SQL_output(), columns =['Crop', 'Planting Start', 'Planting End'])
            dfweather = pd.DataFrame(get_noaa_weather())
            curr_forecast_df = get_noaa_weather()
            forecast_text = str(curr_forecast_df.iloc[0, 2])
            dfepsom = pd.DataFrame(epsom_salt_result(), columns =['Last Applied'])
            dfneem = pd.DataFrame(neem_oil_result(), columns =['Last Applied'])
            dffert = pd.DataFrame(fertilizer_result(), columns =['Last Applied'])
            return render_template('home.html', title = 'Home', forecast = forecast_text, picture = forecast_image(), 
                           column_crop=dfcrop.columns.values, row_crop=list(dfcrop.values.tolist()), 
                           column_weather=dfweather.columns.values, row_weather=list(dfweather.values.tolist()), 
                           column_epsom=dfepsom.columns.values, row_epsom=list(dfepsom.values.tolist()),
                           column_neem=dfneem.columns.values, row_neem=list(dfneem.values.tolist()),
                           column_fert=dffert.columns.values, row_fert=list(dffert.values.tolist()),
                           zip=zip)
    elif request.method == 'GET':
        dfcrop = pd.DataFrame(crops_stream_SQL_output(), columns =['Crop', 'Planting Start', 'Planting End'])
        dfweather = pd.DataFrame(get_noaa_weather())
        curr_forecast_df = get_noaa_weather()
        forecast_text = str(curr_forecast_df.iloc[0, 2])
        dfepsom = pd.DataFrame(epsom_salt_result(), columns =['Last Applied'])
        dfneem = pd.DataFrame(neem_oil_result(), columns =['Last Applied'])
        dffert = pd.DataFrame(fertilizer_result(), columns =['Last Applied'])
        return render_template('home.html', title = 'Home', forecast = forecast_text, picture = forecast_image(), 
                           column_crop=dfcrop.columns.values, row_crop=list(dfcrop.values.tolist()), 
                           column_weather=dfweather.columns.values, row_weather=list(dfweather.values.tolist()), 
                           column_epsom=dfepsom.columns.values, row_epsom=list(dfepsom.values.tolist()),
                           column_neem=dfneem.columns.values, row_neem=list(dfneem.values.tolist()),
                           column_fert=dffert.columns.values, row_fert=list(dffert.values.tolist()),
                           zip=zip)
    dfcrop = pd.DataFrame(crops_stream_SQL_output(), columns =['Crop', 'Planting Start', 'Planting End'])
    dfweather = pd.DataFrame(get_noaa_weather())
    curr_forecast_df = get_noaa_weather()
    forecast_text = str(curr_forecast_df.iloc[0, 2])
    dfepsom = pd.DataFrame(epsom_salt_result(), columns =['Last Applied'])
    dfneem = pd.DataFrame(neem_oil_result(), columns =['Last Applied'])
    dffert = pd.DataFrame(fertilizer_result(), columns =['Last Applied'])
    return render_template('home.html', title = 'Home', forecast = forecast_text, picture = forecast_image(), 
                           column_crop=dfcrop.columns.values, row_crop=list(dfcrop.values.tolist()), 
                           column_weather=dfweather.columns.values, row_weather=list(dfweather.values.tolist()), 
                           column_epsom=dfepsom.columns.values, row_epsom=list(dfepsom.values.tolist()),
                           column_neem=dfneem.columns.values, row_neem=list(dfneem.values.tolist()),
                           column_fert=dffert.columns.values, row_fert=list(dffert.values.tolist()),
                           zip=zip)

@app.route("/news", methods=['GET'])
def news():
    dfnews = pd.DataFrame(news_feed())
    return render_template('news.html', title = 'News', 
                           column_news=dfnews.columns.values, row_news=list(dfnews.values.tolist()), zip=zip)

@app.route("/foodnews", methods=['GET'])
def foodnews():
    dffoodnews = pd.DataFrame(food_news_feed())
    return render_template('foodnews.html', title = 'Food News', 
                           column_news=dffoodnews.columns.values, row_news=list(dffoodnews.values.tolist()), zip=zip)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
