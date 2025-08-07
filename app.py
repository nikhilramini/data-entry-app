from flask import Flask, render_template, redirect, url_for
from forms import EntryForm
from models import db, Entry

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(
            name=form.name.data,
            age=form.age.data,
            title=form.title.data,
            hometown=form.hometown.data
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('confirm', entry_id=entry.id))
    return render_template('index.html', form=form)

@app.route('/confirm/<int:entry_id>')
def confirm(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    entries = Entry.query.all()
    return render_template('confirm.html', entry=entry, entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
