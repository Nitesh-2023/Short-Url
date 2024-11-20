from flask import Flask,request,render_template
import pyshorteners


app=Flask(__name__)
shortener = pyshorteners.Shortener()

@app.get('/')
def show():
    return render_template('index.html')

@app.post('/url')
def url():
    url=request.form['url']
    try:
        short_url = shortener.tinyurl.short(url)
    except Exception as e:
        print("not working")
    return render_template('index.html',link=short_url)

app.run(debug=True)