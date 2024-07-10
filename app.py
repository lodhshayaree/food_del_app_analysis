from flask import Flask, render_template, url_for
import pickle
import os

app = Flask(__name__, template_folder='app/templates', static_folder='data/app/static')
#app = Flask(__name__, template_folder='app/templates')

# Ensure the graph directory exists
graph_dir = os.path.join('data','app', 'static', 'graphs')
if not os.path.exists(graph_dir):
    os.makedirs(graph_dir)

# Load model and data
model_path = os.path.join('data', 'data_pkl', 'myproj1.pkl')
with open(model_path, 'rb') as file:
    model_data = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
     # Collect all image filenames from app/static/graphs
    image_files = [f for f in os.listdir(graph_dir) if os.path.isfile(os.path.join(graph_dir, f))]
    return render_template('view.html', images=image_files, results=model_data)
   

if __name__ == '__main__':
    app.run(debug=True)
