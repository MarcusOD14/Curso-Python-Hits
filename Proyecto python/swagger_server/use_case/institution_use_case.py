from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData


class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_intitution(self):
        """
        Lista de instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_intitution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response
    
    def get_id_intitution(self, institution_id):
        
        data_response = []
        institutions = self.institution_repository.get_id_intitution(institution_id)

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                    created_user=i.created_user,
                    created_at=i.created_at,
                    updated_user=i.updated_user,
                    updated_at=i.updated_at,
                    status=i.status

                )

            )

        if not data_response:
            return {'mensaje': "Id no registrado"}
        response = ResponseInstitution(
            code=0,
            message="Proceso exitoso",
            data=data_response
        )

        return response
