from django.shortcuts import render
import pandas as pd
import plotly.express as px
import os

def home(request):
    #dataset
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'dashboard/static/dataset/Students Social Media Addiction.csv')
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    #Filters
    selected_gender = request.GET.get('gender', 'All')
    selected_platform = request.GET.get('platform', 'All')

    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_platform != 'All':
        filtered_df = filtered_df[filtered_df['Most_Used_Platform'] == selected_platform]

    #Dropdown Options
    genders = ['All'] + sorted(df['Gender'].dropna().unique().tolist())
    platforms = ['All'] + sorted(df['Most_Used_Platform'].dropna().unique().tolist())

    # Summary Stats 
    avg_usage = round(filtered_df['Avg_Daily_Usage_Hours'].mean(), 2)
    avg_sleep = round(filtered_df['Sleep_Hours_Per_Night'].mean(), 2)
    avg_mental = round(filtered_df['Mental_Health_Score'].mean(), 2)
    avg_addiction = round(filtered_df['Addicted_Score'].mean(), 2)

    # Graph 1: Average Daily Usage Hours by Platform 
    platform_usage = filtered_df.groupby('Most_Used_Platform')['Avg_Daily_Usage_Hours'].mean().reset_index()
    fig1 = px.bar(platform_usage, x='Most_Used_Platform', y='Avg_Daily_Usage_Hours', color='Most_Used_Platform',
                  title='Average Daily Usage (hrs) by Platform')

    #  Graph 2: Gender vs Addicted Score 
    fig2 = px.box(filtered_df, x='Gender', y='Addicted_Score', color='Gender',
                  title='Addicted Score Distribution by Gender')

    #  Graph 3: Sleep Hours vs Mental Health 
    fig3 = px.scatter(filtered_df, x='Sleep_Hours_Per_Night', y='Mental_Health_Score', color='Gender',
                      size='Avg_Daily_Usage_Hours', hover_name='Most_Used_Platform',
                      title='Sleep Hours vs Mental Health Score')

    #  Graph 4: Country-wise Average Addiction Score 
    country_addiction = filtered_df.groupby('Country')['Addicted_Score'].mean().reset_index()
    fig4 = px.bar(country_addiction, x='Country', y='Addicted_Score', color='Country',
                  title='Average Addiction Score by Country')

    # Dataset preview - first 10 rows of filtered data
    dataset_preview = filtered_df.head(10).to_html(classes='table table-striped', index=False, border=0)

    context = {
        'graph1': fig1.to_html(full_html=False),
        'graph2': fig2.to_html(full_html=False),
        'graph3': fig3.to_html(full_html=False),
        'graph4': fig4.to_html(full_html=False),
        'genders': genders,
        'platforms': platforms,
        'selected_gender': selected_gender,
        'selected_platform': selected_platform,
        'avg_usage': avg_usage,
        'avg_sleep': avg_sleep,
        'avg_mental': avg_mental,
        'avg_addiction': avg_addiction,
        'dataset_preview': dataset_preview,
        'total_records': len(filtered_df),
    }

    return render(request, 'dashboard/home.html', context)
