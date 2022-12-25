from flask import Flask
from market import app , db
from market.models import Car



with app.app_context():
    
    db.drop_all()
    db.create_all()
    c1 = Car(name="Maruti Swt Dzire VDI" , selling_price="450000" , km_driven="145500" , fuel="Diesel" , year="2014" , seller_type="Individual" , transmission="Manual" , mileage="23.4", engine="1248" , max_power="74" , seats="5" , owner="First" , region="Algeria")
    db.session.add(c1)
    db.session.commit()
