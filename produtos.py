from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec

import datetime as dt

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')

spec.register(app)


@app.route('/')
def home():
    return '<p>Vejá o valor do seu produto com /ver_produto/"Valor do produto"/"Se possui cupom de primeira"</p>'

# @app.route('/ver_produto/<v1>/<c1>')
# def ver_produto(v1,c1):
#
#     v1 = float(v1)
#     if v1 <= 100:
#         desconto = 0
#     elif 101 <= v1 <= 500:
#         desconto = (v1 * 5) / 100
#     elif v1 >= 501:
#         desconto = (v1 * 10) / 100
#
#     vfinal1 = v1 - desconto
#     if c1 == 'true' or c1 == 'True' or c1 == "SIM" or c1 == 'Sim' or c1 == 'sim':
#         if vfinal1 >= 50:
#             desconto_c = 25
#         else:
#             desconto_c = 0
#     elif c1 == 'false' or c1 == 'False' or c1 == '' or c1 is None:
#         desconto_c = 0
#
#     td1 = desconto + desconto_c
#     vf1 = v1 - td1
#
#
#
#
#     valores = {
#         "data_processamento": dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#         "valor_original": v1,
#         "total_desconto": td1,
#         "desconto_percentual": desconto,
#         "desconto_cupom_primeira_compra": desconto_c,
#         "valor_final": vf1
#     }
#
#     return jsonify(valores)

@app.route('/produto',methods=['POST'])
def produto():
    '''
        API para calcular o valor do produto com desconto dependendo do seu preço

        ## Endpoint:
        GET /produto

        ## Parâmetros:

        {
            "v1": 600,
            "c1": "true"
        }
            -
        ## Resposta (json):

        {
        "data_processamento": dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "valor_original": v1,
        "total_desconto": desconto + desconto_c,
        "desconto_percentual": desconto,
        "desconto_cupom_primeira_compra": desconto_c,
        "valor_final": v1 - (desconto + desconto_c)
        }

    '''
    try:
        dados_produto = request.get_json()
        print(dados_produto)
        v1 = float(dados_produto['v1'])
        c1 = dados_produto['c1']

        if v1 <= 100:
            desconto = 0
        elif 101 <= v1 <= 500:
            desconto = (v1 * 5) / 100
        elif v1 >= 501:
            desconto = (v1 * 10) / 100

        vf1 = v1 - desconto
        if c1 == 'true' or c1 == 'True' or c1 == "SIM" or c1 == 'Sim' or c1 == 'sim':
            if vf1 <= 50:
                desconto_c = 25
            else:
                desconto_c = 0
        elif c1 == 'false' or c1 == 'False' or c1 == '' or c1 is None:
            desconto_c = 0

        dados = {
        "data_processamento": dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "valor_original": v1,
        "total_desconto": desconto + desconto_c,
        "desconto_percentual": desconto,
        "desconto_cupom_primeira_compra": desconto_c,
        "valor_final": v1 - (desconto + desconto_c)
        }

        return jsonify(dados),200

    except Exception as e:
        print(e)
        dados = {
            "status": "error",
            "msg": "Valor invalido"
        }

        return jsonify(dados),400



if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')
