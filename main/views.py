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
        #Se toman los datos del formulario
        name = request.POST["name"]
        telephone_number = request.POST["telephone_number"]
        #Se crea el nuevo cliente
        Customers.objects.create(name=name,telephone_number=telephone_number)
        return redirect("all_customers")
    else:
        return render(request, "new_customer.html")


def create_ticket(request):
    """Crea un nuevo presupuesto"""
    #Se pasa por contexto todos los cliente, para que asi
    #el usuario pueda elegir uno en la lista desplegable
    customers = Customers.objects.all()
    if request.method == "POST":
        #Se toman los datos del formulario
        ticket_number = request.POST["ticket_number"]
        customer_id = request.POST["customer_id"]
        #Aqui se toma el id del "customer", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
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
        #Se crea el nuevo presupuesto
        Tickets.objects.create(ticket_number=ticket_number,customer_id=customer,product=product,trademark=trademark,version=version,serial_number=serial_number,failure=failure,product_image1=product_image1,product_image2=product_image2,product_image3=product_image3,description=description)
        return redirect("all_tickets")
    else:
        context = {"customers":customers}
        return render(request, "new_ticket.html",context)


def create_warranty_product(request):
    """Crea un nuevo producto en Garantia"""
    #Se pasa por contexto todos los tickets, para que asi
    #el usuario pueda elegir uno en la lista desplegable
    tickets = Tickets.objects.all()
    context = {"tickets":tickets}
    if request.method == "POST":
        # Toma los datos del formulario
        ticket_id = request.POST["ticket_id"]
        #Aqui se toma el id del "ticket", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
        ticket = Tickets.objects.get(id=ticket_id)
        description = request.POST["description"]
        WarrantyProducts.objects.create(ticket_id=ticket,description=description)
        return redirect("all_warranty_products")
    else:  
        return render(request, "new_warranty_product.html",context)


def create_delivered_product(request):
    """Crea un nuevo producto entregado"""
    #Se pasa por contexto todos los tickets, para que asi
    #el usuario pueda elegir uno en la lista desplegable
    tickets = Tickets.objects.all()
    context = {"tickets":tickets}
    if request.method == "POST":
        #Se toman los datos del formulario
        ticket_id = request.POST["ticket_id"]
        #Aqui se toma el id del "ticket", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
        ticket = Tickets.objects.get(id=ticket_id)
        DeliveredProducts.objects.create(ticket_id=ticket)
        return redirect("all_delivered_products")
    else:
        return render(request, "new_delivered_product.html",context)
    
### TODOS LOS "READ" ###

def show_all_customers(request):
    """Lista todos los clientes"""
    try:
        customers = Customers.objects.all()
        if 'customer_search' in request.GET:
            #Sirve para filtrar clientes, de acuerdo a su nombre (busca coincidencias)
            customer_search = request.GET["customer_search"]
            customers = customers.filter(name__icontains=customer_search)
        context = {"customers": customers}
        return render(request, "customers.html", context)
    except Exception:
        context = {"customers": customers}
        return render(request, "customers.html", context)


def show_all_tickets(request):
    """Lista todos los tickets"""
    try:
        tickets = Tickets.objects.all()
        if 'ticket_search' in request.GET:
            #Sirve para filtrar tickets, de acuerdo a su numero (busca coincidencias)
            ticket_search = request.GET["ticket_search"]
            tickets = tickets.filter(ticket_number__icontains=ticket_search)
        context = {"tickets":tickets}
        return render(request, "tickets.html",context)
    except:
        context = {"tickets":tickets}
        return render(request, "tickets.html",context)


def show_all_warranty_products(request):
    """Lista todos los productos en Garantia"""
    try:
        warranty_products = WarrantyProducts.objects.all()
        if 'warranty_search' in request.GET:
            #Sirve para filtrar productos en garantia, de acuerdo a su numero de ticket (busca coincidencias)
            warranty_search = request.GET["warranty_search"]
            warranty_products = warranty_products.filter(ticket_id__ticket_number__icontains=warranty_search)
        context = {"warranty_products":warranty_products}
        return render(request, "warranty_products.html",context)
    except:
        context = {"warranty_products":warranty_products}
        return render(request, "warranty_products.html")


def show_all_delivered_products(request):
    """Lista todos los productos entregados"""
    try:
        delivered_products = DeliveredProducts.objects.all()
        context = {"delivered_products":delivered_products}
        return render(request, "delivered_products.html",context)
    except:
        return render(request, "delivered_products.html")


### TODOS LOS "UPDATE" ###
    # En estas vista se pueden ver mas detalles, como asi tambien, la
    # posibilidad de modificar datos

def update_customer(request,customer_id):
    """Actualiza un cliente"""
    #Se pasa por parametro el id
    try:
        customer = Customers.objects.get(id=customer_id)
        # Aqui puede observar en que tickets hace referencia el cliente seleccionado 
        tickets = Tickets.objects.filter(customer_id=customer_id)
        context = {"customer":customer, "tickets":tickets}
        if request.method == "POST":
            customer.name = request.POST["name"]
            customer.telephone_number = request.POST["telephone_number"]
            customer.save()
            return redirect("all_customers")
        else:
            return render(request, "update_customer.html",context)
    except:
        return render(request, "update_customer.html",context)


