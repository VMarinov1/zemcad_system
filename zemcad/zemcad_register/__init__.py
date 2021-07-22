


class ZemCad:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_metadata(self):
        pass

    def _check_srs(self):
        pass

    def _check_extent(self):
        pass

    def _check_spatial_consistency(self):
        pass

    def _check_ekatte(self):
        pass

    def _check_duplication(self):
        pass


class RegisterZemCadFile:

    def __init__(self, srs_file):
        self.srs_file = srs_file

    def load_zemcad_file_header(self):
        pass

    def check_file_has_been_registered(self):
        pass

    def register_zemcad_file(self):
        pass

