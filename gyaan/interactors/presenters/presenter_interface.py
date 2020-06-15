from abc import ABC
from abc import abstractmethod

from gyaan.interactors.presenters.dtos import DomainDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_domain_does_not_exist_exception(self):
        pass

    @abstractmethod
    def get_domain_details_response(
            self, domain_details_dto: DomainDetailsDTO) -> dict:
        pass
