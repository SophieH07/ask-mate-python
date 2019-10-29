from flask import Flask, render_template, request, redirect, url_for
import connection
app = Flask(__name__)

saved_answer = {}


@app.route('/')
@app.route('/list')
def route_list():
    answer_text = None
    if 'answer' in saved_answer:
        answer_text = saved_answer['answer']
    return render_template("index.html", answer=answer_text)


@app.route('/post-answer', methods=['POST'])
def route_post():
    if request.method == 'POST':
        saved_answer['answer'] = request.form['answer']
        return redirect('/list')
    answer_text = None
    if 'answer' in saved_answer:
        answer_text = saved_answer['answer']
    return render_template('edit.html', answer=answer_text)

@app.route('/add-question')
def route_add_question():
    return render_template('add.html')




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7000,
        debug=True,
    )