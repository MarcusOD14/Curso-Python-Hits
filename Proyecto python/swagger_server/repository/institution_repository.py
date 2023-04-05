sql_select = "select * from institution where status = 'A'"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_intitution(self):
        """
            resuelve la consulta a la base de datos
        return:
        """
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows
        
    def get_id_intitution(self, institution_id):
        sql_select_id = "select * from institution where status = 'A' and id = '{0}'". format(institution_id)
        with self.session_factory() as session:
            rows = session.execute(sql_select_id)
            return rows
