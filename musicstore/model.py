from datetime import datetime

class transaction:
    def _init_(self, type: int, copies: int):    
        SELL: int = 1
        SUPLY: int = 2
        date: datetime() # type: ignore
    
class disc:
    def _init_(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        sid: str
        title: str
        artist: str
        sale_price: float
        purchase_price: float
        quantity: int
        transactions: list[transaction]= {}
        song_list: list[str]= {}
        def add_song(self, song: str):
            def SELL(self, copies: int) -> bool:
                copies > quantity
                return False
            def SUPLY(self, copies: int):
                quantity = +1

class MusicStore:
    def _init_(self, discs: dict[str, disc] = {}):
        def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int ):
            def search_by_sid(self, sid: str = Disc/None ):
                def sell_disc(self, sid: str, copies: int) -> bool:
                    disc = self.search_by_sid(sid)
                     if disc is None:
                         return False
                            return disc.sell(copies)
                    
                            def supply_disc(self, sid: str, copies: int) -> bool:
                                 disc = self.search_by_sid(sid)
                                    if disc is None:
                                     return False
    
                                    disc.supply(copies)
                                     return True
                
                
