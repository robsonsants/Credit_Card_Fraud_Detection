from pydantic import BaseModel

class predictTransactions(BaseModel):
    TransactionID: int #como substituir o _id pelo transactionID mongodb
    TransactionAmt: int
    ProductCD: int
    card1: int
    card2: int
    card3: int
    card4: int #bandeira do cartão
    card5: int
    card6: int #crédito/ débito
    addr1: float
    addr2: float
    P_emaildomain: float
    C1: float
    C2: float
    C3: float
    C4: float
    C5: float
    C6: float
    C7: float
    C8: float
    C9: float
    C10: float
    C11: float
    C12: float
    C13: float
    C14: float
    D1: float
    D2: float
    D3: float
    D4: float
    D10: float
    D11: float
    D15: float
    M1: float
    M2: float
    M3: float 
    M4: float 
    M6: float 
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    V29: float
    V30: float
    V31: float
    V32: float
    V33: float
    V34: float
    V35: float
    V36: float
    V37: float
    V38: float
    V39: float
    V40: float
    V41: float
    V42: float
    V43: float
    V44: float
    V45: float
    V46: float
    V47: float
    V48: float
    V49: float
    V50: float
    V51: float
    V52: float
    V53: float
    V54: float
    V55: float
    V56: float
    V57: float
    V58: float
    V59: float
    V60: float
    V61: float
    V62: float
    V63: float
    V64: float
    V65: float
    V66: float
    V67: float
    V68: float
    V69: float
    V70: float
    V71: float
    V72: float
    V73: float
    V74: float
    V75: float
    V76: float
    V77: float
    V78: float
    V79: float
    V80: float
    V81: float
    V82: float
    V83: float
    V84: float
    V85: float
    V86: float
    V87: float
    V88: float
    V89: float
    V90: float
    V91: float
    V92: float
    V93: float
    V94: float
    V95: float
    V96: float
    V97: float
    V98: float
    V99: float
    V100: float
    V101: float
    V102: float
    V103: float
    V104: float
    V105: float
    V106: float
    V107: float
    V108: float
    V109: float
    V110: float
    V111: float
    V112: float
    V113: float
    V114: float
    V115: float
    V116: float
    V117: float
    V118: float
    V119: float
    V120: float
    V121: float
    V122: float
    V123: float
    V124: float
    V125: float
    V126: float
    V127: float
    V128: float
    V129: float
    V130: float
    V131: float
    V132: float
    V133: float
    V134: float
    V135: float
    V136: float
    V137: float
    V279: float
    V280: float
    V281: float
    V282: float
    V283: float
    V284: float
    V285: float
    V286: float
    V287: float
    V288: float
    V289: float
    V290: float
    V291: float
    V292: float
    V293: float
    V294: float
    V295: float
    V296: float
    V297: float
    V298: float
    V299: float
    V300: float
    V301: float
    V302: float
    V303: float
    V304: float
    V305: float
    V306: float
    V307: float
    V308: float
    V309: float
    V310: float
    V311: float
    V312: float
    V313: float
    V314: float
    V315: float
    V316: float
    V317: float
    V318: float
    V319: float
    V320: float
    V321: float
    hour: int
    day: int
    dow: int
    month: int 
    year: int