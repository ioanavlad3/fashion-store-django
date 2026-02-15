<h1>Online Clothing Store - Django Web Application</h1>
<h2>Overview</h2>

This project is a full-featured online clothing store built with Django.
It allows users to browse products, filter items by category, create accounts, log in, and complete purchases.

Additionally, users receive personalized promotional emails with special offers and discounts.

The project follows standard Django architecture and includes authentication, product management, and email integration.

<h2>Features</h2>
<ul>
<li>User registration and authentication (Login / Logout)</li>
<li>Product listing with category filtering</li>
<li>Search and filtering functionality</li>
<li>Add to cart & purchase functionality</li>
<li>Personalized promotional emails</li>
<li>Admin panel for product management</li>
<li>Order handling system</li>
</ul>

<h2>Main Models</h2>
<ol>
  <li>Product</li>
    <ul>
      <li>Id, Name, Price</li>
      <li>Relationship with Category, Brand, Material</li>
    </ul>
  <li>Variant_Product</li>
    <ul>
      <li>Id, Color, Size</li>
      <li>Relationship with Product</li>
    </ul>
  <li>Category</li>
    <ul>
      <li>Id, Name</li>
      <li>Relationship with Product</li>
    </ul>
  <li>User</li>
    <ul>
      <li>Id, Username, email</li>
      <li>Roles: Admin, User</li>
    </ul>
  <li>Cart</li>
    <ul>
      <li>Handles each user's shopping cart</li>
    </ul>
</ol>

<h2>Technologies Used</h2>
<ul>
<li>Python</li>
<li>Django</li>
<li>HTML</li>
<li>CSS</li>
<li>PostreSQL Database</li>
<li>Django Email Backend</li>

</ul>

<h2>Project Structure</h2>

```text
manage.py
magazin/              # main Django project (settings, urls, wsgi)
magazin_haine/        # App (models, views, templates)
