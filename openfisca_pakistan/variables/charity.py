from openfisca_core.indexed_enums import Enum
from openfisca_core.variables import Variable
from openfisca_core.periods import YEAR
from openfisca_pakistan.entities import Person


# TODO
# - How to allow multiple donations for one person? - How to allow donation to be
# accessed under charity; `person("charity", period).donation`? Which would hopefully
# enable the first point as well. - How to access the organisation of a donation?
class donation(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Donation amount"
    documentation = """
    Amount paid in a tax year for any charitable purpose:
        1. Relief of the poor
        2. Education
        3. Medical relief
        4. Advancement of any other object of general public utility
    """


class CharityOrganisationTypes(Enum):
    university = "University"
    board_of_education = "Board of Education"
    educational_institution = "Educational institute"
    relief_fund = "Relief fund"
    ngo = "Non-profit organisation"


class organisation(Variable):
    value_type = Enum
    possible_values = CharityOrganisationTypes
    entity = Person
    definition_period = YEAR
    default_value = CharityOrganisationTypes.ngo
    label = "Type of charity organisation"
