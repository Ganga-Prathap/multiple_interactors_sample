from dataclasses import dataclass


@dataclass
class DomainDTO:
    domain_id: int
    name: str
    description: str


@dataclass
class DomainStatsDTO:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int


@dataclass
class UserDetailsDTO:
    user_id: int
    name: str
    profile_pic_url: str
