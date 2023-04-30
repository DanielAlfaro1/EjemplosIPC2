from flask import Blueprint, jsonify, request, Response
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


@ejemplo.route("/ObtenerPublicaciones", methods=["GET"])
def ObtenerPubs():
    Contenido = ObtenerLista()
    return Response(Contenido, mimetype='text/xml')

@ejemplo.route("/ObtenerPublicacion", methods=["POST"])
def GetPub():
    Contenido = ObtenerPub(request.data)
    return Response(Contenido, mimetype='text/xml')

@ejemplo.route("/EditarPublicacion", methods=["POST"])
def EditPub():
    Contenido = EditarPublicacion(request.data)
    return Response(Contenido, mimetype='text/xml')

@ejemplo.route("/CrearPublicacion", methods=["POST"])
def CreatePub():
    Contenido = CrearPublicacion(request.data)
    return Response(Contenido, mimetype='text/xml')

@ejemplo.route("/AnalizarPublicacion", methods=["POST"])
def AnalizarPub():
    Contenido = Analizar(request.data)
    return Response(Contenido, mimetype='text/xml')