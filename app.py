from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

company_name = "FORTUNATE HUB"
company_photos = [

]
subt = "Your all-in-one lifestyle & hangout spot"
logo = 'https://i.postimg.cc/Wz5bNBgB/fortunatehub-ilorin-logo.jpg'
article = {
    "heading": 'Fortunate Hub in Ilorin',
    "section 1": 'A multi-purpose lifestyle and food center',
    "section 2": '5050 Foods is a part of the larger Fortunate Hub brand',
    "section 3": 'Well known in Kwara State',
    "section 4": 'Fortunate Hub has been operational for a significant period of time',
    "section 5": 'The people of Ilorin and many others have accepted us and our brand with open arms',
    "section 6": 'Fortunate Hub Taiwo Isale is one of its kind and it is one destination with many choices.'
}
about = """
Fortunate Hub Ilorin

Fortunate Hub Ilorin is more than just a place to eat — it is a vibrant lifestyle destination designed to bring comfort, flavor, and unforgettable experiences together in one space. 
As part of the well-established Fortunate (Fifty-Fifty Foods) brand, known across Kwara State for its high-quality bread and confectioneries, we proudly continue a legacy of excellence and trust.
With a strong presence built over time and multiple branches across the state and beyond, Fortunate Hub has earned the loyalty and love of the Ilorin community. 
Our Taiwo Isale location stands out as a unique, all-in-one destination where variety meets convenience.
At Fortunate Hub Ilorin, we offer a carefully curated multi-level experience:
* An immersive underground section for a distinct atmosphere.
* A welcoming ground floor for quick access and casual moments.
* A fully serviced restaurant for quality dining.
* A modern gym for fitness and wellness.
* A relaxing lounge for leisure and social connection.
This diverse setup makes Fortunate Hub a place where you can dine, relax, stay active, and unwind — all under one roof.
What truly sets us apart is our unwavering commitment to quality. From the taste of our meals to the warmth of our customer service, every detail is crafted to give you the best experience possible. 
In a competitive space, we remain different by consistently delivering excellence and creating a welcoming environment for everyone.
To make things even easier, we offer reliable delivery services. Whether you are at home or at work, you can enjoy your favorite meals from Fortunate Hub with just a simple order — delivered fresh and right on time.
Fortunate Hub Ilorin — one destination, many choices.
"""
services = {
    "Vital Fitness": 'Gym', 
    "5050 Foods": [
        'Bread', 
        'Restaurant', 
        'Pastries', 
        'deserts'
    ],
    "Cavelux": [
        'Lounge', 
        'Lifestyle'
    ]
}
address = "Ibrahim Taiwo Rd, beside Firstbank, Isale, Ilorin 240211, Kwara State."
breads_gallery = [

]
pastries_gallery = [

]
deserts_gallery = [

]
meals_gallery = [

]
gym_galllery = [

]
lounge_galllery = [

]
lifestyle_galllery = [
    
]
hours = {
    "opens": '7:30 am', 
    "closes": '11:30 pm'
}
contacts = {
    "Whatsapp": '07070646407', 
    "Facebook": 'FortunateHubIlorin', 
    "Instagram": 'fortunatehub_ilorin',
    "Tiktok": 'fortunatehub_ilorin',
    "Email": 'Fortunatebread@gmail.com'
}





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/5050-foods')
def foods():
    return render_template('5050-foods.html')

@app.route('/cavelux')
def cavelux():
    return render_template('cavelux.html')

@app.route('/vital-fitness')
def fitness():
    return render_template('vital-fitness.html')

if __name__ == "__main__":
    app.run()