from django.shortcuts import render, redirect
from .models import CsvUpload
from .predict import predict
from .get_dataframe import get_dataframe
# Create your views here.


def upload_csv(request):
    if request.method == 'POST':
        try:
            file = request.FILES.get('csv_file')
            CsvUpload.objects.create(
                csv_file=file
            )
            return redirect('predict_performance')
        except Exception as e:
            print(e)
    return render(request, "upload.html")


def predict_performance(request):
    file_obj = CsvUpload.objects.all().last()
    file_path = file_obj.csv_file.path

    context = {}

    if request.method == 'POST':

        g1 = int(request.POST.get('g1'))
        g2 = int(request.POST.get('g2'))
        failures = int(request.POST.get('failures'))
        studytime = int(request.POST.get('studytime'))
        absences = int(request.POST.get('absences'))

        g3_prediction, r2 = predict(
            file_path=file_path,
            g1=g1,
            g2=g2,
            failures=failures,
            studytime=studytime,
            absences=absences
        )

        g3_value = round(g3_prediction, 2)
        g3_percentage = round((g3_prediction / 20) * 100, 2)
        prediction_text = "PASS" if g3_prediction >= 10 else "FAIL"

        context = {
            'prediction': prediction_text,
            'g1': g1,
            'g2': g2,
            'failures': failures,
            'studytime': studytime,
            'absences': absences,
            'g3_value': g3_value,
            'g3_percentage': g3_percentage,
            'r2_score': round(r2 * 100, 2),
        }
        return render(request, "predict.html", context)

    return render(request, "predict.html")


def dashboard(request):
    file_obj = CsvUpload.objects.all().last()
    file_path = file_obj.csv_file.path
    df = get_dataframe(file_path)

    # Prepare chart data
    gender_counts = df['sex'].value_counts().to_dict()
    failures_counts = df['failures'].value_counts().sort_index().to_dict()
    avg_grades = df[['G1', 'G2', 'G3']].mean().to_dict()
    studytime_vs_g3 = df.groupby('studytime')['G3'].mean().to_dict()

    context = {
        'gender_labels': list(gender_counts.keys()),
        'gender_values': list(gender_counts.values()),

        'failures_labels': list(failures_counts.keys()),
        'failures_values': list(failures_counts.values()),

        'avg_grades_labels': list(avg_grades.keys()),
        'avg_grades_values': list(avg_grades.values()),

        'studytime_labels': list(studytime_vs_g3.keys()),
        'studytime_values': list(studytime_vs_g3.values()),
    }

    address_counts = df['address'].value_counts().to_dict()
    higher_counts = df['higher'].value_counts().to_dict()
    alc_dalc = df['Dalc'].value_counts().sort_index().to_dict()
    alc_walc = df['Walc'].value_counts().sort_index().to_dict()
    medu = df['Medu'].value_counts().sort_index().to_dict()
    fedu = df['Fedu'].value_counts().sort_index().to_dict()

    context.update({
        'address_labels': list(address_counts.keys()),
        'address_values': list(address_counts.values()),

        'higher_labels': list(higher_counts.keys()),
        'higher_values': list(higher_counts.values()),

        'alc_labels': list(alc_dalc.keys()),
        'dalc_values': list(alc_dalc.values()),
        'walc_values': list(alc_walc.values()),

        'parentedu_labels': list(medu.keys()),  # assuming both have same levels
        'medu_values': list(medu.values()),
        'fedu_values': list(fedu.values()),
    })

    return render(request, 'dashboard.html', context)
