class Student():
    def __init__(
        self,
        student_id=0,
        student_name="xyz",
        student_f_name="none",
        student_phone_number="not given",
        student_address="not present",
        student_fees="0",
        student_trade_name="none"
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees
        self.student_trade_name = student_trade_name    

    def getStudent(self):    
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees},classname = {self.student_trade_name}"     
