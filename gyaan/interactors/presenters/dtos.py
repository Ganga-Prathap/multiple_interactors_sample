"""
Created on 11/06/20

@author: revanth
"""
from dataclasses import dataclass
from typing import List


from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO


@dataclass
class DomainDetailsDTO:
    domain: DomainDTO
    domain_stats: DomainStatsDTO
    domain_experts: List[UserDetailsDTO]
    user_id: int
    is_user_following: bool
