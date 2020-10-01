import rs
print('************************************************')
rs.load_model()


context = "Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei"

question = "Ce surprinde Macro Cam la Samsung Galaxy A31?"

import tensorflow
print(tensorflow.__version__)
rs.load_model()
answer = rs.predict(context, question)
print(answer)
