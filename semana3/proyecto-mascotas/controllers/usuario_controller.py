from flask_restful import Resource, request
from base_de_datos import conexion
from models.usuarios_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto


class UsuariosController(Resource):
    # cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre que un metodo HTTP GET, POST, PUT, DELETE entonces ingresaran a esos metodos

    def get(self):
        # Lista
        resultado = conexion.session.query(UsuarioModel).all()
        dto = UsuarioResponseDto(many=True)
        # dump > convierte la instancia de la clase en un diccionario
        data = dto.dump(resultado)
        # data = []
        # for usuario in resultado:
        #       data.append({
        #       'id': usuario.id,
        #       'nombre': usuario.nombre,
        #       'apellido': usuario.apellido,
        #       'correo': usuario.correo,
        #       'dni': usuario.dni
        # })
        return{
            'content': data
        }
    
    def post(self):
        data = request.json
        dto = UsuarioRequestDto()
        # load > valida el diccionario que le pasamos con los campos que cumplan las condiciones (requeridos, que sean del tipo de dato correcto)
        dataValidada = dto.load(data)
        print(dataValidada)
        # inicializo mi nuevo usuario
        nuevoUsuario = UsuarioModel (**dataValidada)
        # nombre='Steve', apellido='Morales', correo='stevemorales@gmail.com', dni='71140403')
        # indicar que vamos a agregar un nuevo registro
        conexion.session.add(nuevoUsuario)   
        try:
            # se usa para transaccion sirve para indicar que todos los cambios se guarden de manera permanente, sino hacemos el commit entonces no se guardara la informacion de manera permanente
            conexion.session.commit()
            return {
                'message' : 'me hicieron post!'
            }, 201 # Created (Creado exitosamente)
        except Exception as error:
            conexion.session.rollback()
            return {
            'message': 'Error al crear el usuario',
            'content': error.args # args > argumentos( por que falló )
        },400
