from flask import Flask, request, render_template
import logging

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Set up logging to log actions to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory list to store items
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    if item:
        items.append(item)
        logging.info(f'Added item: {item}')
    return index()

@app.route('/delete', methods=['POST'])
def delete():
    item = request.form.get('item')
    if item in items:
        items.remove(item)
        logging.info(f'Deleted item: {item}')
    return index()

if __name__ == '__main__':
    app.run(debug=True)
