from flask import Blueprint, jsonify, request
from controllers.controller import *

ejemplo = Blueprint("ejemplo", __name__)

@ejemplo.route("/SaludoNormal", methods=["GET"])
def UnSaludoNormal():
    variable = EjecutarUnHola()
    print(variable)
    return jsonify(variable)
    
@ejemplo.route("/SaludoPersonal", methods=["POST"])
def UnSaludoPersonal():
    print(request.data)
    LoPersonalizado = request.data
    variable = EjecutarUnHola(LoPersonalizado)
    return variable
