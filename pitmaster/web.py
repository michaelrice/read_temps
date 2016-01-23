#   Copyright 2016 Michael Rice <michael@michaelrice.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import Flask, render_template, make_response, request, abort
from pitmaster.tools import data

app = Flask(__name__, static_folder='static', static_url_path='',
            template_folder='templates')
app.secret_key = "some key"

db = data.DBObject(filename="/home/pi/pitmaster_flex.sq3")


@app.route("/")
def show_start():
    """
    Display the start page of the app.

    :return:
    """
    return render_template("display_temps_gchart.j2", cook_data=db.list_all_by_cook("Test1"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
