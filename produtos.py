from flask import Flask, jsonify
import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>Vejá o valor do seu produto com /ver_produto/"Valor do produto"/"Se possui cupom de primeira"</p>'


@app.route('/ver_produto/<v1>/<c1>')
def produtos(v1,c1):
    v1 = float(v1)
    if v1 <= 100:
        desconto = 0
    elif 101 <= v1 <= 500:
        desconto = (v1 * 5) / 100
    elif v1 >= 501:
        desconto = (v1 * 10) / 100

    if c1 == 'true' or c1 == 'True' or c1 == "SIM" or c1 == 'Sim' or c1 == 'sim':
        desconto_c = 25
        c1 = True
    elif c1 == 'false' or c1 == 'False' or c1 == '' or c1 is None:
        desconto_c = 0
        c1 = False



    if c1 == True:
        valores = {
            "data_processamento": dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "valor_original": v1,
            "total_desconto": desconto + desconto_c,
            "valor_final": v1 - (desconto + desconto_c)
        }
    elif c1 == False:
        valores = {
            "data_processamento": dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "valor_original": v1,
            "total_desconto": desconto,
            "valor_final": v1 - (desconto + desconto_c)
        }
    return jsonify(valores)











if __name__ == '__main__':
    app.run(debug=True,port=5003)