from flask import Flask, render_template, url_for

app = Flask(__name__)

# Data 5 Produk Rebreather RDI
products = [
    {
        'id': 1,
        'name': 'RDI Basic Backmount',
        'category': 'Backmount',
        'image': 'basic-backmount.jpg',
        'o2_range': '0.21 - 1.40 bar',
        'depth_rating': '40m',
        'duration': '3-4 hrs',
        'co2_scrubber': '3-4 hrs',
        'weight': '12 kg',
        'description': 'Entry-level closed-circuit rebreather untuk recreational diving. Mudah digunakan dan reliable untuk pemula.',
        'price': 'Rp 85.000.000',
        'features': ['Single loop', 'Manual diluent', 'Basic HUD', 'Backpack harness']
    },
    {
        'id': 2,
        'name': 'RDI Deluxe',
        'category': 'Backmount',
        'image': 'deluxe.jpg',
        'o2_range': '0.21 - 1.60 bar',
        'depth_rating': '60m',
        'duration': '5-6 hrs',
        'co2_scrubber': '5-6 hrs',
        'weight': '14 kg',
        'description': 'Mid-range rebreather dengan fitur lengkap untuk technical diving. Dilengkapi dengan advanced monitoring system.',
        'price': 'Rp 125.000.000',
        'features': ['Dual loop', 'Auto diluent', 'Advanced HUD', 'O2 sensors x3', 'Deco algorithm']
    },
    {
        'id': 3,
        'name': 'RDI Deepdive Pro',
        'category': 'Deepdive',
        'image': 'deepdive-pro.jpg',
        'o2_range': '0.21 - 2.00 bar',
        'depth_rating': '120m',
        'duration': '8-10 hrs',
        'co2_scrubber': '8-10 hrs',
        'weight': '18 kg',
        'description': 'Technical rebreather untuk extreme deep diving. Dirancang untuk cave diving dan wreck penetration.',
        'price': 'Rp 185.000.000',
        'features': ['Triple redundant', 'Full auto', 'He diluent ready', 'Bailout integrated', 'Cave mode']
    },
    {
        'id': 4,
        'name': 'RDI Chest Mount Compact',
        'category': 'Chest Mount',
        'image': 'chest-mount.jpg',
        'o2_range': '0.21 - 1.40 bar',
        'depth_rating': '30m',
        'duration': '2-3 hrs',
        'co2_scrubber': '2-3 hrs',
        'weight': '8 kg',
        'description': 'Compact chest-mounted rebreather untuk shallow diving dan photography. Ultra-lightweight dan streamlined.',
        'price': 'Rp 65.000.000',
        'features': ['Chest harness', 'Minimal profile', 'Quick don', 'Photo-friendly', 'Silent operation']
    },
    {
        'id': 5,
        'name': 'RDI Advanced Explorer',
        'category': 'Backmount',
        'image': 'advanced-explorer.jpg',
        'o2_range': '0.21 - 1.80 bar',
        'depth_rating': '80m',
        'duration': '6-8 hrs',
        'co2_scrubber': '6-8 hrs',
        'weight': '16 kg',
        'description': 'Professional-grade rebreather untuk expedition diving. Kombinasi performa tinggi dan reliability.',
        'price': 'Rp 155.000.000',
        'features': ['Dual loop', 'Full auto', 'GPS tracking', 'Satellite comm', 'Expedition mode']
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product_detail.html', product=product)

@app.route('/demo')
def book_demo():
    return render_template('demo.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)