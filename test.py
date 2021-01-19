from db.models import Product, Category, session



tv = session.query(Category).filter(Category.name=='TV').one()
print(tv)
print(tv.products)


product = session.query(Product).filter(Product.name == 'LG').one()
print(product.name)
print(product.description)
