from flask import Flask, render_template, request, redirect
from datetime import date

app = Flask(__name__)

# In-memory list to hold schedule entries temporarily
schedule = []

@app.route('/')
def home():
    min_date = date.today().isoformat()
    return render_template('index.html', schedule=schedule,min_date=min_date)
    


@app.route('/add', methods=['POST'])
def add_class():
    subject = request.form.get('subject','').strip()
    teacher = request.form.get('teacher','').strip()
    date = request.form.get('date','').strip()
    time = request.form.get('time','').strip()

    if not subject or not teacher or not date or not time:
     return "All fields are required",400 #bad request

    for cls in schedule:
     if cls['subject'] == subject and cls['date'] == date and cls['time'] == time:
      return "This class is already scheduled at that time!", 400

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