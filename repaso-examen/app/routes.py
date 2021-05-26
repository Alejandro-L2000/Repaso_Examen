from app import app
from flask import render_template
from app.forms import HonorariosForm
from decimal import Decimal

def subtotal(valor):
    iva = Decimal(0.16)
    r_iva = Decimal(0.10666666)
    r_isr = Decimal(0.1)
    subtotal = valor + (valor*iva)
    neto = subtotal - (valor*r_iva) - (valor*r_isr)
    return neto

@app.route('/', methods=["GET","POST"])
# @app.route('/index')
def index():
    form = HonorariosForm()
    if form.validate_on_submit():
        honorarios = form.honorarios.data
        neto = subtotal(honorarios)
        return  render_template("resultado.html", honorarios=honorarios, neto=neto)
    return render_template("index.html", form = form)