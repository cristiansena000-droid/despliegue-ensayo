def totalizar_carro(request):
    total=0
    if request.user.is_authenticated:
        if "carro" in request.session:
            for key,value in request.session["carro"].items():
                total+=float(value["precio"])*value["cantidad"]
    return {"totalizar_carro":total}