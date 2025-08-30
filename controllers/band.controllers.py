from flask import blueprint

band_bp =blueprint("band_bp",__name__)
 print("hola")

@band_bp.route("/bands", methods=['GET'])
 print("hola")

@band_bp.route("/bands/<int:band_id>", methods=['GET'])
 print("hola")

@band_bp.route("/bands", methods=['POST'])
 print("hola")

@band_bp.route("/bands/<int:band_id>", methods=['GET'])
 print("hola")

@band_bp.route("/bands/<int:band_id>", methods=['DELETE'])
 print("hola")