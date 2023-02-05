from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="Specify Make")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):

    # Many to One relationship with CarMake model
    car_make = models.ForeignKey(CarMake, on_delete = models.CASCADE)

    # Informations on CarModel Table
    name = models.CharField(null=False, max_length=30, default="Specify Model")
    dealer_id = models.IntegerField(null=False)

    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    SUV = "suv"
    COUPE = "coupe"
    CONVERTIBLE = "convertible"
    WAGON = "wagon"
    SPORTS_CAR = "sports_car"
    OTHERS = "others"

    TYPE_CHOICES = [
        (HATCHBACK, "Hatchback"),
        (SEDAN, "Sedan"),
        (SUV, "Sports Utility Vehicle (SUV)"),
        (COUPE, "Coupe"),
        (CONVERTIBLE, "Convertible"),
        (WAGON, "Wagon"),
        (SPORTS_CAR, "Sports Car"),
        (OTHERS, "Others")
    ]

    car_type = models.CharField(null=False, max_length=30,\
         choices=TYPE_CHOICES, default=HATCHBACK)
    year = models.DateField()

    def __str__(self):
        return "Model Name : " + self.name + ", " \
                "Car Type : " + self.car_type 



# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:

    def __init__(self, address, city, state, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer state
        self.state = state
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date,
                car_make, car_model, car_year, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        # self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Dealer Name : " + self.name + ", " +\
                "Dealer Review : " + self.review
