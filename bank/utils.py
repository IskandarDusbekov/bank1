import re


def card_mask(card_number):
    yashirn = card_number[:4] + " **** **** " + card_number[-4:]
    return yashirn

def phone_mask(phone):
    raqamni_yashirish ="+998"+" "+phone[:2]+" *** ** "+ phone[-2:]
    return raqamni_yashirish

def format_card(raw_card):
    son =re.sub(r"\D", "", str(raw_card))
    return " ".join([son[i:i + 4] for i in range(0, len(son), 4)])

def format_phone(raw_phone):

    if not raw_phone:
        return "None"

    raqam =re.sub(r"\D", "", str(raw_phone))

    if not raqam.startswith("998"):
        raqam = "+998"+raqam

    return f"+{raqam[:3]} {raqam[3:5]} {raqam[5:8]} {raqam[8:10]} {raqam[10:12]}"



# def prepare_message(card_number, balance, lang="UZ"): ...
# def send_message(message, chat_id=12345): ...
