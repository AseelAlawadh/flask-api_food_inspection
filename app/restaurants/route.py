from flask import jsonify, Blueprint
import joblib
import pandas as pd

api = Blueprint("restaurants", __name__, url_prefix='/restaurants')

dba_names = pd.read_csv('/Users/aseel/Developer/GA/Capstone/flask-api/app/restaurants/dba_names.csv')
model = joblib.load('/Users/aseel/Developer/GA/Capstone/flask-api/app/restaurants/xgboost_trained_model.joblib')


@api.route('/predict/<name>', methods=['GET'])
def predict_resposne():
    name = dba_names.iloc[1, :]
    # name.drop('')
    result = model.predict_proba(name)
    result1 = {
        "message": result[0]
    }
    return jsonify(result)


def predict(name):
    test_case = pd.read_csv('/Users/aseel/Developer/GA/Capstone/flask-api/app/restaurants/dummy.csv')
    # test_case = test_case.columns
    # ['dew_point_avg', 'temperature_avg', 'census_tractsmonth', 'community_areas', 'no_of_violations', 'month', 'test_case.inspection_id', 'dba_name']

    # test_case.month = 5
    # test_case.inspection_id = 2600000
    # test_case.temperature_avg = 67
    # test_case.dew_point_avg = 59

    # test_case.loc[:, [name in x for x in test_case.columns]] = 1
    # test_case.loc[:, [name in x for x in test_case.columns]] = 1
    test_case.loc[:, [name in x for x in test_case.columns]] = 1

    # test_case = pd.DataFrame([{"inspection_id": "2286009"}])
    # test_case = test_case.columns
    # test_case.loc[:, ['Subway' in x for x in test_case.columns]] = 1
    # model.verbose = False

    probs = model.predict_proba(test_case)
    prob_results = {
        'Pass': probs[0],
        'Pass w/condition': probs[1],
        'Fail': probs[2]
    }
    return prob_results
