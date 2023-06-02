from flask_restful import Resource, request
from base_de_datos import conexion
from models.mascotas_model import MascotaModel
from dtos.mascota_dto import MascotaRequestDto

class MascotasController(Resource):
    def post(self):
        data = request.json
        try:
            dto = MascotaRequestDto()
            dto.load(data)
            return{
                'message': 'Mascota creada exitosamente'
            }, 201
        except Exception as error:
            return {
                'message': 'Error al crear la mascota',
                'content': error.args
            }