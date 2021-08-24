@app.route('/')
@app.route('/home')
def home_page():
    # render_template
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
