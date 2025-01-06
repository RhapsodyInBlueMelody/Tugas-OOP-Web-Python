import logging
from app import app
from flask import render_template, request, redirect, url_for, flash, current_app
from app.models.product import Product
from app.services.product_service import ProductService

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kategori')
def kategori():
    return render_template("kategori.html")

@app.route('/produk')
def produk():
    try:
        # Get products using the service
        raw_products = ProductService.get_products_by_category('electronics')
        
        if not raw_products:
            flash('No products found', 'warning')
            return render_template("produk.html", products=[])

        products = [
            Product(
                id=product_data['id'],
                title=product_data['title'],
                price=product_data['price'],
                description=product_data['description'],
                category=product_data['category'],
                image=product_data['image']
            )
            for product_data in raw_products
        ]
        return render_template("produk.html", products=products)
    except Exception as e:
        logging.error(f"Error fetching products: {str(e)}")
        flash('Error fetching products', 'error')
        return render_template("produk.html", products=[])

@app.route('/produk/new', methods=['GET'])
def show_create_product_form():
    return render_template("create_product.html")

import logging
from flask import current_app  # Add this import

@app.route('/produk/new', methods=['POST'])
def create_product():
    try:
        # Extract form data
        new_product = Product(
            id=None,
            title=request.form.get('title'),
            price=float(request.form.get('price', 0)),
            description=request.form.get('description'),
            category=request.form.get('category'),
            image=request.form.get('image')
        )
        
        # Create product
        result = ProductService.create_product(new_product)
        
        # Check result
        if isinstance(result, dict):
            flash('Product created successfully!', 'success')
            return redirect(url_for('produk'))
        else:
            flash(str(result), 'danger')
            return redirect(url_for('show_create_product_form'))
    
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('show_create_product_form'))

@app.route('/contact')
def contact():
    return render_template("kontak.html")

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = ProductService.get_product(product_id)
        
        if not product:
            flash('Product not found', 'warning')
            return redirect(url_for('produk'))
        
        return render_template('detail_produk.html', product=product)
    except Exception as e:
        logging.error(f"Error fetching product {product_id}: {str(e)}")
        flash('Error fetching product details', 'error')
        return redirect(url_for('produk'))
