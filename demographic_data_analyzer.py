import pandas as pd

def calculate_demographic_data(print_data=True):
    # Завантаження даних
    df = pd.read_csv('adult.data.csv')

    # 1. Кількість людей кожної раси
    race_count = df['race'].value_counts()

    # 2. Середній вік чоловіків
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Відсоток людей зі ступенем бакалавра
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Відсоток людей з вищою освітою, які заробляють >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Відсоток людей без вищої освіти, які заробляють >50K
    lower_education = ~higher_education
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Мінімальна кількість годин на тиждень
    min_work_hours = df['hours-per-week'].min()

    # 7. Відсоток людей, які працюють мінімальну кількість годин і заробляють >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Країна з найвищим відсотком людей, які заробляють >50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    country_percentages = (country_earnings / country_counts * 100).dropna()
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # 9. Найпопулярніша професія серед людей з Індії, які заробляють >50K
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Кількість людей кожної раси:\n", race_count)
        print("Середній вік чоловіків:", average_age_men)
        print("Відсоток людей зі ступенем бакалавра:", percentage_bachelors)
        print("Відсоток людей з вищою освітою, які заробляють >50K:", higher_education_rich)
        print("Відсоток людей без вищої освіти, які заробляють >50K:", lower_education_rich)
        print("Мінімальна кількість годин на тиждень:", min_work_hours)
        print("Відсоток людей, які працюють мінімальну кількість годин і заробляють >50K:", rich_percentage)
        print("Країна з найвищим відсотком людей, які заробляють >50K:", highest_earning_country)
        print("Відсоток у цій країні:", highest_earning_country_percentage)
        print("Найпопулярніша професія серед людей з Індії, які заробляють >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Виклик функції для виведення результатів
calculate_demographic_data(print_data=True)
