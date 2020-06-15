from abc import ABC
from abc import abstractmethod
from typing import List

from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO


class StorageInterface(ABC):

    @abstractmethod
    def get_domain(self, domain_id: int) -> DomainDTO:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDTO]:
        pass

    @abstractmethod
    def is_user_following_domain(self, domain_id: int, user_id: int) -> bool:
        pass
