# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import requests

module = GetParams("module")

if module == "getDir":

    try:

        api_key = GetParams("api_key")
        ciudad_ = GetParams("ciudad_")
        dir_ = GetParams("dir_")
        var_ = GetParams("var_")

        # params
        country = "CL"

        if not dir_:
            raise Exception('Debe ingresar una dirección')
        else:

            URL_ = "https://api.tomtom.com/search/2/geocode/" + dir_ + ".json?countrySet=" + country + "&key=" + api_key + ""
            #URL_ = "https://api.tomtom.com/search/2/structuredGeocode.json?countryCode="+ country +"&crossStreet=" + dir_ + "&municipality=" + ciudad_ + "&key=" + api_key + ""

            print(URL_)

            data = requests.get(URL_)
            data = data.json()

            print(data)

        SetVar(var_,data)

    except Exception as e:
        raise(e)
        PrintException()
