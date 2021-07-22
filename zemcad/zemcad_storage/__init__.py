import pickle


class ZemCadStorage:
    '''
    ZemCadStorage class stores as follows:
    - universal storage for zemcad files at given system/instance
    - track each and every file transformations over it lifecycle

    '''

    def __init__(self, storage_path, ingest_postgis: str, registered_files_base_folder: str):
        self.storage = storage_path
        self.ingest_postgis= ingest_postgis
        self.registered_files_base_folder = registered_files_base_folder

    def _init_storage(self):
        pass

    def _load_storage_into_memory(self):
        pass

    def _save_to_storage(self):
        pass
