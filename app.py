from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory list to hold schedule entries temporarily
schedule = []

@app.route('/')
def home():
    return render_template('index.html', schedule=schedule)

@app.route('/add', methods=['POST'])
def add_class():
    subject = request.form['subject']
    teacher = request.form['teacher']
    date = request.form['date']
    time = request.form['time']

    schedule.append({
        'subject': subject,
        'teacher': teacher,
        'date': date,
        'time': time
    })

    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_class(index):
    if 0 <= index < len(schedule):
        del schedule[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)