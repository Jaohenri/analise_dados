    
class Phone:

    def __init__(self, cep, phone):
        self.cep = cep
        self.raw_phone = phone
        self.phone = self.get_phone(cep, phone)

    def get_phone(self, cep, phone):
        from src.models.adress import Address
        phone = phone.replace(' ', '').replace('-', '')
        address = Address(cep)
        ddd = address.get_ddd()
        if not ddd:
            return 'DDD não disponível, CEP inválido' 
        
        if len(phone) == 11 or len(phone) == 12 and phone.startswith(f"{ddd}9"):
            return f'{phone[:2]} {phone[2:]}'
             
        if len(phone) == 8:
            return f"{ddd} 9{phone}"   
           
        elif len(phone) == 9 and phone[0] == '9':
            return f"{ddd} {phone}"
        
        else:
            return 'Número inválido.'