def update_ticket(request,ticket_id):
    """Actualiza un ticket"""
    #Se pasa por parametro el id
    try:
        ticket = Tickets.objects.get(id=ticket_id)
        # Lista de Clientes. En caso de que quiera modificar el existente
        customers = Customers.objects.all()
        context = {"customers":customers, "ticket":ticket}
        if request.method == "POST":
            print(request.POST)
            ticket.ticket_number = request.POST["ticket_number"]
            
            #Aqui se toma el id del "customer", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
            new_customer_id = int(request.POST["customer_id"])
            new_customer = Customers.objects.get(id=new_customer_id)
            ticket.customer_id = new_customer

            ticket.product = request.POST["product"]
            ticket.trademark = request.POST["trademark"]
            ticket.version = request.POST["version"]
            ticket.serial_number = request.POST["serial_number"]
            ticket.failure = request.POST["failure"]
            ticket.description = request.POST["description"]

            if request.POST.get("local") == "1":
                ticket.local = int(request.POST.get("local", 0))
            else:
                ticket.local = int(request.POST.get("local", 1))
            ticket.save()
            return redirect("all_tickets")
        else:
            return render(request, "update_ticket.html",context)
    except:
        return render(request, "update_ticket.html",context)



def update_warranty_product(request,warranty_id):
    """Actualiza un producto en garantia"""
    #Se pasa por parametro el id
    try:
        warranty_product = WarrantyProducts.objects.get(id=warranty_id)
        # Lista de Tickets. En caso de que quiera modificar el existente
        tickets = Tickets.objects.all()
        context = {"warranty_product":warranty_product,"tickets":tickets}
        if request.method == "POST":
            #Aqui se toma el id del "ticket", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
            new_ticket_id = int(request.POST["ticket_id"])
            new_ticket = Tickets.objects.get(id=new_ticket_id)
            warranty_product.ticket_id = new_ticket

            warranty_product.description = request.POST["description"]

            if request.POST.get("local") == "1":
                warranty_product.local = int(request.POST.get("local", 0))
            else:
                warranty_product.local = int(request.POST.get("local", 1))
            warranty_product.save()
            return redirect("all_warranty_products")
        else:
            return render(request, "update_warranty_product.html",context)
    except:
        return render(request, "update_warranty_product.html",context)

def update_delivered_product(request,delivered_id):
    """Actualiza un producto entregado"""
    #Se pasa por parametro el id
    try:
        delivered_product = DeliveredProducts.objects.get(id=delivered_id)
        # Lista de Tickets. En caso de que quiera modificar el existente
        tickets = Tickets.objects.all()
        context = {"delivered_product":delivered_product,"tickets":tickets}
        if request.method == "POST":
            #Aqui se toma el id del "ticket", para luego pasarle por parametro un objeto y no un numero. Ya que es una llave Foranea
            new_ticket_id = int(request.POST["ticket_id"])
            new_ticket = Tickets.objects.get(id=new_ticket_id)
            delivered_product.ticket_id = new_ticket

            delivered_product.save()
            return redirect("all_delivered_products")
        else:
            return render(request, "update_delivered_product.html",context)
    except:
        return render(request, "update_delivered_product.html",context)

### TODOS LOS "DELETE" ###
    
def delete_customer(request,customer_id):
    """Borra un cliente"""
    #Se pasa por parametro el id
    customers = Customers.objects.all()
    context = {"customers":customers}
    try:
        customer = Customers.objects.get(id=customer_id)
        customer.delete()
        return redirect("customers")
    except:
        return render(request,"customers.html",context)


def delete_ticket(request,ticket_id):
    """Borra un Ticket"""
    #Se pasa por parametro el id
    tickets = Tickets.objects.all()
    context = {"tickets":tickets}
    try:
        ticket = Tickets.objects.get(id=ticket_id)
        ticket.delete()
        return redirect("tickets")
    except:
        return render(request,"tickets.html",context)


def delete_warranty_product(request,warranty_id):
    """Borra un producto en Garantia"""
    #Se pasa por parametro el id
    warranty_products = WarrantyProducts.objects.all()
    context = {"warranty_products":warranty_products}
    try:
        warranty_product = WarrantyProducts.objects.get(id=warranty_id)
        warranty_product.delete()
        return redirect("warranty_products")
    except:
        return render(request,"warranty_products.html",context)
    

def delete_delivered_product(request,delivered_id):
    """Borra un producto entregado"""
    #Se pasa por parametro el id
    delivered_products = DeliveredProducts.objects.all()
    context = {"delivered_products":delivered_products}
    try:
        delivered_product = DeliveredProducts.objects.get(id=delivered_id)
        delivered_product.delete()
        return redirect("delivered_products")
    except:
        return render(request,"delivered_products.html",context)
