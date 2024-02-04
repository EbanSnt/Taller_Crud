from django.shortcuts import render,redirect
from main.models import Customers,Tickets,WarrantyProducts,DeliveredProducts


def index(request):
    """Vista principal"""
    try:
        return render(request, "index.html")
    except Exception:
        return render(request, "index.html")

### TODOS LOS "CREATE" ###
def create_customer(request):
    """Crea un nuevo cliente"""
    if request.method == "POST":
        name = request.POST["name"]
        telephone_number = request.POST["telephone_number"]
        Customers.objects.create(name=name,telephone_number=telephone_number)
        return redirect("all_customers")
    else:
        return render(request, "new_customer.html")


def create_ticket(request):
    customers = Customers.objects.all()
    if request.method == "POST":
        ticket_number = request.POST["ticket_number"]
        customer_id = request.POST["customer_id"]
        customer = Customers.objects.get(id=customer_id)
        product = request.POST["product"]
        trademark = request.POST["trademark"]
        version = request.POST["version"]
        serial_number = request.POST["serial_number"]
        failure = request.POST["failure"]
        product_image1 = request.FILES.get("product_image1")
        product_image2 = request.FILES.get("product_image2")
        product_image3 = request.FILES.get("product_image3")
        description = request.POST["description"]
        Tickets.objects.create(ticket_number=ticket_number,customer_id=customer,product=product,trademark=trademark,version=version,serial_number=serial_number,failure=failure,product_image1=product_image1,product_image2=product_image2,product_image3=product_image3,description=description)
        return redirect("all_tickets")
    else:
        context = {"customers":customers}
        return render(request, "new_ticket.html",context)


def create_warranty_product(request):
    if request.method == "POST":
        customer_id = request.POST["customer_id"]
        customer = Customers.objects.get(id=customer_id)
        ticket_id = request.POST["ticket_id"]
        ticket = Tickets.objects.get(id=ticket_id)
        description = request.POST["description"]
        WarrantyProducts.objects.create(customer_id=customer,ticket_id=ticket,description=description)
        return redirect("all_warranty_products")
    else:  
        return render(request, "new_warranty_product.html")


def create_delivered_product(request):
    if request.method == "POST":
        ticket_id = request.POST["ticket_id"]
        ticket = Tickets.objects.get(id=ticket_id)
        DeliveredProducts.objects.create(ticket_id=ticket)
        return redirect("all_delivered_products")
    else:
        return render(request, "new_delivered_product.html")
    
### TODOS LOS "READ" ###

def show_all_customers(request):
    try:
        customers = Customers.objects.all()
        context = {"customers":customers}
        return render(request, "customers.html",context)
    except:
        return render(request, "customers.html")


def show_all_tickets(request):
    try:
        tickets = Tickets.objects.all()
        context = {"tickets":tickets}
        return render(request, "tickets.html",context)
    except:
        return render(request, "tickets.html")


def show_all_warranty_products(request):
    try:
        warranty_products = WarrantyProducts.objects.all()
        context = {"warranty_products":warranty_products}
        return render(request, "warranty_products.html",context)
    except:
        return render(request, "warranty_products.html")


def show_all_delivered_products(request):
    try:
        delivered_products = DeliveredProducts.objects.all()
        context = {"delivered_products":delivered_products}
        return render(request, "delivered_products.html",context)
    except:
        return render(request, "delivered_products.html")


### TODOS LOS "UPDATE" ###
    
def update_customer(request,customer_id):
    customer = Customers.objects.get(id=customer_id)
    tickets = Tickets.objects.filter(customer_id=customer_id)
    context = {"customer":customer, "tickets":tickets}
    #warranties = WarrantyProducts.objects.filter(ticket_id=customer_id)
    try:
        if request.method == "POST":
            customer.name = request.POST["name"]
            customer.telephone_number = request.POST["telephone_number"]
            customer.save()
            return redirect("update_customer")
    except:
        return render(request, "update_customer.html",context)