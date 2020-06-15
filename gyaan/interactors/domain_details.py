"""
Created on 11/06/20

@author: revanth
"""
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface

from gyaan.interactors.presenters.dtos import DomainDetailsDTO


class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, domain_id: int, user_id: int,
                                   presenter: PresenterInterface) -> dict:
        from gyaan.exceptions.exceptions import DomainDoesNotExist
        try:
            domain_details_dto = self.get_domain_details(domain_id, user_id)
            response = presenter.get_domain_details_response(
                domain_details_dto)
            return response
        except DomainDoesNotExist:
            presenter.raise_domain_does_not_exist_exception()

    def get_domain_details(self, domain_id: int, user_id: int) -> \
            DomainDetailsDTO:

        domain_dto = self.storage.get_domain(domain_id)
        domain_stats = self.storage.get_domain_stats(domain_id)
        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts = self.storage.get_users_details(domain_expert_ids)
        is_user_following = self.storage.is_user_following_domain(
            domain_id, user_id)

        response = DomainDetailsDTO(
            domain_dto, domain_stats, domain_experts, user_id,
            is_user_following)
        return response
