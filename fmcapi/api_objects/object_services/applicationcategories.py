from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class ApplicationCategories(APIClassTemplate):
    """
    The ApplicationCategories Object in the FMC.
    """

    VALID_JSON_DATA = ['id', 'name', 'type']
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = '/object/applicationcategories'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationCategories class.")
        self.parse_kwargs(**kwargs)

    def post(self):
        logging.info('POST method for API for ApplicationCategories not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationCategories not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationCategories not supported.')
        pass


class ApplicationCategory(ApplicationCategories):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: ApplicationCategory() should be called via ApplicationCategories().")
        super().__init__(fmc, **kwargs)