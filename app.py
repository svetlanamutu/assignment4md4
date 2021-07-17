from flask import Flask, jsonify, request
import json
import ast
import pandas as pd


app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_data():
    with open('output-data/data_extract.txt', 'r') as f:
        deserialized_list = ast.literal_eval(f.read())
       # strip white spaces, if present
        deserialized_list = [tuple(str(i).strip() for i in x) for x in deserialized_list]

        week_start = request.args.get('week_start')
        week_end = request.args.get('week_end')
        if week_start is not None and week_end is not None:
            filtered_list = list()
            for i in deserialized_list:
                try:

                    week_start_date_in_data = pd.to_datetime(i[4])
                    week_start_date_in_parameter = pd.to_datetime(week_start)

                    week_end_date_in_data = pd.to_datetime(i[5])
                    week_end_date_in_parameter = pd.to_datetime(week_end)
                    if week_start_date_in_data == week_start_date_in_parameter and week_end_date_in_data == week_end_date_in_parameter:
                        filtered_list.append(i)
                except:
                    return jsonify(message="Bad data format for date value."), 401
                    raise
            if len(filtered_list) > 0:
                d = dict()
                d = build_dictionary_from_list_of_tuples(filtered_list)
                #return jsonify(results=filtered_list), 200
                return json.dumps(d), 200
            else:
                return jsonify(message="Nothing to display for week data of " + week_start + " and " + week_end+"."), 401
        else:
            return jsonify(message="Nothing to display for week data of " + str(week_start) + " and " + str(week_end) + "."), 401

def build_dictionary_from_list_of_tuples(list):
    dic = dict()

    for i in list:
        dic[i[0]] = int(i[1])
    dic['week_start'] = list[0][4]
    dic['week_end'] = list[0][5]
    return dic

@app.route('/')
def super_simple():
    return jsonify(message='Hello, type http://127.0.0.1:8080/data?week_start=08-28-2016&week_end=09-03-2016 to see some results'), 200


if __name__ == '__main__':
    app.run(debug=True)